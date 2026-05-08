# RTM Traceability

| implemented_in              | requirement_id   | status   | summary                          | verification                                                     |
|:----------------------------|:-----------------|:---------|:---------------------------------|:-----------------------------------------------------------------|
| src/calc_leak_rate.py       | RTM-047          | ACCEPT   | Math conversion                  | tests/test_calc_leak_rate.py::test_dimensional_chain             |
| docs/calculations.html      | RTM-048          | ACCEPT   | Temperature pressure sensitivity | tests/test_calc_leak_rate.py::test_temperature_pressure_scaling  |
| data/scenarios.json         | RTM-049          | ACCEPT   | Fleet scenarios                  | tests/test_calc_leak_rate.py::test_baseline_scenario_total_range |
| docs/dashboard.html         | RTM-050          | ACCEPT   | Dashboard visuals                | tests/test_build_outputs.py::test_required_outputs_exist         |
| docs/dashboard.html         | RTM-051          | ACCEPT   | Reliability strategy             | manual review                                                    |
| docs/executive_summary.html | RTM-052          | ACCEPT   | Cost/benefit                     | manual review                                                    |
| docs/handover.html          | RTM-053          | ACCEPT   | Handover package                 | tests/test_build_outputs.py::test_manifest_has_hashes            |
| src/calc_leak_rate.py       | RTM-054          | ACCEPT   | Math conversion                  | tests/test_calc_leak_rate.py::test_dimensional_chain             |
| docs/calculations.html      | RTM-055          | REVIEW   | Temperature pressure sensitivity | tests/test_calc_leak_rate.py::test_temperature_pressure_scaling  |
| data/scenarios.json         | RTM-056          | ACCEPT   | Fleet scenarios                  | tests/test_calc_leak_rate.py::test_baseline_scenario_total_range |
| docs/dashboard.html         | RTM-057          | ACCEPT   | Dashboard visuals                | tests/test_build_outputs.py::test_required_outputs_exist         |
| docs/dashboard.html         | RTM-058          | ACCEPT   | Reliability strategy             | manual review                                                    |
| docs/executive_summary.html | RTM-059          | ACCEPT   | Cost/benefit                     | manual review                                                    |
| docs/handover.html          | RTM-060          | REVIEW   | Handover package                 | tests/test_build_outputs.py::test_manifest_has_hashes            |
| src/calc_leak_rate.py       | RTM-061          | ACCEPT   | Math conversion                  | tests/test_calc_leak_rate.py::test_dimensional_chain             |
| docs/calculations.html      | RTM-062          | ACCEPT   | Temperature pressure sensitivity | tests/test_calc_leak_rate.py::test_temperature_pressure_scaling  |
| data/scenarios.json         | RTM-063          | ACCEPT   | Fleet scenarios                  | tests/test_calc_leak_rate.py::test_baseline_scenario_total_range |
| docs/dashboard.html         | RTM-064          | ACCEPT   | Dashboard visuals                | tests/test_build_outputs.py::test_required_outputs_exist         |
| docs/dashboard.html         | RTM-065          | ACCEPT   | Reliability strategy             | manual review                                                    |
| docs/executive_summary.html | RTM-066          | REVIEW   | Cost/benefit                     | manual review                                                    |
| docs/handover.html          | RTM-067          | ACCEPT   | Handover package                 | tests/test_build_outputs.py::test_manifest_has_hashes            |

## DMAIC View Note
- DEFINE: requirement-to-implementation map.
- MEASURE: all RTM rows captured with verification hooks.
- ANALYZE: detects review/risk rows quickly.
- IMPROVE: supports audit readiness.
- CONTROL: generated deterministically from build script.
