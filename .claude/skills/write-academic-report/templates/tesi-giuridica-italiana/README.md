# Template LaTeX — tesi giuridica italiana

Impianto per la tesi di specializzazione in contabilità pubblica. Sostituisce, per questo lavoro, il template
`university-thesis/` della skill originale, che è tarato su report STEM in inglese.

## Differenze rispetto a `university-thesis/`

| | `university-thesis/` | `tesi-giuridica-italiana/` |
|---|---|---|
| Lingua | inglese | italiano (`babel`) |
| Capitoli | 1–6, arabi, struttura sperimentale | I–VII, romani, struttura ricostruttiva |
| Citazioni | BibTeX + `natbib`, autore-anno | note a piè di pagina, bibliografia a mano per sezioni |
| Figure | pipeline matplotlib, palette | nessuna: solo tabelle sinottiche |
| Interlinea | singola | 1,5 |

## Uso

```bash
cp -r .claude/skills/write-academic-report/templates/tesi-giuridica-italiana output/tesi-latex
cd output/tesi-latex
# travasare i capitoli da output/capitoli/*.md, un file per capitolo
tectonic main.tex        # oppure: latexmk -pdf main.tex
```

Poi, sempre:

```bash
python3 ../../.claude/skills/write-academic-report/scripts/cross_ref_audit.py .
```

Due esiti dello script sono attesi e non vanno corretti: `\ref{#1} undefined`, che è la definizione della
macro `\supra` in `preambolo.tex` letta come rinvio reale, e l'elenco delle `ORPHANED LABELS`, che sui capitoli
ancora vuoti comprende tutte le etichette. Conta invece ogni etichetta duplicata e ogni altro rinvio cieco.

## Prima di consegnare

- `grep -rn "FONTE DA REPERIRE\|DA VERIFICARE\|IPOTESI RICOSTRUTTIVA" .` deve dare esito vuoto, oppure ogni
  occorrenza deve essere stata segnalata all'utente e accettata consapevolmente;
- il frontespizio va sostituito con quello della scuola, se esiste;
- la numerazione delle note è continua su tutta la tesi: per farla ripartire da ogni capitolo, commentare
  `\counterwithout{footnote}{chapter}` in `preambolo.tex`.

## File

```
main.tex                  documento principale, elenco degli \input
preambolo.tex             pacchetti, stile, comandi (\supra, \daverificare, ambiente citazione)
frontespizio.tex          da sostituire con quello dell'ateneo, se fornito
capitoli/                 introduzione, cap. I–VII, conclusioni
bibliografia.tex          bibliografia per sezioni, composta a mano
```
