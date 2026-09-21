# Adattamento alla tesi giuridica italiana

Questo documento raccorda `write-academic-report` (pensata per report STEM: repository di ricerca, esperimenti,
figure, LaTeX) con `tesi-contabilita-pubblica` (tesi di specializzazione in diritto, fonti documentali, note a
piè di pagina). Le due skill convivono così:

> **`tesi-contabilita-pubblica` decide cosa scrivere e come citarlo. `write-academic-report` fornisce
> l'orchestrazione in parallelo e la composizione tipografica finale.**

In caso di conflitto prevale sempre `tesi-contabilita-pubblica`. Le indicazioni del relatore prevalgono su
entrambe.

---

## 1. Che cosa si prende e che cosa si scarta

| Parte della skill originale | Qui | Perché |
|---|---|---|
| Regola «mai inventare citazioni» | **Si prende, rafforzata** | Coincide con la regola 1 di `tesi-contabilita-pubblica`. Nel diritto il danno è maggiore: una deliberazione inesistente citata al relatore chiude il lavoro. |
| Architettura a ondate (Wave 0/1/2) | **Si prende, riadattata** | Vedi §2. Il principio «prima i dati, poi la prosa» diventa «prima le schede, poi i capitoli». |
| Cancello di fine ondata | **Si prende** | Nessun capitolo si scrive su materiale non ancora schedato. |
| `cross_ref_audit.py` | **Si prende in F7** | Serve solo quando esiste il sorgente LaTeX. |
| `citation_checker.py` | **Si prende con riserva** | Vedi §4: sulle fonti giuridiche italiane è quasi cieco. |
| Template `university-thesis/` | **Si scarta** | Struttura STEM (metodologia, setup sperimentale, risultati), inglese, citazioni autore-anno. Si usa `templates/tesi-giuridica-italiana/`. |
| Agenti 0B/0C (analisi del codice e del sistema) | **Si scartano** | Non esiste un codice sorgente da analizzare. |
| Agenti 0D/0E (storia degli esperimenti, statistiche) | **Si scartano** | Non esistono dati sperimentali. |
| Agente 0F (pipeline figure, palette, matplotlib) | **Si scarta** | Una tesi giuridica non ha figure. Gli unici elementi grafici ammessi sono tabelle sinottiche (confronto fra assetto anteriore e posteriore alla riforma, matrice degli indici di unitarietà). |
| Modelli di capitolo Ch1–Ch6 | **Si scartano** | Si segue `tesi-contabilita-pubblica/references/struttura-tesi.md`. |
| Guida stilistica (Gopen & Swan, Lipton) | **Si prende in parte** | Vedi §5. |
| Sezione «Limitations» | **Si prende, ricollocata** | Diventa «limiti dell'indagine» in introduzione e nelle conclusioni. |

---

## 2. Le ondate, tradotte nelle fasi F0–F7

La pipeline originale ha tre ondate. Qui sono quattro, e la parallelizzazione dei capitoli è **molto più
limitata**: in una tesi giuridica i capitoli non sono indipendenti, perché il capitolo che prende posizione
poggia su quelli che ricostruiscono.

### Ondata A — materiale (fasi F0–F2)

Parallelizzabile per **gruppi omogenei di documenti**, un agente per gruppo:

| Agente | Materiale | Output |
|---|---|---|
| A1 | testi normativi (l. n. 1/2026, l. n. 20/1994, TUEL, c.g.c., d.lgs. attuativi) | schede + estratti testuali letterali degli articoli rilevanti |
| A2 | giurisprudenza costituzionale e di legittimità | schede |
| A3 | deliberazioni della Corte dei conti (controllo, SS.RR., QMIG/PAR) | schede |
| A4 | dottrina | schede |
| A5 | atti parlamentari, relazioni, linee guida del relatore | schede + vincoli imposti al lavoro |

Ogni agente scrive **solo** schede con il template `templates/scheda-fonte.md` e alimenta
`output/registro-fonti.md`. Nessun agente di questa ondata scrive prosa da tesi.

