# Tesi di specializzazione — la funzione consultiva della Corte dei conti dopo la legge n. 1/2026

Repository di lavoro per la costruzione della tesi di specializzazione in diritto amministrativo e scienza
dell'amministrazione, materia contabilità pubblica.

## Come si usa

1. Carica il materiale in `materiali/` (vedi `materiali/README.md`).
2. Invoca la skill: `/tesi-contabilita-pubblica`, oppure chiedi semplicemente la fase che ti serve
   («fai la ricognizione del materiale», «prepara la traccia per il relatore», «scrivi il capitolo IV»).
3. Gli output sono prodotti in `output/`, una fase per file.

## Struttura

- `.claude/skills/tesi-contabilita-pubblica/` — la skill principale: metodo, riferimenti, template
- `.claude/skills/write-academic-report/` — skill importata: lavorazione in parallelo e composizione del documento
- `materiali/` — le fonti fornite dall'utente
- `output/` — inventario, schede di lettura, ricognizione, traccia, indice, capitoli, revisione, tesi composta

## Fasi

`F0` intake e inventario → `F1` schede di lettura → `F2` ricognizione per problemi → `F3` traccia orientativa per il
relatore → `F4` indice ragionato → `F5` stesura dei capitoli → `F6` revisione di note e bibliografia →
`F7` composizione del documento consegnabile.

Nessuna fase si anticipa prima che la precedente sia chiusa. Nessuna fonte entra in tesi se non è stata letta nel
materiale o verificata su fonte ufficiale.

## Le due skill

`tesi-contabilita-pubblica` decide **che cosa** si scrive e **come si cita**. `write-academic-report` — importata da
[PHY041/claude-skill-write-academic-report](https://github.com/PHY041/claude-skill-write-academic-report), MIT —
fornisce **l'orchestrazione in parallelo** (schedatura e stesura su più agenti) e **la composizione tipografica**
(template LaTeX, compilazione, audit dei rinvii). In caso di contrasto prevale la prima; le indicazioni del relatore
prevalgono su entrambe.

Quella skill è nata per report STEM in inglese: prima di usarla va letto
`.claude/skills/write-academic-report/references/adattamento-tesi-giuridica.md`, che dice quali sue parti valgono qui
e quali no. In particolare, il suo verificatore di citazioni non copre deliberazioni della Corte dei conti,
giurisprudenza italiana e riviste giuridiche senza DOI: su quelle fonti un esito «non trovato» non significa nulla.

## Controlli automatici

```bash
# note, schede e registro delle fonti (durante e a fine stesura)
python3 .claude/skills/write-academic-report/scripts/audit_note_tesi.py
python3 .claude/skills/write-academic-report/scripts/audit_note_tesi.py --consegna   # prima di consegnare

# rinvii interni ed etichette duplicate (dopo la composizione in LaTeX)
python3 .claude/skills/write-academic-report/scripts/cross_ref_audit.py output/tesi-latex/

# citazioni della sola dottrina indicizzata (DOI, open access)
python3 .claude/skills/write-academic-report/scripts/citation_checker.py <file.bib>
```
