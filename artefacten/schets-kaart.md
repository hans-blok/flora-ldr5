# Schets-kaart — Perceel nr. 5

Bron: `schets-kaart.pptx` (PowerPoint schets, automatisch geëxtraheerd)
Canvas-afmeting origineel: **33,87 × 19,05 cm** (liggend)

> **Let op:** Alle shapes in de PPTX zijn geroteerd. De coördinaten (x, y) zijn de linkerbovenhoek van de *bounding box vóór rotatie*. Rotatie is **met de klok mee (CW)** in graden, om het middelpunt van de bounding box.

## Oriëntatie

- **Noord = boven** op canvas (bevestigd via Google Earth screenshot)
- **x-as** loopt van west (links) naar oost (rechts), in cm vanaf linkerbovenhoek
- **y-as** loopt van noord (boven) naar zuid (onder), in cm vanaf linkerbovenhoek
- Alle bebouwing is ~297° CW gedraaid → de lange as van het woonhuis loopt **NNO–ZZW**
- Daardoor wijst de **voorkant (straat) naar het noordwesten (NW)**
- De **achterzijde** (schuur, tuin) wijst naar het **zuidoosten (ZO)**
- De perceelgrenzen lopen ruwweg **NW–ZO** (voor-achter) en **NNO–ZZW** (linker-rechtergrens)

---

## Gebouwen en vaste structuren

| Element               | x (cm) | y (cm) | b (cm) | h (cm) | rot (°CW) | Toelichting                                              |
|-----------------------|--------|--------|--------|--------|-----------|----------------------------------------------------------|
| Woonhuis (NW-deel)    | 10,98  | 8,78   | 2,95   | 3,70   | 297,45    | Eigen woonhuis nr. 5 – NW-vleugel (dicht bij straat)     |
| Woonhuis (ZO-deel)    | 13,17  | 10,16  | 4,67   | 2,35   | 299,26    | Eigen woonhuis nr. 5 – ZO-vleugel (uitbouw achter)       |
| Bijgebouw             | 20,01  | 9,20   | 3,75   | 3,51   | 295,04    | Los bijgebouw aan de O/ZO-kant van het perceel           |
| Schuur                | 19,18  | 15,23  | 1,75   | 4,61   | 299,26    | Schuur aan de ZO-rand van het perceel                    |
| Parkeerplaats (grind) | 12,65  | 5,24   | 2,86   | 3,89   | 296,50    | Eigen oprit aan de NW-zijde (straatkant)                 |
| Parkeerplaats buren   |  6,50  | 3,80   | 2,00   | 2,50   | 297,00    | Parkeerplek buren langs de straat (NW-kant)              |
| Straat                | −1,00  | 2,20   | 18,00  | 2,00   | 297,00    | Straat langs NW-zijde perceel (geschat)                  |
| Sloot                 | −1,00  | 0,30   | 17,00  | 1,50   | 297,00    | Sloot langs straat, aan buitenrand NW (geschat)          |
| Muurtje (NW)          | 16,75  | 6,93   | 4,68   | 0,63   |  26,43    | Lage muur langs NW-kant; scheidt straat-/parkeerzone     |
| Muurtje (ZO)          | 19,93  | 15,04  | 4,13   | 0,60   | 299,26    | Lage muur bij schuur, ZO-rand perceel                    |
| Onbenoemde structuur  | 15,89  | 7,09   | 1,74   | 1,51   | 297,09    | Klein hoekstuk naast NW-muurtje                          |

---

## Aangrenzende percelen (buren)

| Element                  | x (cm) | y (cm) | b (cm) | h (cm) | rot (°CW) | Toelichting                                                    |
|--------------------------|--------|--------|--------|--------|-----------|-----------------------------------------------------------------|
| Buren – grensstrook      | 12,98  | 9,34   | 1,80   | 9,53   | 299,26    | Smal element langs de W/ZW-grens van het perceel               |
| Buren – woning           | 14,17  | 1,83   | 3,64   | 4,53   | 295,04    | Woning buren aan de NW-zijde, aan (of direct naast) de straat  |
| Tuin buren (NW)          |  9,50  | 2,80   | 3,00   | 4,50   | 296,00    | Tuin buren aan de NW-kant (tussen straat en eigen woning) — **handmatig geschat in v2**, grens is indicatief (stroke-rand in SVG) |
| Tuin buren (NO)          | 18,73  | 3,87   | 2,86   | 3,89   | 296,50    | Tuin buren aan de NO-kant van het perceel                      |
| Tuin buren (groot, ZO)   | 20,41  | 12,78  | 8,34   | 2,63   | 296,50    | Grote tuinstrook buren aan de ZO-zijde van het perceel         |

---

## Tuinzones (beplantingszones)

De zones zijn smalle rechthoeken (0,87–1,35 cm breed) die strips of beplantingsrijen markeren.
Meer planten per zone worden bijgehouden in `mijn-planten.md`.

