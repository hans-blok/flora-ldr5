---
agent: documentatie-omvormer
intent: genereer-publicatiestructuur
execution_id: 685b
timestamp: 2026-04-04 15:41:31
initiatie: handmatig
---

# Audit log — documentatie-omvormer genereer-publicatiestructuur

## 1. Gelezen bronbestanden

| # | Bronbestand |
|---|-------------|
| 1 | `artefacten/borders-zon-schaduw.md` |
| 2 | `artefacten/mijn-planten-borders.md` |
| 3 | `artefacten/mijn-tuin-materiaal.md` |
| 4 | `artefacten/schets-kaart.md` |
| 5 | `artefacten/boodschappen/boodschappen-2026-04-04.md` |
| 6 | `artefacten/onderhoud/onderhouds-kalender.md` |
| 7 | `artefacten/plannen/mestplan.md` |
| 8 | `artefacten/plannen/zone-11-herinrichting.md` |

## 2. Aangemaakte bestanden in doelstructuur

| # | Doelbestand | Actie |
|---|-------------|-------|
| 1 | `docs/borders-zon-schaduw.md` | ✅ Aangemaakt (kopie van `artefacten/borders-zon-schaduw.md`) |
| 2 | `docs/mijn-tuin-materiaal.md` | ✅ Aangemaakt (kopie van `artefacten/mijn-tuin-materiaal.md`) |
| 3 | `docs/schets-kaart.md` | ✅ Aangemaakt (kopie van `artefacten/schets-kaart.md`) |
| 4 | `docs/plannen/mestplan.md` | ✅ Aangemaakt (kopie van `artefacten/plannen/mestplan.md`) |
| 5 | `docs/plannen/zone-11-herinrichting.md` | ✅ Aangemaakt (kopie van `artefacten/plannen/zone-11-herinrichting.md`) |
| 6 | `docs/onderhoud/onderhouds-kalender.md` | ✅ Aangemaakt (kopie van `artefacten/onderhoud/onderhouds-kalender.md`) |

## 3. Overgeslagen bestanden (al aanwezig en identiek)

| # | Bestand | Reden |
|---|---------|-------|
| 1 | `docs/mijn-planten-borders.md` | Identiek aan `artefacten/mijn-planten-borders.md` — geen actie |
| 2 | `docs/boodschappen/boodschappen-2026-04-04.md` | Identiek aan `artefacten/boodschappen/boodschappen-2026-04-04.md` — geen actie |

## 4. Aangepaste configuratiebestanden

Geen — `genereer-publicatiestructuur` wijzigt geen configuratiebestanden. Voor nav-updates: voer intent `genereer-navigatiebestand` uit.

## 5. Aandachtspunten

⚠️ **Duplicaat mestplan.md**: `docs/mestplan.md` bestaat reeds (voorafgaand aan deze transformatie, handmatig geplaatst). De 1:1-mapping van `artefacten/plannen/mestplan.md` resulteert in `docs/plannen/mestplan.md`. Beide bestanden bevatten dezelfde inhoud maar bevinden zich op verschillende paden. Aanbeveling voor workspace-steward: verwijder `docs/mestplan.md` en pas `mkdocs.yml` nav aan naar `plannen/mestplan.md`.

## 6. Toegepaste structuur_regels

Geen structuur_regels meegeleverd — structuur 1:1 overgenomen vanuit `artefacten/`.

## 7. Resulterende docs/-structuur

```
docs/
├── index.md
├── borders-zon-schaduw.md       ← nieuw
├── mestplan.md                  ← pre-existing (zie aandachtspunt 5)
├── mijn-planten-borders.md
├── mijn-tuin-materiaal.md       ← nieuw
├── schets-kaart.md              ← nieuw
├── schets-kaart-zon-schaduw.svg
├── boodschappen/
│   └── boodschappen-2026-04-04.md
├── onderhoud/
│   └── onderhouds-kalender.md   ← nieuw
└── plannen/
    ├── mestplan.md              ← nieuw (zie aandachtspunt 5)
    └── zone-11-herinrichting.md ← nieuw
```
