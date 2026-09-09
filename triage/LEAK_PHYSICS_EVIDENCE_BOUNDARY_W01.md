# Leak physics evidence boundary W01

Observed base SHA: `0e473475dbe0662541a67af52f86a79b93b6e7d6`

This repository is retained as an independent engineering-validation satellite. Its first-principles leak conversion engine is useful for QPS/ABACUS cross-checking, but two distinct semantics must remain separate:

1. **Throughput conversion**: a stated leak rate in mbar·L/s is converted to molar/mass flow using the stated reference condition.
2. **Operating-point pressure sensitivity**: multiplying that throughput by `pressure_bar_abs / reference_pressure_bar` is a comparative sensitivity assumption, not a new measured leak-rate property.

The current implementation in `src/calc_leak_rate.py` already exposes both inputs, but downstream consumers can otherwise mistake the sensitivity scaling for source evidence. TRIAGE promotion therefore requires the receipt to record `interpretation`, `reference_pressure_bar`, `temperature_k`, and whether pressure scaling was applied.

Bridge targets:
- cryoplant-project: independent leak / helium-loss cross-check only;
- ABACUS: calculation evidence + RTM/test linkage;
- CODEX/TRIAGE: receipt schema and deterministic execution.

No bidder compliance, formal engineering score, or release credit is created until a result is bound to current QPS source IDs and an exact source SHA.