| Zone   | x (cm) | y (cm) | b (cm) | h (cm) | rot (°CW) | Ligging       | Oriëntatie strip                            |
|--------|--------|--------|--------|--------|-----------|---------------|---------------------------------------------|
| Zone 1 | 10,21  | 7,31   | 0,89   | 3,75   |  27,22    | W-zijde       | Parallel aan huisas (NNO–ZZW)               |
| Zone 2 | 12,38  | 7,43   | 0,89   | 2,60   | 118,70    | NW-zijde      | Haaks op huis = parallel aan voorgevel (NW–ZO) |
| Zone 3 | 18,50  | 5,97   | 0,89   | 4,23   | 116,85    | NO-kant       | Haaks op huis = parallel aan voorgevel (NW–ZO) |
| Zone 4 | 20,43  | 11,36  | 0,89   | 3,35   | 116,46    | O-kant        | Haaks op huis = parallel aan voorgevel (NW–ZO) |
| Zone 5  | 20,86  | 13,75  | 0,89   | 2,74   |  28,95    | ZO-kant       | Parallel aan huisas (NNO–ZZW)                   |
| Zone 6  | 17,95  | 13,95  | 0,90   | 1,40   | 120,35    | Z/ZO-kant     | Kleiner; haaks op huis (NW–ZO richting)         |
| Zone 7  | 16,14  | 12,90  | 0,89   | 2,39   | 120,35    | Z-kant        | Haaks op huis = parallel aan voorgevel (NW–ZO)  |
| Zone 8  | 16,47  | 7,90   | 0,87   | 2,14   | 120,35    | Centrum       | Haaks op huis = parallel aan voorgevel (NW–ZO)  |
| Zone 10 |  2,50  | 3,50   | 9,00   | 0,90   | 297,00    | NW-rand       | Strook langs binnenkant straat (NW–ZO richting) |
| Zone 11 |  0,50  | 3,00   | 0,90   | 9,00   |  27,00    | W-grens       | Lange strook langs W/ZW-grens (NNO–ZZW richting)|
| Zone 12 |  1,50  | 1,50   | 10,00  | 0,90   | 297,00    | Langs sloot   | Strook langs sloot/straatrand buiten perceel    |

> **Let op:** Zone 9 ontbreekt — de nummering loopt van zone 8 direct door naar zone 10. Zone 9 is niet aangemaakt in de brondata (PPTX).

---

## Ruimtelijke beschrijving (voor LLM)

### NW–ZO as (voorkant → achterkant)
Van noordwest (straat) naar zuidoost (achtertuin):
1. **Sloot** (NW, buiten perceel) – watergang langs straatrand
2. **Zone 12** – beplantingsstrook langs sloot
3. **Straat** (NW, buiten/grens perceel) – rijweg langs NW-kant
4. **Zone 10** – beplantingsstrook langs binnenkant straat
5. **Parkeerplaats buren** + **Tuin buren (NW)** – aangrenzend aan straat
6. **Buren-woning** – directe buren aan de straatzijde
7. **Parkeerplaats eigen** (grind) – oprit nr. 5 tussen straat en voordeur
8. **Muurtje NW** – scheiding parkeer-/straat­zone en tuin
9. **Woonhuis nr. 5** (centrum) – NW-vleugel bij straat, ZO-vleugel uitbouw
10. **Bijgebouw** (O/ZO-kant) – achter het woonhuis
11. **Tuinzones 4, 5, 6, 7** (ZO-kant) – beplanting achtererf
12. **Schuur + muurtje ZO** – ZO-rand perceel

### W/ZW–O/NO as (linkergrens → rechtergrens)
Van west/zuidwest naar oost/noordoost:
- **Grensstrook "Buren"** (W/ZW-kant, x≈13) — perceelgrens met buren links
- **Zone 1** (W-kant, x≈10,2) — beplantingsrand langs W-grens
- **Woonhuis** (centrum, x≈10,9–17,8)
- **Zone 3, bijgebouw, zone 4/5** (O-kant, x≈18,5–21,8)
- **Tuin buren (NO en groot ZO)** — aangrenzende buurpercelen O/NO kant

### Begrenzingen
| Zijde | Grenselement (van buiten naar binnen)                                                              |
|-------|----------------------------------------------------------------------------------------------------|
| NW    | Sloot → zone 12 → straat → zone 10 → parkeerplaats buren + tuin buren (NW) → woning buren straat  |
| ZO    | Tuin buren (groot, ZO) → muurtje ZO → schuur                                                      |
| W/ZW  | Zone 11 → grensstrook "Buren" → zone 1                                                             |
| NO/O  | Tuin buren (NO) → bijgebouw                                                                        |

---

## Visuele representatie

Zie: `artefacten/schets-kaart.SVG` — SVG op schaal (~37,8 px/cm; 1280 px ÷ 33,87 cm), Noord = boven, **met correcte CW-rotaties** uit PPTX.

De SVG geeft de PPTX correct weer. De coördinaten in deze markdown corresponderen 1:1 met de SVG-shapes.

---

## Brondata
- **Bestand**: `schets-kaart.pptx` (1 slide, liggend 33,87×19,05 cm) + handmatige toevoegingen o.b.v. schets v2
- **Extraheer-methode**: Python `zipfile` + `xml.etree.ElementTree` (EMU ÷ 914400 × 2,54 = cm; rot ÷ 60000 = graden CW)
- **Achtergrondafbeelding in PPTX**: kompasroos (x=6,19 y=0,5 cm, 3,10×2,83 cm)
- **Rotatie-patroon**: bebouwing ~295–299° CW (perceel staat ~26–30° scheef t.o.v. Noord); zones ~27° of ~117–120°
- **Versie 2 toevoegingen**: sloot, straat, zone 10, zone 11, zone 12, tuin buren (NW), parkeerplaats buren, zone 6 verkleind
