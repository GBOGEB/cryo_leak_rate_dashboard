# VISUAL_CATALOG

## Existing Visuals (Created in v2.1.0)
- [x] Chart 1: Basic leak rate vs mass loss
- [x] Chart 2: Temperature effects
- [x] Chart 3: Cost waterfall
- [x] Chart 4: Monte Carlo distribution
- [x] Chart 5: Risk heatmap
- [x] Chart 6: Sankey diagram
- [x] Chart 7: Supplier comparison (basic)
- [x] Chart 8: Maintenance Gantt
- [x] Chart 9: Reliability distributions

## Reproducible (Can Regenerate)
- All existing charts via `python src/build_v2.py`

## TODO (Planned Enhancements)
- [ ] Overlay plots with isolines (Charts 1-3 above)
- [ ] Secondary axis plots (Charts 4-5)
- [ ] Material-specific comparisons (Charts 6-9)
- [ ] Operating condition matrices (Charts 10-13)
- [ ] Enhanced cost analysis (Charts 14-18)

## Value-Add Recommendations
1. **Interactive Valve Selector**: User picks valve type/size → see all impacts
2. **Scenario Builder**: User defines operating conditions → get recommendation
3. **Cost Optimizer**: Find optimal valve mix for budget constraint
4. **Risk Explorer**: Adjust MTBF/MTTR/He price → see cost distribution

## v2.5 Material-Specific Traceability Notes
- Derogation documented: W1d warm valves use Meca Inox HDPE at 1×10⁻⁸ equivalent ambient class where 1×10⁻⁹ is considered non-industry-stringent.
- Supplier specs linked to source anchors from warm valve slide section 2.3.4 and vendor offers.
- RTM mapping focus: material choice, service type, and leak class acceptance boundaries.
