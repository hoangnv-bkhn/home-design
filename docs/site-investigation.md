# Site evidence and open geometry — Noi Bai

Updated: 2026-10-01.

## Evidence

Owner identifies the plot as the central parcel enclosed by sides A, B, C and D in [plot_dimensions.jpg](../plot_dimensions.jpg). The local file was successfully opened and inspected despite the attachment error reported in the chat.

The photograph shows a roughly four-sided parcel with a bend along D. A, B and C label the other sides; they are side labels, not vertex names. The plot must not be treated as a mathematical square. A road runs alongside D and is reported by the owner to be approximately 3–4 m wide. The sketch also shows a nearby road junction; access rights along any additional edge are not established.

| Item | Evidence/status |
| --- | --- |
| Location | Owner: Noi Bai, Hanoi, near airport; exact parcel address unknown |
| A | Owner confirmed approximately 15 m side length |
| B | Owner confirmed approximately 16 m side length |
| C | Owner confirmed approximately 13 m side length |
| D | Owner confirmed approximately 18 m total length along both bent segments, not the end-to-end distance |
| D bend | Visible in photograph; owner authorizes a sketch-based assumption; segment lengths and bend position/angle are unmeasured |
| Road | Owner: approximately 3–4 m wide next to D; surveyed width, legal boundary and access geometry pending |
| Direction | Owner confirms 130° SE as the direction along A toward the road beside D (from the A/B junction toward the A/D junction). Adopt for concept orientation; measurement method and magnetic/true north remain unspecified |
| Central annotation | Appears to read “182” over “192”; owner explicitly says to ignore 192. Neither annotation is a geometric input; no area inferred |
| Nearby annotations | “168” and “169” visible; meanings not established |
| Beyond A | Owner: neighbor's wall/house |
| Beyond B | Owner: neighbor's garden |
| Beyond C | Owner: neighbor's wall/house |
| Preferred house position | Owner: near A–B junction; does not establish permission or intent to build directly on either boundary |

Site-planning brief: one car plus a few scooters/bicycles, with a garden/front yard preferred. Owner confirmed approximately 100 m² building footprint near A–B, leaving outdoor space. The house is not intended to occupy the entire plot. Remaining outdoor area cannot be quantified reliably until a provisional geometric model or survey establishes plot area; 192 remains excluded.

For concept studies, account for the neighboring walls/houses at A and C. The garden beyond B is the currently reported condition, not a guarantee of permanent openness or a right to place boundary windows. Exact offsets, openings and neighboring building heights remain to be established.

## Geometry rules for the next step

Lengths use metres (m); area uses square metres (m²). The owner confirmed the boundary units and D's total length on 2026-10-01. Four approximate edge lengths, especially with one bent side, do not uniquely define the parcel. The owner authorizes an approximate bend for concept work; no registered area is being imposed.

Use the photograph for topology and a provisional bend only. It is a photographed drawing with perspective distortion and unknown original scale; pixel proportions cannot establish exact angles, area or setbacks. Do not silently distort dimensions to make an assumed area fit.

Concept C01 now provides a provisional polygon in [the data source](../data/concepts.json), derived by [the build script](../scripts/build_concepts.py). It assumes perpendicular A/B, a 1.8 m drop along C and two 9 m segments for D. Its computed area is approximately 243.78 m², for this model only. See [the geometry review](../outputs/geometry-review.md) for coordinates and assumptions. No surveyed boundary or registered area has been adopted.

Use the owner-confirmed 130° bearing along A toward D for concept orientation. It is not the bearing along D or necessarily the perpendicular facing direction of a future facade. D has two segments; the eventual house facade and gate need not align with either. Measurement method and magnetic/true north are still unverified, so retain this as owner-provided concept data until survey. Do not derive bearings from the camera framing.

## Location-specific investigations

- Obtain parcel location, current planning conditions and a level/boundary survey before fixing the buildable envelope.
- Ask the local design team to check whether airport-related planning or height controls apply at the exact location, including rooftop equipment and construction lifting. No restriction or exemption is established here simply from airport proximity.
- Observe or measure aircraft and road noise at different times, especially where bedrooms might sit. Aircraft noise is an identified environmental concern: [WHO noise guidance](https://www.who.int/tools/compendium-on-health-and-environment/environmental-noise/) and [ICAO aircraft noise](https://www.icao.int/environmental-protection/aircraft-noise). These sources do not establish exposure at this parcel or a Vietnamese compliance limit.
- Project inference: if site noise is significant, compare roof/wall/window acoustic performance together with a ventilation strategy that remains usable when windows are closed. Do not specify glazing solely by pane count or assume the opposite side of the house eliminates overhead aircraft noise.
- Verify road access for deliveries, emergency access, turning, construction storage and any parking maneuver. An approximate road width is not a complete access assessment.
- Record neighbors/open sides, drainage and flood history, utility points, ground conditions and road/site levels.

## Questions to resolve

1. For later survey/directional refinement: how was the confirmed 130° bearing measured, and is it magnetic or true north? This does not block initial concept studies.
2. Later site detailing: what are the heights/offsets of the reported walls/houses at A and C, and the boundary treatment at B's garden? Any access/opening rights remain unverified.
3. Where should the gate/vehicle access be, and is any road widening or building line known?

Boundary units and the meaning of the 130° orientation are resolved; 192 is excluded. Room relationships and a visibly provisional boundary study can progress using the confirmed approximate lengths, owner-provided bearing and an assumed bend. Survey verification remains outstanding.
