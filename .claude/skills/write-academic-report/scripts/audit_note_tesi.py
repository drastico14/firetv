#!/usr/bin/env python3
"""
Audit delle note e del registro delle fonti — tesi giuridica italiana.

È l'equivalente di cross_ref_audit.py per la fase di stesura, che in questo
repository avviene in Markdown: cross_ref_audit.py lavora su \\label e \\cite
LaTeX e serve solo dopo la composizione tipografica (F7), quando ormai è tardi
per accorgersi che una nota non ha una fonte dietro.

Controlla, sui capitoli in output/capitoli/:
  1. marcatori di lavorazione rimasti nel testo
     ([FONTE DA REPERIRE], [DA VERIFICARE], [ORIENTAMENTO NON UNIVOCO],
      [IPOTESI RICOSTRUTTIVA]);
  2. note usate e mai definite, definite e mai usate, definite due volte;
  3. note che non richiamano alcun id del registro delle fonti;
  4. schede di lettura senza riga nel registro, e viceversa;
  5. fonti del registro mai utilizzate in tesi.

Convenzioni attese (v. references/adattamento-tesi-giuridica.md):
  - le note sono note Markdown:  uso "[^12]", definizione "[^12]: ...";
  - la definizione della nota contiene l'id della fonte come compare nella
    prima colonna di output/registro-fonti.md;
  - le schede stanno in output/schede/, una per fonte, e il titolo è
    "# Scheda di lettura — <id>".

Uso:
    python3 audit_note_tesi.py                 # dalla radice del repository
    python3 audit_note_tesi.py /percorso/repo
    python3 audit_note_tesi.py --consegna      # i marcatori diventano errori
    python3 audit_note_tesi.py --json
"""

import re
import sys
import json
from pathlib import Path
from collections import defaultdict

MARCATORI = [
    "FONTE DA REPERIRE",
    "DA VERIFICARE",
    "ORIENTAMENTO NON UNIVOCO",
    "IPOTESI RICOSTRUTTIVA",
]

RE_NOTA_DEF = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$")
RE_NOTA_USO = re.compile(r"\[\^([^\]]+)\](?!:)")
RE_RINVIO_INTERNO = re.compile(r"\b(supra|infra|ivi|ibidem)\b", re.IGNORECASE)
RE_SCHEDA_ID = re.compile(r"^#\s*Scheda di lettura\s*[—–-]\s*(.+?)\s*$", re.MULTILINE)


def leggi_registro(path):
    """Estrae gli id dalla prima colonna della tabella del registro fonti."""
    ids = []
    if not path.exists():
        return ids, [f"registro delle fonti assente: {path}"]
    problemi = []
    for riga in path.read_text(encoding="utf-8").splitlines():
        riga = riga.strip()
        if not riga.startswith("|"):
            continue
        celle = [c.strip().strip("`*") for c in riga.strip("|").split("|")]
        if not celle or not celle[0]:
            continue
        primo = celle[0]
        if set(primo) <= set("-: "):          # riga separatrice
            continue
        if primo.lower() in ("id", "identificativo"):   # intestazione
            continue
        ids.append(primo)
        if len(celle) >= 3 and not celle[2]:
            problemi.append(f"registro: la fonte «{primo}» non ha citazione completa")
    return ids, problemi


def analizza_capitoli(files, ids_registro):
    usi = defaultdict(list)           # nota -> [file:riga]
    definizioni = defaultdict(list)   # nota -> [file:riga]
    testo_note = {}                   # (file, nota) -> testo
    marcatori = []
    id_usati = set()

    for f in files:
        for n, riga in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for m in MARCATORI:
                if m in riga:
                    marcatori.append(f"{f}:{n}: {riga.strip()[:110]}")
            d = RE_NOTA_DEF.match(riga)
            if d:
                definizioni[d.group(1)].append(f"{f}:{n}")
                testo_note[(f.name, d.group(1))] = d.group(2)
                continue
            for u in RE_NOTA_USO.finditer(riga):
                usi[u.group(1)].append(f"{f}:{n}")

    note_senza_fonte = []
    for (nome_file, nota), testo in sorted(testo_note.items()):
        richiamate = [i for i in ids_registro if i and i in testo]
        if richiamate:
            id_usati.update(richiamate)
        elif not RE_RINVIO_INTERNO.search(testo):
            note_senza_fonte.append(f"{nome_file} [^{nota}]: {testo[:90]}")

    return usi, definizioni, marcatori, note_senza_fonte, id_usati