**Cancello di fine ondata A** — non si passa oltre finché:

- [ ] ogni file di `materiali/` compare nell'inventario `output/F0-inventario.md`;
- [ ] ogni documento utilizzabile ha una scheda;
- [ ] ogni scheda riporta la citazione esatta, con pagina o paragrafo, dei passaggi che si intende usare;
- [ ] le lacune sono dichiarate all'utente, non aggirate;
- [ ] il registro delle fonti non contiene righe con citazione incompleta.

La ricognizione per problemi (F2) si fa **dopo**, in un passaggio unico e non parallelizzato: serve una testa
sola, perché è lì che si vedono le connessioni fra documenti diversi.

### Ondata B — impianto (fasi F3–F4)

Non si parallelizza. Traccia orientativa e indice ragionato sono atti di una sola mano e vanno approvati
dall'utente prima della stesura.

### Ondata C — stesura (fase F5)

Qui sta il guadagno di tempo, ma con vincoli di dipendenza reali:

```
C1 (in parallelo)   Cap. I  — inquadramento costituzionale
                    Cap. II — assetto anteriore alla riforma
                    Cap. III— struttura e ratio della legge n. 1/2026

C2 (in parallelo, dopo C1)
                    Cap. IV — il nuovo procedimento consultivo
                    Cap. V  — effetti del parere sulla responsabilità

C3 (sequenziale, dopo C2)
                    Cap. VI — funzione unitaria o pluralità di funzioni

C4 (dopo C3)        Cap. VII— prospettive de iure condendo
                    Introduzione e Conclusioni (per ultime: l'introduzione
                    si scrive quando si sa che cosa si è dimostrato)
```

Perché non tutto in parallelo: il capitolo VI è il luogo della presa di posizione e usa come premesse gli indici
ricostruiti in IV e V; il VII classifica le criticità emerse in VI secondo lo schema della legge delega. Scriverli
insieme produce un lavoro che si contraddice.

Che cosa riceve ciascun agente di stesura, e nient'altro:

1. l'estratto dell'indice ragionato relativo al suo capitolo (tesi da sostenere, fonti, lunghezza);
2. le sole schede richiamate da quell'estratto, più il registro delle fonti;
3. `references/metodo-citazione.md` e le regole non negoziabili;
4. i capitoli già scritti da cui dipende, in sola lettura, per i rinvii interni.

Ogni agente restituisce un file in `output/capitoli/`, più l'elenco delle note prodotte con l'`id` della fonte
richiamata.

### Ondata D — assemblaggio (fasi F6–F7)

Sequenziale. Vedi §3.

---

## 3. F7 — composizione tipografica (nuova fase)

`tesi-contabilita-pubblica` si ferma a F6 (revisione sul Markdown). F7 produce il documento consegnabile.

1. **Scelta del formato.** Se la scuola accetta il Word, esportare da Markdown con la skill `docx` e fermarsi qui:
   il LaTeX ha senso solo se il documento finale lo richiede o se l'utente lo preferisce. La conversione è
   comunque a senso unico: dopo F7 le correzioni si fanno sul formato finale, non più sul Markdown.
2. **Impianto LaTeX**: copiare `templates/tesi-giuridica-italiana/` in `output/tesi-latex/` e travasare i capitoli,
   un file per capitolo, mantenendo i nomi.
3. **Note**: le note del Markdown diventano `\footnote{}`. Non si usa BibTeX né `natbib`: la bibliografia giuridica
   italiana è per sezioni e si compone a mano (vedi `bibliografia.tex`), e il sistema autore-anno è estraneo a
   questo tipo di lavoro.
4. **Etichette e rinvii interni**: i rinvii `V. supra, § 2.3` diventano `\label{}` / `\ref{}` con prefisso di
   capitolo (`sez:cap4:oggetto`), come prescrive la skill originale. È qui che serve
   `python3 scripts/cross_ref_audit.py output/tesi-latex/`, che intercetta etichette duplicate e rinvii ciechi.
