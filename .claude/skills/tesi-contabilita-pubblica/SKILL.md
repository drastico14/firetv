---
name: tesi-contabilita-pubblica
description: Costruisce, passo per passo, una tesi di specializzazione in diritto amministrativo e scienza dell'amministrazione in materia di contabilità pubblica, con specifico riferimento alla funzione consultiva della Corte dei conti dopo la legge 7 gennaio 2026 n. 1. Da usare quando l'utente carica materiale (sentenze, pareri, deliberazioni, dottrina, testi normativi, linee guida del relatore) e chiede di: fare la ricognizione per punti degli aspetti e delle criticità, predisporre una traccia orientativa per il relatore, costruire o rivedere l'indice, redigere o revisionare capitoli e paragrafi, formulare proposte de iure condendo, sistemare note e bibliografia. Attivare anche per richieste come "tesi", "traccia", "indice ragionato", "capitolo", "nota a piè di pagina", "ricognizione del materiale", "schede di lettura", "funzione consultiva", "pareri della Corte dei conti", "legge 1/2026".
---

# Tesi di specializzazione — contabilità pubblica / funzione consultiva della Corte dei conti

## 1. Regole non negoziabili

Sono regole di metodo: la loro violazione compromette la tesi davanti al relatore.

1. **Non inventare mai fonti.** Nessuna sentenza, deliberazione, pagina, rivista, autore o numero di articolo può essere citato se non è stato letto nel materiale fornito dall'utente o verificato su fonte ufficiale. Se serve un appiglio non disponibile, scrivere `[FONTE DA REPERIRE: …]` nel testo.
2. **Distinguere sempre tre livelli** e tenerli tipograficamente separati nel lavoro: (a) *dato normativo*; (b) *elaborazione giurisprudenziale o dottrinale documentata nel materiale*; (c) *opinione ricostruttiva dell'autore*. La confusione fra (b) e (c) è il difetto più penalizzato.
3. **Ogni affermazione sostanziale ha una nota.** La nota rinvia a una scheda di fonte (v. `templates/scheda-fonte.md`) tracciata nel registro delle fonti.
4. **Marcare l'incertezza**, non nasconderla: `[DA VERIFICARE sul testo ufficiale]`, `[ORIENTAMENTO NON UNIVOCO]`, `[IPOTESI RICOSTRUTTIVA]`.
5. **Non riscrivere in italiano "da AI".** Registro giuridico italiano, periodi articolati ma sorvegliati, nessun elenco puntato al posto dell'argomentazione nel corpo dei capitoli, nessuna enfasi retorica ("cruciale", "fondamentale snodo", tricolon). Gli elenchi si usano nella traccia e negli schemi, non nella prosa della tesi.
6. **La legge n. 1/2026 è una legge delega parzialmente self-executing**: alcune disposizioni sono immediatamente precettive, altre rinviano a decreti legislativi. Prima di ogni affermazione, chiarire in quale dei due piani si colloca. Questa distinzione è il cuore del tema assegnato.

## 2. Fasi del lavoro

Il lavoro procede per fasi. Non anticipare una fase se la precedente non è chiusa e approvata dall'utente.

| Fase | Output | Cartella |
|---|---|---|
| F0 — Intake | inventario del materiale, segnalazione lacune | `output/F0-inventario.md` |
| F1 — Schede di lettura | una scheda per documento | `output/schede/` |
| F2 — Ricognizione | ricognizione per punti di aspetti e criticità | `output/F2-ricognizione.md` |
| F3 — Traccia orientativa | documento da sottoporre al relatore | `output/F3-traccia-orientativa.md` |
| F4 — Indice ragionato | indice con carico argomentativo per paragrafo | `output/F4-indice.md` |
| F5 — Stesura | capitoli, uno per file | `output/capitoli/` |
| F6 — Revisione | controllo note, coerenza, bibliografia | `output/F6-revisione.md` |

### F0 — Intake del materiale

1. Il materiale dell'utente sta in `materiali/`. Leggerlo **tutto e integralmente**, non per campione. Per i PDF usare `pdftotext -layout`; per i .docx la skill `docx`; se un PDF è scansionato, segnalarlo e chiedere OCR invece di indovinare il contenuto.
2. Produrre l'inventario: per ciascun file → tipologia (norma / giurisprudenza costituzionale / deliberazione Corte dei conti in sede di controllo / sentenza contabile / dottrina / atto parlamentare / linee guida del relatore), data, organo, oggetto in una riga.
3. Dichiarare esplicitamente **cosa manca** rispetto a quanto servirebbe (v. `references/quadro-normativo.md`, colonna "essenziale").
4. Se tra il materiale ci sono indicazioni del relatore o del corso (lunghezza, stile citazionale, struttura obbligata), esse **prevalgono** su questa skill: segnalarlo e adeguarsi.

