---
workspace: flora
value_stream: tmt.tuin-onderhoud
value_stream-fasen: ["tmt.01"]
canon_github_url: https://github.com/hans-blok/mandarin-canon.git
---

# Beleid voor de flora workspace

Deze workspace hoort bij de waardestroom **Tuin Management & Tuinonderhoud** **tmt.tuin-onderhoud**.

## Verplichte leesvolgorde van grondslagen

Elke geautomatiseerde rol, agent of runner hanteert bij aanvang van zijn functioneren de volgende verplichte leesvolgorde:

**In de centrale canon repository** (`https://github.com/hans-blok/mandarin-canon.git`):
1. `grondslagen/.algemeen/` — inclusief de constitutie
2. grondslagen van de toegewezen value stream (`grondslagen/{value-stream-code}/`)
3. grondslagen van de toegewezen value-stream-fase (`grondslagen/{value-stream-code}/{value-stream-code}.{fase}/`)

**In deze workspace**:
4. workspace-specifiek beleid (dit bestand)

Het overslaan, herordenen of impliciet toepassen van deze leesvolgorde is niet toegestaan.

**Zonder aantoonbare toepassing van de constitutie is handelen ongeldig.**

## Dit beleid is workspace-specifiek

Dit beleid beschrijft alleen de workspace-specifieke scope. Voor alle regels, uitzonderingen, details en constitutionele bepalingen volgen we volledig de richtlijnen in `hans-blok/mandarin-canon`.

De constitutie, algemene regels en governance voor alle workspaces staan in:
- https://github.com/hans-blok/mandarin-canon.git

## Canon Repository Synchronisatie

In alle geautomatiseerde en handmatige processen wordt de centrale canon repository geraadpleegd. Dit gebeurt altijd eerst met een `git pull` om te waarborgen dat de meest recente grondslagen worden gebruikt.

**Foutmelding**: Wanneer de mandarin-canon-repository niet bereikbaar is of niet kan worden gevonden, wordt een foutmelding gegeven en stopt het proces.

## Charter & Template Repository Configuratie

Deze workspace gebruikt externe agents uit de `mandarin-agents` repository. Charters en templates blijven in die repository; alleen prompts en agent-contracten worden hier gefetcht.

```yaml
external_agent_resources:
  # Primaire agent repository (schaalt automatisch voor alle agents)
  agent_repository:
    type: github  # Gebruik 'github' voor productie, 'local' voor development
    base_url: https://raw.githubusercontent.com/hans-blok/mandarin-agents/main/artefacten
    # BELANGRIJK: base_url is niet direct browseable, maar wordt gebruikt als prefix
    # voor individuele charter- en template-paden. Bijvoorbeeld:
    # {base_url}/aod/aod.02.core-framework-architect/core-framework-architect.charter.md
    # {base_url}/aod/aod.02.core-framework-architect/templates/core-framework-architect.structureer-gedrag.template.md
    
    # Voor lokale development (comment out base_url en gebruik):
    # type: local
    # local_path: ../mandarin-agents/artefacten
  
  # Pad-conventies (gebruikt door run_prompt.py om resources te vinden)
  # Variabelen: {vs} = value stream code, {fase} = fase nummer, {agent} = agent naam, {intent} = intent naam
  conventions:
    charter: "{vs}/{vs}.{fase}.{agent}/{agent}.charter.md"
    template: "{vs}/{vs}.{fase}.{agent}/templates/{agent}.{intent}.template.md"
  
  # Alleen uitzonderingen hier definiëren (optioneel)
  # Gebruik dit alleen voor agents die afwijken van de standaard pad-conventies
  exceptions: {}
    # voorbeeld:
    # legacy-agent:
    #   charter_path: special/path/legacy-agent.charter.md
    #   templates:
    #     legacy-intent: special/path/legacy.template.md
```

**Voorbeeld resource-opbouw voor agent `core-framework-architect` met `value_stream_fase: aod.02` en `intent: structureer-gedrag`:**
- Parse: `vs=aod`, `fase=02`, `agent=core-framework-architect`, `intent=structureer-gedrag`
- Charter pad via conventie: `aod/aod.02.core-framework-architect/core-framework-architect.charter.md`
- Template pad via conventie: `aod/aod.02.core-framework-architect/templates/core-framework-architect.structureer-gedrag.template.md`
- Volledige URLs:
  - Charter: `{base_url}/aod/aod.02.core-framework-architect/core-framework-architect.charter.md`
  - Template: `{base_url}/aod/aod.02.core-framework-architect/templates/core-framework-architect.structureer-gedrag.template.md`

**Development workflow:**
1. **Lokaal ontwikkelen**: Zet `type: local` en gebruik `local_path: ../mandarin-agents/artefacten`
2. **Na commit**: Zet `type: github` en gebruik `base_url` naar main branch

Nieuwe agents die de conventies volgen hoeven niet geconfigureerd te worden!

## Scope

### Wat we in deze workspace vastleggen

Deze workspace beheert alle documentatie en plannen voor **Perceel nr. 5** — een privétuin in Nederland. De scope omvat de volledige levenscyclus van tuinonderhoud: van inventarisatie en analyse tot concrete uitvoeringsplannen.

**Binnen scope:**

- **Inventarisatie & analyse**
  - Plattegrond en zonekaart van het perceel (`artefacten/schets-kaart.md`, `artefacten/schets-kaart-zon-schaduw.svg`)
  - Zon- en schaduwanalyse per border/zone (`artefacten/borders-zon-schaduw.md`)
  - Plantenregister per border (`artefacten/mijn-planten-borders.md`)
  - Materiaalinventaris (`artefacten/mijn-tuin-materiaal.md`)

- **Planning & uitvoering**
  - Seizoensgebonden onderhoudsplannen (`artefacten/plannen/`)
  - Mestplannen per border
  - Herinrichtingsplannen per zone (bijv. zone 11 gazon)
  - Snoeiplanning per plant en seizoen

- **Registratie**
  - Observatiedata en fotodocumentatie (`fotos/`)
  - Voortgang en aanpassingen per uitvoeringsperiode

- **Visuele artefacten**
  - SVG-kaarten van het perceel (incl. zon/schaduw visualisatie)
  - Generatiescripts voor SVG-output (`scripts/`)

### Wat niet in deze workspace hoort

- Onderhoud van andere percelen of tuinen
- Aankopen en leveranciersbeheer (alleen boodschappenlijsten als onderdeel van een plan)
- Financiële administratie of facturatie
- Algemene botanische kennisbank zonder directe koppeling aan Perceel nr. 5

## Workspace-specifieke aanvullingen

- **Taal:** alle documentatie is in het **Nederlands**
- **Zones vs. borders:** zones worden aangeduid als *border* in planningsdocumenten; de nummering volgt de PPTX-originele indeling (zones 1–12, inclusief zone 4 bij bijgebouw)
- **Fotoverwijzingen:** foto's worden opgeslagen in `fotos/` met naamconventie `zone-{nr}.foto.{datum}.{volgnr}.jpg`
- **Planningen:** concrete uitvoeringsplannen staan in `artefacten/plannen/`; elk plan bevat een boodschappenlijst en kalenderoverzicht
- **Datumsconventie:** referentiedatum voor zon/schaduw is **1 mei** (equivalent aan 11 augustus qua zondeclinatie)

---

*Laatste update: 4 april 2026 — Perceel nr. 5*
