# Hanoi house: planning and design roadmap

Created: 2026-09-30  
Updated: 2026-10-02  
Status: C03a owner-feedback comparison available; neither balcony/layout selected. Surveyed geometry, near-boundary permissions and engineering remain pending.  
Purpose: Guide an editable, AI-assisted process from land investigation to construction and handover.

Current review package: [interactive viewer](outputs/house-concepts.html), [C03 design comparison](docs/concept-study-C03.md), [C03a handoff correction](docs/concept-study-C03a.md), and [geometry review](outputs/geometry-review.md). Road arrival is confirmed; shared versus bedroom balcony access is compared. The approximate footprint target is flexible; C03a retains a proposed 120.96 m² F1 footprint. The following roadmap is a phase guide; current owner requirements live in docs/brief.md. Model area is not registered area.

## 1. Recommended approach

Develop the house as a coordinated project: architecture, structure, building services, interiors, cost, and construction constraints evolve together. Start with the land and household needs. Compare a few feasible layouts before investing in detailed finishes or photorealistic rendering.

For early design, use **structured building data → SVG drawings in HTML + simple Three.js 3D**. Use **Python scripts for traceable engineering calculations**, with a Vietnamese structural engineer defining and reviewing the engineering basis. Move to the architect's CAD/BIM workflow when detailed documentation requires it; use Blender for higher quality visualization.

Keep editable sources, decisions, assumptions, generated drawings, and issued documents together in this workspace. Each issued package must state its revision and purpose: concept, coordination, permit, tender, or construction.

This plan proposes a workflow and technology direction. It does not establish site dimensions, permissible development, structural member sizes, a foundation solution, or a construction budget. Those remain open until the relevant evidence is available.

## 2. Starting brief and missing information

Confirmed: the owner has land near Noi Bai Airport, Hanoi, Vietnam, and plans two floors with five bedrooms. The project values easy editing, reproducible calculations, staged visualization, feng shui considerations, and an improving AI workflow.

The current detailed requirements are in [the owner brief](docs/brief.md), [site investigation notes](docs/site-investigation.md), and [preferences and feng shui register](docs/preferences-and-feng-shui.md). These records distinguish owner requirements from provisional interpretations. The original plot reference is [plot_dimensions.jpg](plot_dimensions.jpg).

Altar clarification: use indoor space beyond the solid backing wall as the baseline. The family is open to an outdoor gap/courtyard if suitable under its feng shui interpretation; preliminary research supports the solid-backing principle but does not settle the courtyard question. Keep courtyard layouts as unresolved alternatives. The owner confirms 130° along A toward the road beside D for concept orientation; survey and compass convention remain unverified.

Budget policy for initial exploration: a monetary ceiling may be deferred while preparing the first layouts. Track floor area and major cost drivers from the start; establish a rough budget range before committing to a preferred concept or detailed engineering.

Latest household/site clarification: prefer the house near the A–B junction; A and C border neighboring walls/houses and B borders a neighbor's garden. Provide parking for one car and a few scooters/bicycles, prefer a garden/front yard, and seat approximately six at dining. Laundry/drying and special accessibility planning are low priorities at this stage. Above the altar, F2 may have a floor but the corresponding zone must remain empty, without tables/chairs or frequent circulation. Owner confirmed approximately 100 m² footprint with outdoor space retained, implying about 200 m² gross across two full floors; actual areas and fit remain to be developed. Full plot coverage is not intended.

| Input | What to obtain | Why it affects the design |
| --- | --- | --- |
| Site identity | Exact address and current ward/commune; land-use documents | Applicable planning conditions and authority |
| Survey | Boundary coordinates, dimensions, levels, road level, north, existing features | Reliable buildable envelope and geometry |
| Neighbors | Buildings, foundations if known, party walls, windows, access, existing condition photos | Excavation, privacy, daylight, construction method |
| Household | Residents now and later, ages, mobility, guests, working from home | Room program and accessibility |
| Uses | Family-only use, rental/business use, parking, storage, worship, outdoor space | Layout, services, fire strategy, approvals |
| Scale | Desired floors, rooms, roof use, basement, future expansion | Feasibility, structure, cost |
| Budget | Total ceiling in VND; inclusions; contingency; funding milestones | Option selection and procurement |
| Timing | Desired start/move-in and any fixed dates | Investigation, design and procurement schedule |
| Preferences | Reference images, materials, maintenance tolerance, comfort priorities | Exterior/interior direction |
| Feng shui | Specific rules, method/adviser, hard requirements versus preferences | Explicit criteria for comparing options |