def audit(radice):
    out = radice / "output"
    capitoli = sorted((out / "capitoli").glob("*.md")) if (out / "capitoli").is_dir() else []
    schede = sorted((out / "schede").glob("*.md")) if (out / "schede").is_dir() else []

    ids_registro, problemi_registro = leggi_registro(out / "registro-fonti.md")
    usi, definizioni, marcatori, note_senza_fonte, id_usati = analizza_capitoli(capitoli, ids_registro)

    ids_schede = []
    for s in schede:
        m = RE_SCHEDA_ID.search(s.read_text(encoding="utf-8"))
        ids_schede.append(m.group(1).strip() if m else f"<senza id: {s.name}>")

    r = {
        "capitoli_esaminati": [str(c) for c in capitoli],
        "schede_esaminate": len(schede),
        "fonti_nel_registro": len(ids_registro),
        "marcatori_residui": marcatori,
        "note_usate_non_definite": sorted(
            f"[^{k}] usata in {', '.join(v)}" for k, v in usi.items() if k not in definizioni
        ),
        "note_definite_non_usate": sorted(
            f"[^{k}] definita in {', '.join(v)}" for k, v in definizioni.items() if k not in usi
        ),
        "note_definite_due_volte": sorted(
            f"[^{k}] in {', '.join(v)}" for k, v in definizioni.items() if len(v) > 1
        ),
        "note_senza_fonte_nel_registro": note_senza_fonte,
        "schede_senza_riga_nel_registro": sorted(set(ids_schede) - set(ids_registro)),
        "registro_senza_scheda": sorted(set(ids_registro) - set(ids_schede)),
        "fonti_mai_usate_in_tesi": sorted(set(ids_registro) - id_usati),
        "problemi_registro": problemi_registro,
    }
    return r


BLOCCANTI = [
    ("note_usate_non_definite", "note richiamate nel testo e mai definite"),
    ("note_definite_due_volte", "note definite più volte"),
    ("note_senza_fonte_nel_registro", "note che non rinviano ad alcuna fonte del registro"),
    ("schede_senza_riga_nel_registro", "schede di lettura senza riga nel registro"),
    ("registro_senza_scheda", "fonti nel registro senza scheda di lettura"),
    ("problemi_registro", "righe del registro incomplete"),
]

AVVERTENZE = [
    ("note_definite_non_usate", "note definite e mai richiamate"),
    ("fonti_mai_usate_in_tesi", "fonti lette e non sfruttate (da valutare, non necessariamente un errore)"),
]


def stampa(r, consegna):
    print("\n" + "=" * 66)
    print("  AUDIT DELLE NOTE — tesi di specializzazione")
    print("=" * 66)
    print(f"  capitoli: {len(r['capitoli_esaminati'])}   "
          f"schede: {r['schede_esaminate']}   fonti nel registro: {r['fonti_nel_registro']}")

    if not r["capitoli_esaminati"]:
        print("\n  Nessun capitolo in output/capitoli/: niente da controllare.")
        print("=" * 66 + "\n")
        return 0

    errori = 0
    for chiave, etichetta in BLOCCANTI:
        voci = r[chiave]
        if voci:
            errori += len(voci)
            print(f"\n  ERRORE — {etichetta} ({len(voci)})")
            print("  " + "-" * 56)
            for v in voci[:25]:
                print(f"    {v}")
            if len(voci) > 25:
                print(f"    ... e altre {len(voci) - 25}")

    marc = r["marcatori_residui"]
    if marc:
        livello = "ERRORE" if consegna else "AVVISO"
        if consegna:
            errori += len(marc)
        print(f"\n  {livello} — marcatori di lavorazione ancora nel testo ({len(marc)})")
        print("  " + "-" * 56)
        for v in marc[:25]:
            print(f"    {v}")
        if len(marc) > 25:
            print(f"    ... e altri {len(marc) - 25}")

    for chiave, etichetta in AVVERTENZE:
        voci = r[chiave]
        if voci:
            print(f"\n  AVVISO — {etichetta} ({len(voci)})")
            print("  " + "-" * 56)
            for v in voci[:25]:
                print(f"    {v}")
            if len(voci) > 25:
                print(f"    ... e altre {len(voci) - 25}")

    print("\n" + "=" * 66)
    if errori:
        print(f"  ESITO: {errori} errori da sanare prima di procedere")
    else:
        print("  ESITO: nessun errore" + (" (solo avvisi)" if marc or any(r[k] for k, _ in AVVERTENZE) else ""))
    print("=" * 66 + "\n")
    return errori


def main():
    import argparse

    p = argparse.ArgumentParser(
        description="Controlla note, schede e registro delle fonti di una tesi giuridica"
    )
    p.add_argument("radice", nargs="?", default=".",
                   help="radice del repository della tesi (default: directory corrente)")
    p.add_argument("--consegna", action="store_true",
                   help="tratta i marcatori di lavorazione residui come errori bloccanti")
    p.add_argument("--json", action="store_true", help="output in JSON")
    a = p.parse_args()

    radice = Path(a.radice)
    if not radice.is_dir():
        print(f"Errore: {radice} non è una directory", file=sys.stderr)
        sys.exit(2)

    r = audit(radice)

    if a.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
        errori = sum(len(r[k]) for k, _ in BLOCCANTI)
        if a.consegna:
            errori += len(r["marcatori_residui"])
    else:
        errori = stampa(r, a.consegna)

    sys.exit(1 if errori else 0)


if __name__ == "__main__":
    main()