### F1 — Schede di lettura

Una scheda per documento, con il template `templates/scheda-fonte.md`. La scheda è il solo tramite consentito fra materiale e tesi: nulla entra in tesi che non sia passato per una scheda. Ogni scheda registra la *citazione esatta* (con numero di pagina o paragrafo) dei passaggi che si intende utilizzare.

### F2 — Ricognizione per punti

Usare `references/griglia-ricognizione.md`. La ricognizione non è un riassunto: è la mappa dei **problemi**. Per ciascun problema indicare: come si poneva prima della riforma, cosa ha fatto la riforma, cosa resta aperto, chi lo segnala (fonte), cosa rinvia al decreto legislativo.

### F3 — Traccia orientativa per il relatore

Usare `templates/traccia-orientativa.md`. È un documento breve (5–8 pagine) che deve mostrare al relatore tre cose: che il tema è stato problematizzato e non solo descritto; che esiste un'ipotesi di ricerca falsificabile; che la divisione in capitoli regge. Va accompagnata da 3–5 domande esplicite al relatore su cui si chiede un indirizzo (perimetro, taglio, se includere o no il profilo comparato, se sviluppare le proposte de iure condendo).

### F4 — Indice ragionato

Ogni paragrafo dell'indice porta con sé: la tesi che sostiene, le fonti su cui poggia (rinvio alle schede), la lunghezza stimata. Un paragrafo senza fonti nell'indice è un paragrafo che non si scriverà.

### F5 — Stesura

Un file per capitolo. Prima del testo, riportare in testa al file l'estratto dell'indice ragionato relativo a quel capitolo, così da controllare gli scostamenti. Le note seguono `references/metodo-citazione.md`.

### F6 — Revisione

Controlli obbligatori, nell'ordine: (1) ogni nota rinvia a una fonte esistente nel registro; (2) nessun `[FONTE DA REPERIRE]` o `[DA VERIFICARE]` residuo non segnalato all'utente; (3) coerenza fra tesi dichiarata nell'introduzione e conclusioni; (4) bibliografia completa e ordinata; (5) passaggio finale con la skill `humanizer` sui capitoli, per eliminare gli stilemi da testo generato.

## 3. Il nucleo argomentativo del tema

Il tema assegnato — *la funzione consultiva della Corte dei conti alla luce della legge n. 1 del 2026* — regge su una domanda di ricerca che va tenuta ferma in tutto il lavoro:

> dopo la riforma, la funzione consultiva della Corte dei conti è ricostruibile come **funzione unitaria** (unico istituto con varianti procedurali), oppure convivono **più funzioni consultive** eterogenee per legittimazione, oggetto, effetti e collocazione costituzionale?

Il materiale dell'utente serve a rispondere, non a illustrare. Le due ipotesi vanno messe alla prova sugli indici individuati in `references/quadro-normativo.md` §4 (legittimazione soggettiva, oggetto, effetti sulla responsabilità, organo competente, nomofilachia, rapporto con controllo e giurisdizione).

Sul versante *de iure condendo*, il perno è che si tratta di **legge delega**: ogni criticità rilevata va classificata come (i) risolvibile in sede di decreto legislativo entro i principi di delega; (ii) risolvibile solo con nuova legge; (iii) rimessa alla prassi della Corte o al giudice. La proposta che ignora questa classificazione non è utilizzabile. Schema in `references/de-iure-condendo.md`.

## 4. Riferimenti di questa skill

- `references/quadro-normativo.md` — mappa delle fonti da padroneggiare, con flag di verifica
- `references/griglia-ricognizione.md` — griglia dei problemi e matrice unitarietà/pluralità
- `references/de-iure-condendo.md` — metodo per formulare le proposte su legge delega
- `references/metodo-citazione.md` — stile citazionale giuridico italiano
- `references/struttura-tesi.md` — architettura dei capitoli e alternative
- `templates/scheda-fonte.md`, `templates/traccia-orientativa.md`, `templates/indice-ragionato.md`

## 5. Avvertenza sulla conoscenza pregressa

Il contenuto della legge n. 1/2026 e i commenti dottrinali **non vanno ricostruiti a memoria**. Vanno letti nel materiale dell'utente o verificati su fonte ufficiale (Gazzetta Ufficiale, Normattiva, sito istituzionale della Corte dei conti). Le indicazioni contenute in `references/quadro-normativo.md` sono una *lista di controllo*, non una fonte citabile.