5. **Compilazione**: `tectonic main.tex`, oppure `latexmk -pdf main.tex`. Il template è scritto per `pdflatex`,
   senza pacchetti esotici. Vedi `references/compilation-guide.md`.
6. **Controllo finale**: la checklist post-compilazione della skill originale, più la verifica che la numerazione
   dei capitoli sia in numeri romani e che l'indice corrisponda a `output/F4-indice.md`.

---

## 4. `citation_checker.py`: quando serve e quando inganna

Lo script verifica una voce bibliografica contro CrossRef, Semantic Scholar e OpenAlex. Quei tre archivi
**non indicizzano** la maggior parte di ciò che si cita in questa tesi:

- le deliberazioni e i pareri della Corte dei conti (nessuna delle tre banche dati li contiene);
- le sentenze della Corte costituzionale, della Cassazione e del Consiglio di Stato;
- le riviste giuridiche italiane, che in larga parte non assegnano DOI (*Riv. Corte conti*, *Foro it.*,
  *Giur. cost.*, *Dir. proc. amm.*, *Azienditalia*, e altre);
- gli atti parlamentari e i dossier dei servizi studi.

Su queste fonti un esito `not found` **non significa nulla**: non è indizio di invenzione. Usarlo come tale
porterebbe a cancellare fonti vere.

**Regola operativa.**

| Tipo di fonte | Come si verifica |
|---|---|
| Dottrina straniera, articoli con DOI, open access | `python3 scripts/citation_checker.py <file.bib>` |
| Dottrina italiana, riviste giuridiche | scheda di lettura + registro fonti: si cita solo ciò che è nel materiale o è stato verificato sul catalogo dell'editore o su una banca dati giuridica |
| Norme | testo ufficiale in *Gazzetta Ufficiale* / Normattiva |
| Giurisprudenza e deliberazioni | banca dati ufficiale dell'organo (per la Corte dei conti: banca dati delle deliberazioni delle sezioni di controllo) |

Per tutto ciò che il checker non copre, il controllo automatico è `scripts/audit_note_tesi.py`, che confronta le
note dei capitoli con il registro delle fonti e segnala i marcatori di incertezza rimasti nel testo.

---

## 5. Stile: che cosa resta della guida originale

`references/writing-guide.md` è scritta per la prosa scientifica inglese. Alcune prescrizioni sono trasferibili,
altre sono dannose in un testo giuridico italiano.

**Si applicano** (sono regole di leggibilità, non di lingua):

- posizione tematica e posizione d'enfasi: il noto a inizio periodo, il nuovo alla fine;
- soggetto e verbo vicini; periodo lungo ma con struttura riconoscibile;
- un paragrafo, un'idea;
- terminologia costante: scelto un termine per un concetto, non si varia per eleganza (in diritto la variazione
  lessicale è ambiguità: *parere*, *pronuncia*, *deliberazione* non sono sinonimi);
- ogni affermazione porta l'evidenza che la regge.

**Non si applicano**:

- «voce attiva sempre», «*We show*…»: nella tesi italiana si usa la forma impersonale o la prima persona plurale
  attenuata, e il soggetto è spesso l'istituto, non l'autore;
- «eliminare le attenuazioni»: *sembra*, *pare preferibile*, *non è pacifico* sono qualificazioni del grado di
  certezza di una tesi, e in diritto sono informazione, non timidezza. Si eliminano quando mascherano una
  mancata presa di posizione, non per regola;
- l'uso degli elenchi puntati nel corpo del testo: `tesi-contabilita-pubblica` lo vieta nella prosa dei capitoli;
- le convenzioni tipografiche STEM (tabelle `booktabs` con frecce di direzione, valori in grassetto, simboli
  statistici).

Il passaggio finale con la skill `humanizer` previsto da F6 resta obbligatorio e prevale su ogni indicazione
stilistica di questa skill.
