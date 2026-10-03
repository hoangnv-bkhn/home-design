# Site evidence and open geometry — Noi Bai

Updated: 2026-10-03.

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
| Preferred house position | Owner now wants rear beside B and about 0.30 m at A. C03 models a 0.10 m B allowance; exact B distance, boundary-wall construction and permissions remain unverified |

Site-planning brief: one car plus a few scooters/bicycles, with a garden/front yard preferred. Owner confirmed approximately 100 m² footprint near A–B, later allowing departures from exactly 100 m² / 10 × 10 m and exploration of upper cantilevers. Latest feedback prefers horizontal B extent longer than vertical A extent. C05 proposes 122.88 m² F1; acceptance remains pending. The house is not intended to occupy the entire plot. Remaining outdoor area is model-derived until survey; 192 remains excluded.

For concept studies, account for the neighboring walls/houses at A and C. The garden beyond B is the currently reported condition, not a guarantee of permanent openness or a right to place boundary windows. Exact offsets, openings and neighboring building heights remain to be established.

## Geometry rules for the next step

Lengths use metres (m); area uses square metres (m²). The owner confirmed the boundary units and D's total length on 2026-10-01. Four approximate edge lengths, especially with one bent side, do not uniquely define the parcel. The owner authorizes an approximate bend for concept work; no registered area is being imposed.

Use the photograph for topology and a provisional bend only. It is a photographed drawing with perspective distortion and unknown original scale; pixel proportions cannot establish exact angles, area or setbacks. Do not silently distort dimensions to make an assumed area fit.

The concept model provides a provisional polygon in [the data source](../data/concepts.json), derived by [the build script](../scripts/build_concepts.py). It assumes perpendicular A/B, a 1.8 m drop along C and two 9 m segments for D. Its computed area is approximately 243.78 m², for this model only. See [the geometry review](../outputs/geometry-review.md) for coordinates and assumptions. No surveyed boundary or registered area has been adopted.

C05 retains that polygon and F1/F2 origin **(0.10, 0.30)** in local site axes. Approximately 0.30 m at A is the owner's desired layout; 0.10 m at B is the assistant's provisional allowance for “right next to B.” Neither fixes a surveyed envelope, legal setback, construction access or drainage/eaves rights.

C02's rear/B 0.8 m projection and garden door remain superseded; the upper envelope projects **0.8 m toward C**, within the modeled parcel. Shared and bedroom corner balconies project toward D. No A/B boundary doors or windows are assumed. C05 places kitchen/dining on C with a direct door/window to owned side yard below the upper layer. Upper rear bedroom rooflight, kitchen extract and actual shafts remain unresolved; near-boundary room performance is not established.

C05 changes F1 to **9.6 m along A × 12.8 m along B**. Model land outside F1 becomes about **120.90 m²**, versus C03's 122.82 m²; it includes boundary gaps, access and parking. Front depth along A grows from 3.70 to **5.30 m**, but varies across bent D and is not a uniform yard depth. Side-yard width reduces by 2.0 m versus C03; upper C projection reduces it a further 0.8 m locally. Garden planting moves into the remaining side strip. Front/A parking is a 2.8 × 5.0 m stationary bay, with distinct porch/step rectangles separated laterally by 1.15 m. Three two-wheel reservations remain. Ground containment/overlaps pass; turning, site levels, upper supports and clear heights remain unverified.

Plot/F1/F2 retain the 90° clockwise presentation. This puts B above, A right and C left on the display. Named A/B edges take precedence over casual left/right wording; no boundary side or bearing was relabeled.

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
