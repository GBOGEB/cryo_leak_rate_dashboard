# FAT/SAT Procedures — QPLANT Cryogenic Helium System

## 1. FAT Procedure: Valve Leak Testing (per EN 13185 & ISO 5208)

### 1.1 Preparation
1. Valve installed in test fixture with known calibrated volume
2. Helium mass spectrometer calibrated (calibration cert <1 year old, NIST-traceable)
3. Standard leak verified: ±10% of stated value
4. Test volume evacuated to <1×10⁻³ mbar
5. Ambient temperature recorded (stability ±2°C over test duration)
6. Valve identification: serial number, model, DN, PN, manufacturer

### 1.2 Test Execution
1. Pressurize upstream side with helium to specified operating pressure
2. Wait 5 minutes for thermal equilibrium
3. Detect helium on downstream (vacuum) side with mass spectrometer
4. Record leak rate (mbar·l/s) — minimum 60 seconds continuous
5. Repeat measurement 3 times; report arithmetic mean
6. Record background leak rate before and after test

### 1.3 Acceptance Criteria (RTM Table 6)

| Type | Limit (mbar·l/s) | Standard | Notes |
|------|-------------------|----------|-------|
| Leak to vacuum | <1×10⁻⁸ | EN 13185 §6.2 | Process boundary |
| Leak to ambient | <1×10⁻⁹ | EN 13185 §6.2 | External leakage |
| Valve seat (internal) | <1×10⁻⁴ | ISO 5208 §6.3.2 | Across valve seat |
| System total | <1×10⁻⁵ | RTM-048 | All valves combined |

### 1.4 Deliverables
- Leak test data sheet (per valve: S/N, date, operator, 3× measurements, average, pass/fail)
- Calibration certificate for mass spectrometer
- Calibration certificate for standard leak
- Photo evidence of test setup
- Accept/Reject decision signed by QA Inspector

---

## 2. SAT Procedure: System-Level Leak Test

### 2.1 Scope
Entire QPLANT system after installation — validates RTM-048 and RTM-053.

### 2.2 Method: Pressure Hold Test (24-hour)
1. Isolate system section under test
2. Pressurize with helium to operating pressure
3. Record initial pressure P₁ and temperature T₁
4. Monitor continuously for 24 hours (minimum)
5. Record final P₂ and T₂
6. Calculate: Q_leak = (P₁ - P₂) × V / Δt [mbar·l/s]
7. Temperature correction: Q_corr = Q_leak × (T₁/T₂)

### 2.3 Acceptance
- Total system leak rate < 1×10⁻⁵ mbar·l/s (RTM-048)
- He loss rate < 1 Nm³/day (RTM-048)
- Functional test under simulated LOOP conditions (RTM-053)

### 2.4 Deliverables
- Pressure-time chart (continuous, calibrated recorder)
- Temperature log (exclude thermal effects)
- Leak rate calculation sheet
- Acceptance sign-off (PM + QA)
- Punch list (if remedial action required)