Record unknowns as unknowns. An approximate sketch may support exploration, but every inferred dimension must be marked provisional and replaced by surveyed information before detailed design.

## 3. Phases, deliverables, and decision gates

The gates below are project decisions, not claims about statutory approval stages. Some work overlaps; major changes reopen affected gates.

| Phase | Work and deliverables | Completion decision |
| --- | --- | --- |
| 0 — Brief and team | Owner brief, room/area schedule, budget status, responsibilities, questions and evidence register | Owner confirms priorities; a monetary target may remain deferred during initial exploration |
| 1 — Site and feasibility | Survey; planning/permit investigation; utilities; neighboring conditions; engineer-defined ground investigation; buildable envelope | Architect confirms the feasible envelope and outstanding constraints |
| 2 — Concept options | Two or three floor-plan options, sections, simple massing, preliminary structural grids, service shafts, furniture, cost comparison | Owner selects a coordinated direction with architect/engineer input |
| 3 — Coordinated schematic design | Refined plans/elevations/sections; structural system; foundation basis; service routes; exterior/interior direction; updated estimate | Team agrees geometry and systems are sufficiently resolved for detailed work |
| 4 — Detailed design and permit coordination | Calculations, dimensions, schedules, reinforcement and connection details, electrical/plumbing/HVAC drawings, waterproofing, material specifications, required permit documents | Discipline reviewers resolve issues and owner accepts cost/scope; applicable approvals obtained before relevant work |
| 5 — Tender and procurement | Consistent pricing package, quantities, comparable quotations, exclusions, contract scope, payment milestones, long-lead schedule | Owner selects contractor against a reconciled scope and budget |
| 6 — Construction | Issued drawings, inspections, site questions, approved changes, material checks, progress/cost records | Work accepted at defined inspection stages before concealment or continuation |
| 7 — Commissioning and handover | Services testing, defects list, as-built drawings, warranties, equipment manuals, maintenance plan | Owner accepts completed work and documented outstanding items |

### Phase 1: investigate before choosing the house shape

