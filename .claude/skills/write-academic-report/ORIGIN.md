# Provenienza e modifiche locali

## Origine

Questa skill è importata da un progetto di terzi:

- **Repository**: https://github.com/PHY041/claude-skill-write-academic-report
- **Autore**: Haoyang Pang
- **Licenza**: MIT (dichiarata nel `README.md` d'origine; il repository non contiene un file `LICENSE`)
- **Commit importato**: `ff656b05a7f696134192c318e6738f2653db89de` (2026-03-22)
- **Data di importazione**: 2026-09-21

I file `SKILL.md`, `README.md`, `references/`, `scripts/`, `templates/university-thesis/` e `tests/`
provengono da quel repository. Per aggiornarli, ri-clonare l'origine e riapplicare le modifiche
elencate qui sotto.

## Modifiche apportate in questo repository

1. **`SKILL.md`** — sostituita la `description` del front matter (l'originale era in inglese e tarata su
   report STEM: non si sarebbe attivata su richieste in italiano) e aggiunto in testa il richiamo a
   `references/adattamento-tesi-giuridica.md`. Il resto del testo è invariato.
2. **`references/adattamento-tesi-giuridica.md`** — aggiunto. È lo strato di raccordo fra questa skill e
   `tesi-contabilita-pubblica`: dice quali parti della pipeline valgono per una tesi giuridica italiana,
   quali non valgono e perché.
3. **`templates/tesi-giuridica-italiana/`** — aggiunto. Template LaTeX per la tesi di specializzazione
   (A4, italiano, capitoli in numeri romani, note a piè di pagina, bibliografia per sezioni). Il template
   originale `university-thesis/` resta come riferimento ma non si usa qui.
4. **`scripts/audit_note_tesi.py`** — aggiunto. Controlla le note dei capitoli in Markdown contro il
   registro delle fonti: è l'equivalente di `cross_ref_audit.py` per la fase di stesura, che in questo
   repository avviene in Markdown e non in LaTeX.

Nessun file originale è stato cancellato o riscritto nel merito.