- Ask a local architect to establish land-use compatibility, boundaries, building lines/setbacks, height/floor limits, allowable coverage, projections, and any local restrictions. Record the source and date for each constraint.
- Confirm the current permit route and submission requirements for the actual location and proposed use. Do not infer permit exemption from the description “private house.” A 2026 Hanoi source illustrates commune-level handling, but it does not establish the route for this plot: [Xuân Mai permit guidance](https://xuanmai.hanoi.gov.vn/kinh-te-tai-chinh/xuan-mai-trien-khai-thuc-hien-cap-giay-phep-xay-dung-nha-o-rieng-le-2785260313163347473.htm).
- Commission a measured site/level survey. Establish one elevation datum and distinguish surveyed north from a casual compass reading.
- Have the structural/geotechnical team specify an appropriate ground investigation. Obtain groundwater and soil information needed for foundation and excavation decisions; do not assume shallow footings or piles in advance.
- Investigate drainage connection levels, water pressure, electrical supply capacity, communications, construction access, storage, lifting, and waste removal.
- Assess site-specific flooding history, heat/sun exposure, rain penetration, humidity, noise, air quality, and ventilation opportunities. Document neighboring buildings rather than assuming unobstructed light or air.

### Phases 2–3: design the whole house together

Each option should include furniture and circulation, staircase geometry/headroom, usable room dimensions, daylight/privacy, wet-room stacking, shafts, outdoor/service areas, and an indicative structural grid. Include at least one section through stairs and bathrooms; floor plans alone can hide vertical conflicts.

Compare options against owner-agreed criteria: everyday usability, area efficiency, accessibility, daylight/comfort, feng shui preferences, structural simplicity, service access, cost, and future flexibility. Hard constraints are pass/fail; weighted preference scores must not compensate for a failed hard constraint.

Start interiors now at the level of furniture, storage, kitchen/bathroom arrangements, appliances and lighting needs. Start exterior design with massing, openings, shade, roof/drainage, and material durability. Detailed textures and decorative finishes can follow after coordinated geometry is stable.

Specific topics to resolve:

- Continuous gravity and lateral load paths; column positions across floors; spans, cantilevers, openings and roof equipment loads.
- Stair and escape strategy, smoke/fire considerations for the actual occupancy, and any parking or charging provisions.
- Water storage and pumps, hot water strategy, drain falls/vents/cleanouts, roof and balcony outlets/overflows, and connection levels.
- Electrical load schedule, distribution boards, circuits/protection/earthing, outlet locations, data/Wi-Fi, optional solar/EV readiness.
- Cooling/ventilation, outdoor unit locations, condensate drainage, kitchen/bathroom exhaust, noise and maintenance access.
- Roof/bathroom/balcony waterproofing interfaces, facade junctions, shading, glazing, moisture management, and service penetrations.
- Future additions or a lift only if intentionally included in the brief and engineering basis; “future-ready” is not an uncalculated promise.

## 4. Editable design technology

### 4.1 Is HTML good enough for floor plans and structural layouts?

**Yes, HTML containing SVG is a good early design and review interface.** SVG supplies vector geometry, labels, dimensions, layers and selectable elements. HTML supplies navigation, option comparison, notes and controls. CSS boxes alone are an awkward representation of dimensioned building geometry.

Store actual dimensions and relationships separately from the page. Generate floor plans, column/beam overlays, service layouts and 3D from the same underlying building data. Editing a window or column should update all affected views.

| Purpose | Proposed format/tool | Boundary |
| --- | --- | --- |
| Brief, decisions, investigations | Markdown | Human-readable durable project memory |
| Early authoritative geometry | JSON with a versioned schema | Easy validation and controlled AI editing |
| Calculation assumptions/configuration | YAML or JSON with explicit units and sources | No undocumented numerical defaults |
| Room, equipment, quantity schedules | CSV or generated tables | Maintain element IDs linking back to the model |
| 2D review | SVG inside HTML, generated with TypeScript | Dimensions use model coordinates, not screen pixels |
| Shared/static drawings | SVG and dimensioned PDF sheets | State scale/page size and verify printing at 100% |
| Early 3D | Three.js massing generated from the model | Spatial review; not an engineering solver |
| Visual exchange | glTF/GLB | Carries visualization; does not replace engineering/BIM semantics |
| Detailed building documentation | Architect's agreed CAD/BIM tool; IFC exchange where supported | Choose with the actual design team before detailed development |
| Final visualization | Blender scene with reusable materials/cameras | Keep design geometry synchronized through documented imports |
| Engineering calculations | Python modules and generated reports | Engineer-approved methods and independent checks |

The Three.js documentation supports a simple scene workflow and glTF loading: [scene basics](https://threejs.org/manual/pages/creating-a-scene.html), [loading models](https://threejs.org/manual/pages/loading-3d-models.html). This stack is a project recommendation, not a requirement to build a custom CAD application.

### 4.2 Data conventions to settle before drawing automation

- Use millimetres for early building geometry; explicitly convert to the chosen engineering units at calculation boundaries.
- Define model origin, horizontal axes, positive Z upward, level elevations, north rotation, survey transformation and elevation datum.
- Give stable IDs to levels, spaces, walls, openings, columns, beams, slabs, shafts and fixtures. Human labels can change without changing IDs.
- Specify whether wall coordinates describe centerlines or faces, and distinguish structural dimensions from finished clear dimensions.
- Keep proposed structural elements tagged `preliminary`; geometry alone never implies structural adequacy.
- Attach evidence, assumption status and revision references to consequential inputs. Derived areas/volumes should be calculated rather than separately typed.
- Keep alternatives separate, with a named selected revision. Never silently combine parts of different options.

The building geometry and structural analysis model are related but distinct. The engineer defines member idealization, supports, offsets, diaphragm behavior and loads. A visual wall mesh must not automatically become a load-bearing analytical member.

### 4.3 Start small; migrate deliberately

First implement one representative floor, a dimensioned SVG, a structural overlay, and a simple extruded 3D view. Validate the edit-to-drawing loop before adding an interactive editor, automatic optimization or many libraries. A small TypeScript viewer/build script is sufficient initially; a large application framework is optional.

When the architect needs detailed BIM authoring, evaluate their existing workflow first. An open-source candidate is Blender with Bonsai, which provides IFC authoring: [Bonsai documentation](https://docs.bonsaibim.org/). Prove one sample exchange for dimensions, levels, openings and IDs before adopting it. IFC interoperability does not guarantee a lossless round trip between tools.

Declare which source becomes authoritative after migration. If IFC/native BIM takes over, generate downstream review data from it or a controlled export; avoid maintaining independently editable JSON and BIM versions of the same geometry.

For polished renderings, use Blender's EEVEE for fast previews and Cycles for final images as appropriate: [Blender rendering](https://www.blender.org/features/rendering/). Higher realism is usually an asset/material/lighting workflow decision, not a reason to replace the browser viewer. AI-generated mood images can help explore style, but measured geometry remains the reference for what is buildable.

## 5. Reproducible structural engineering

Scripts improve repeatability, traceability and revision comparison. Deterministic output can still be wrong if the model, units, loads, soil assumptions or code interpretation are wrong. The responsible Vietnamese structural engineer should establish the design basis, select/check the analysis method, and review issued calculations and details.

### Calculation workflow

1. **Establish the basis:** site, building use, design life, structural system, materials, exposure, geotechnical report, selected standards/editions, and performance criteria.
2. **Define inputs:** geometry revision, load cases, finishes/partitions, occupancy loads, roof/water tank/equipment loads, wind/seismic parameters, soil data and construction-stage assumptions as applicable.
3. **Generate combinations:** explicitly implement applicable ultimate and serviceability combinations; preserve the source clause, factors and combination IDs.
4. **Analyze:** use a suitable established solver selected by the engineer. Start custom scripting with transparent load take-downs, simple members and report generation. A custom whole-building finite-element solver is unnecessary for the initial workflow.
5. **Check:** relevant strength, stability, deflection, drift, cracking, punching, foundation capacity/settlement, detailing and constructability. The engineer determines the complete applicable set.
6. **Validate:** unit/dimension checks; published or independently worked benchmarks; equilibrium/reaction checks; independent comparison for critical results; sensitivity to uncertain inputs. Establish these checks before relying on a calculator.
7. **Issue:** human-readable report with inputs, equations, clause references, intermediate results, governing cases, margins, unresolved issues and reviewer status. Unknown critical inputs must produce an incomplete result, not a pass.

Use Python modules as the calculation source; notebooks may explain investigations but should call those modules. Pin dependencies and record interpreter/solver versions. Every run should record input files/hash, model revision, script revision, assumptions, units, timestamp and solver settings. Define tolerances where solver floating-point behavior precludes identical bytes.

Do not release column/beam/foundation sizes or reinforcement as construction instructions until the engineer has completed the applicable analysis and detailing. Basement excavation, neighboring foundations and temporary works require explicit consideration where relevant.

### Vietnam standards register

Maintain a register with: designation, title, edition/amendments, official source, access date, applicable scope, cited clauses, adoption reason, engineer confirmation, and review trigger. Distinguish mandatory technical regulations (QCVN) from standards (TCVN); the team must confirm which requirements apply through law, referenced regulations and the adopted design basis.

The following is a **research starting point checked on 2026-09-30**, not a complete or approved code list. Catalog listings identify documents; full authorized texts and current legal applicability must be checked before use. Do not calculate from search snippets or draft documents.

| Topic | Starting reference | Research status and next action |
| --- | --- | --- |
| Loads and combinations | [TCVN 2737:2023 — VSQI](https://tieuchuan.vsqi.gov.vn/tieuchuan/view?sohieu=TCVN+2737%3A2023) | Catalog identifies replacement of the 1995 edition and a related change to an appendix of TCVN 5574:2018; coordinate adopted provisions |
| Reinforced concrete | [TCVN 5574:2018 — VSQI](https://tieuchuan.vsqi.gov.vn/tieuchuan/view?sohieu=TCVN+5574%3A2018) | Catalog lists active status; engineer confirms current applicability and associated amendments |
| Pile foundations, if selected | [TCVN 10304 search — VSQI](https://tieuchuan.vsqi.gov.vn/tim-kiem?si=TCVN+10304) | Catalog lists TCVN 10304:2025; obtain the text and confirm replacement/transition details before adopting an edition |
| Natural conditions data | [QCVN 02:2022/BXD — official legal record](https://vbpl.vn/TW/Pages/ivbpq-thuoctinh.aspx?ItemID=156199&Keyword=) | Starting source for relevant site-dependent data; establish exact location and current amendments |
| Fire safety applicability | [QCVN 06:2022/BXD amendment 1:2023 — Ministry of Construction](https://xaydung.gov.vn/Images/editor/files/Quy%20Chu%E1%BA%A9n/QCVN%2006-2022.pdf) | Amendment text located; obtain base text and verify current scope, revisions and house-specific requirements |
| Seismic, shallow foundations, other structural materials | Engineer to identify current standards and parts | Editions not established in this initial research; no seismic exemption assumed |
| Planning, private-house requirements, electricity, water/drainage, ventilation, energy and construction acceptance | Architect/MEP team to identify applicable QCVN, TCVN and utility/local requirements | Register incomplete until location, occupancy, size and systems are defined |

Recheck the register at design-basis approval and before permit/construction issue. When a rule changes, document whether it affects this project and which calculations/drawings need revision.

## 6. Preferences and feng shui

Maintain a preference register rather than scattering requirements through chat. For each item record: ID, description, origin/adviser, method, priority, measurable interpretation, affected spaces, status, and any accepted compromise.

Separate four kinds of criteria:

- **Mandatory constraints:** confirmed planning, safety and engineering requirements.
- **Owner essentials:** room uses, privacy, worship space, accessibility, budget ceiling.
- **Preferences:** style, views, materials, indoor/outdoor relationships.
- **Feng shui requirements:** explicit traditions or rules the household chooses to follow.

Investigate the chosen feng shui method before encoding rules; different schools/advisers may interpret direction and placement differently. Record how facing direction is measured, including whether the convention uses magnetic or true north. Collect personal birth information only if the owner chooses a method that requires it, and keep it out of shared/public materials.

Potential topics to discuss include entrance orientation, altar location, kitchen/stove direction, bed placement, stair position, toilet relationships and room proportions. These are discussion prompts, not assumed requirements. Distinguish cultural preferences from measurable daylight, airflow or safety claims; do not present a traditional rule as a scientifically established health or financial effect.

For a conflict, show the affected plan, explain alternatives and costs, and record the decision. An owner preference cannot waive an applicable safety/legal constraint; find another layout. Introduce important rules before concept selection to avoid expensive late rearrangement.

## 7. AI collaboration and project memory

Use a repeatable loop: **read the brief and current revision → propose a bounded change → edit source data → regenerate affected views/calculations → inspect differences → record the decision**.

Start with a concise project `AGENTS.md` when implementation begins. Suggested rules:

- Read the brief, adopted design basis, latest decisions and open issues before proposing changes.
- Label verified facts, owner decisions, assumptions, estimates and unknowns distinctly.
- Never invent site measurements, standard clauses, material properties, soil data or approvals.
- Preserve element IDs and unit conventions; edit authoritative sources and regenerate derivatives.
- State what changed and which disciplines/documents are affected; flag stale calculations.
- Keep concept/coordination output visibly distinct from reviewed construction issues.
- Require named human review appropriate to the discipline before an issue status changes.
- Keep private land documents and household information in controlled storage; use redacted copies for broader sharing.
- Record consequential outcomes in files so later sessions do not depend on chat history.

Add focused skills only after a useful workflow repeats: survey ingestion, option generation, drawing checks, standards research, calculation reporting, coordination review, rendering and issue-package preparation. Each skill should specify inputs, steps, outputs, checks, limitations and reviewer responsibility. Review proposed rules with the project team before treating them as adopted practice.

Future automation can detect geometry overlaps, duplicate IDs, missing dimensions, inconsistent elevations, stair/headroom issues, service/structure clashes and unexpected area/cost changes. Encode dimensional limits only after the relevant source and applicability are confirmed. An automated warning or clean report supports professional review; it does not replace it.

## 8. Proposed repository and revision strategy

The roadmap and initial brief/site/preference records are now created. Add the remaining directories as their work begins:

```text
HOUSE_BUILDING_PLAN.md
AGENTS.md                         # Adopted AI/project conventions
docs/
  brief.md
  site-investigation.md
  preferences-and-feng-shui.md
  design-basis.md
  standards-register.md
  decisions.md
  open-issues.md
data/
  site.json
  options/                        # Independent concept alternatives
  building.json                   # Selected early geometry
  schemas/
  materials.yaml
  loads.yaml
  room-schedule.csv
src/                              # SVG/HTML and 3D generation
engineering/
  calculations/
  benchmarks/
  reports/
models/                           # Agreed BIM/rendering sources
references/                       # Source index and permitted copies
outputs/                          # Regenerable previews
issued/                           # Immutable, dated review/issue packages
cost/                             # Quantities, estimates, quotations, changes
construction/                     # Site questions, inspections, as-built record
```

Use Git for text/code history and named revision tags when initialized. Keep large binaries in an appropriate versioned file store or Git LFS if needed; do not assume Git alone is a backup. Maintain a separate backup of sources and issued packages.

An issue package should include a manifest: revision, purpose, included files, geometry/calculation versions, author/reviewer, date, unresolved issues and superseded package. Freeze issued files and create a new issue for changes.

When moving a column, wall, stair, shaft or opening, assess effects on adjacent floors, loads, room dimensions, services, quantities and approvals. Changing a render must never silently change the approved geometry.

## 9. Cost, procurement and construction follow-through

Define an all-in budget that explicitly addresses design/engineering, surveys and ground investigation, approvals/fees, site preparation, temporary works, foundations, frame, envelope, services, finishes, built-ins, appliances/furniture, external works, taxes and contingency. Obtain local quotations; do not infer a reliable price from floor area alone.

At each design gate update quantities, unit-rate sources, allowances, exclusions and estimate uncertainty. Record the cost consequence before accepting a scope change. Owner and adviser should choose contingency based on unresolved ground/site/design risks rather than silently applying a universal percentage.

Before tender, reconcile architectural, structural and service drawings. Confirm who supplies fixtures/equipment, what substitutions require review, and what inspections/payment evidence the contract requires.

During construction, agree inspection points for foundations/reinforcement before concrete, embedded services before concealment, waterproofing, and equipment commissioning. Qualified parties should define and perform applicable concrete/material checks, electrical tests, plumbing pressure/leak tests, drainage checks and waterproofing tests. Keep reports and photos linked to locations and drawing revisions.

At handover retain as-built service routes, board/circuit schedules, shutoff locations, equipment manuals, warranties and a maintenance calendar. Update the digital model to reflect accepted site changes.

## 10. First working milestone

Target: a **credible brief, site constraints sheet, and comparison of two or three coordinated concept layouts**. Do not set a construction start date from this roadmap alone; survey, local approvals, ground conditions and team availability govern the schedule.

1. Use the supplied plot sketch, confirmed approximate lengths A/B/C/D = 15/16/13/18 m (D includes both bent segments), and owner-confirmed 130° along A toward D's road; ignore the 192 annotation. Refine the two-floor/five-bedroom program and remaining spatial requirements. Budget range may follow the first layout exploration.
2. Create the brief and open-issues register, separating evidence from assumptions.
3. Engage a local architect and structural engineer early; agree deliverables, editable file ownership, tools, review responsibilities and fee scope.
4. Arrange survey and engineer-directed ground investigation; confirm planning/permit conditions and utility constraints.
5. Build the smallest useful model/viewer once enough geometry is known; keep provisional information visible.
6. Produce concept alternatives with plans, a key section, structural/service overlays, simple 3D and an indicative cost comparison.
7. Review with the owner and design team; record the preferred option and unresolved questions before detailed development.

Ready for initial concept studies using the confirmed approximately 100 m² footprint target and retained outdoor space. Later refinements: exact address and surveyed geometry; boundary offsets/openings; exact altar/buffer-zone extents; parking maneuver/gate arrangement; storage; budget range before concept commitment; additional feng shui method/rules; and professional team. Parking capacity, six-person dining, neighbor types and the empty F2 zone above the altar are recorded. Laundry/drying and special accessibility planning need no further briefing now. Approximate boundary lengths/units and D's total length are confirmed; 192 is excluded from geometric inputs.
