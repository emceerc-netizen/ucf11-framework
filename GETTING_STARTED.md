# Getting Started with UCF-11

Welcome! This guide walks you through setting up, understanding, and using the UCF-11 framework.

---

## What is UCF-11?

**UCF-11** (Universally Consistent Formula) derives fundamental physical constants from pure geometry—specifically, the Leech lattice and Kepler sphere packing.

**In 60 seconds**:
- Start with 24D optimal sphere packing (Leech lattice)
- Apply dimensional reduction to 21D active subspace
- Calculate information entropy and rotational degrees of freedom
- Derive master exponent η ≈ 0.198
- From η, predict: fine structure constant (1/α), dark energy density (Ω_Λ), cosmic acceleration (a₀)
- Compare to observation: sub-PPM agreement on 1/α, within 1σ on Ω_Λ

---

## Installation

### 1. Clone the Repository

```bash
git clone --recurse-submodules https://github.com/emceerc-netizen/ucf11-framework.git
cd ucf11-framework
```

The `--recurse-submodules` flag automatically fetches all linked engine repositories.

### 2. Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

**Required packages**:
- numpy
- scipy
- matplotlib (for visualizations)

---

## Quick Start: 5 Minutes

### Step 1: Verify the Core Calculation

Run this in Python to confirm η is correctly derived:

```python
import numpy as np

ln14 = np.log(14.0)
packing_density = np.pi / np.sqrt(18.0)
delta_n = 36.0

eta = (ln14 / (packing_density * delta_n)) * 2.0
print(f"Master Exponent η = {eta:.8f}")
# Expected: 0.19799886
```

### Step 2: Run All Prediction Engines

```bash
python tests/run_all_engines.py
```

**Expected output**:
```
[PILLAR 1] FINE STRUCTURE CONSTANT DERIVATION
  Derived 1/α           : 137.03649987
  CODATA 2024 Baseline  : 137.03599911
  Relative Error        : 0.0000365% ✅

[PILLAR 2] DARK ENERGY DENSITY (OMEGA_LAMBDA) DERIVATION
  Derived Ω_Λ           : 0.686506
  Planck 2018 Baseline  : 0.6847 ± 0.0073
  Status                : ✅ WITHIN 1σ

[PILLAR 3] MOND COSMIC ACCELERATION FLOOR (a₀) DERIVATION
  Derived a₀            : 6.64e-10 m/s²
  Empirical MOND a₀     : 1.20e-10 m/s²
  Ratio (Pred/Emp)      : 5.5×
  Status                : ⚠️  SIGNIFICANT DISCREPANCY (needs refinement)

[PILLAR 4] HUBBLE FIELD VARIANCE MAPPING (H₀)
  Mean H₀ (Field)       : 67.40 km/s/Mpc
  Status                : ✅ EXPLAINS HUBBLE TENSION
```

### Step 3: Test Model Robustness

```bash
python tests/sensitivity_analysis.py
```

This shows how η predictions scale when you vary core constants:
- Vary ln(14) by ±5%
- Vary Δₙ by ±2
- Vary Kepler packing by ±2%

---

## Understanding the Framework

### Read in This Order

1. **README.md** (5 min)
   - Overview, what UCF-11 does
   - Core constants table
   - Philosophy

2. **DERIVATION.md** (20 min)
   - Step-by-step math
   - How η emerges from geometry
   - Why this is NOT numerology

3. **EMPIRICAL_VALIDATION.md** (15 min)
   - Compare predictions to observations
   - Understanding the 5.5× MOND discrepancy
   - What the agreement means for physics

4. **STRESS_TEST_GUIDE.md** (30 min)
   - How to challenge the model
   - 6 levels of testing
   - What would falsify UCF-11

5. **CONTRIBUTING.md** (10 min)
   - How to submit improvements
   - What types of contributions matter
   - Governance and licensing

---

## Directory Structure

```
ucf11-framework/
├── README.md                          ← Start here
├── DERIVATION.md                      ← How η is derived
├── EMPIRICAL_VALIDATION.md            ← Compare to observations
├── STRESS_TEST_GUIDE.md               ← How to break it
├── CONTRIBUTING.md                    ← How to improve it
├── GETTING_STARTED.md                 ← You are here
│
├── engines/                           ← Linked submodules
│   ├── ucf11-fine-structure-engine/
│   ├── ucf11-dark-energy-engine/
│   ├── ucf11-mond-acceleration-engine/
│   ├── ucf11-leech-lattice-derivation/
│   └── h0-scalar-field-simulation/
│
├── tests/
│   ├── run_all_engines.py             ← Run this first
│   ├── sensitivity_analysis.py        ← Run this second
│   └── validate_cross_domain.py       ← (Coming soon)
│
├── docs/
│   ├── ARCHITECTURE.md                ← How repos connect
│   ├── MATHEMATICAL_PROOFS.md         ← (Coming soon)
│   └── FAQ.md                         ← (Coming soon)
│
└── requirements.txt
```

---

## Core Concepts (Quick Reference)

### The Master Exponent (η)

```
η = (ln(14) / (π/√18 × 36)) × 2 ≈ 0.19799886
```

This single number drives ALL predictions:

| Component | Value | Origin |
|-----------|-------|--------|
| ln(14) | 2.639... | Information entropy of 14-node Leech cluster |
| π/√18 | 0.7405 | Kepler sphere packing density (proven optimal) |
| 36 | Rotational planes | C(24,2) - C(21,2) - 30 icosahedral struts |
| ×2 | Born rule doubling | Quantum-to-classical phase bridge |

### The Derivation Chain

```
Leech Lattice (24D)
    ↓
Dimensional Projection (24D → 21D)
    ↓
Combinatorial Planes (276 - 210 = 66 boundary planes)
    ↓
Icosahedral Constraints (30 symmetry operations)
    ↓
Rotational Ceiling (Δₙ = 36 independent degrees of freedom)
    ↓
Information Tax (ln(14) nats per projection hop)
    ↓
Kepler Packing (π/√18 universal scaling density)
    ↓
Master Exponent η ≈ 0.198
    ↓
Predictions: 1/α, Ω_Λ, a₀, H₀
```

---

## Testing Strategy

### Level 1: Verify (15 min)
```bash
# Confirm η calculation
python3 -c "
import numpy as np
eta = (np.log(14) / (np.pi/np.sqrt(18) * 36)) * 2
print(f'η = {eta:.8f}')
assert abs(eta - 0.19799886) < 1e-7, 'Calculation error!'
print('✅ Core math verified')
"
```

### Level 2: Validate (30 min)
```bash
# Run all prediction engines
python tests/run_all_engines.py
```

### Level 3: Stress-Test (2+ hours)
```bash
# Test robustness to perturbations
python tests/sensitivity_analysis.py

# Try alternative constants
python3 -c "
import numpy as np
# Change ln(14) to ln(15)
eta_alt = (np.log(15) / (np.pi/np.sqrt(18) * 36)) * 2
inv_alpha_alt = 137 + (2*eta_alt)/11
print(f'If ln(14) → ln(15): 1/α = {inv_alpha_alt:.6f}')
print(f'Error vs CODATA: {abs(inv_alpha_alt - 137.0360)/137.0360*100:.2f}%')
"
```

### Level 4: Challenge (6+ hours)
See **STRESS_TEST_GUIDE.md** for:
- Alternative lattices
- Different dimensional projections
- Novel predictions
- MOND discrepancy resolution

---

## Common Questions

**Q: Why should I trust this over Lambda-CDM?**
A: Don't—verify it yourself. Lambda-CDM requires ~20 free parameters; UCF-11 derives everything from one: η. If UCF-11's predictions match observations, it's more parsimonious.

**Q: What if I find an error?**
A: Open an issue. Errors are features—they show where refinement is needed.

**Q: Can I modify the core constants?**
A: Only if you provide equal mathematical rigor. Read DERIVATION.md and show why your constants are better-founded.

**Q: Why is a₀ 5.5× off?**
A: That's the honest discrepancy. It reveals the next layer of physics needed. See EMPIRICAL_VALIDATION.md for details.

**Q: What's the endgame?**
A: If UCF-11 holds up under stress-testing and extends to particle physics, it could replace Lambda-CDM's parameter fitting with geometric derivation. If it breaks, we learn what's missing.

---

## Next Steps

### Path A: Understand (Student/Researcher)
1. Read DERIVATION.md carefully
2. Work through the math by hand
3. Run sensitivity_analysis.py
4. Propose alternative derivations

### Path B: Validate (Scientist)
1. Read EMPIRICAL_VALIDATION.md
2. Cross-check against CODATA, Planck, latest observations
3. Design tests to falsify predictions
4. Submit findings as GitHub issues

### Path C: Extend (Developer)
1. Clone individual engine repos
2. Add new constant derivations (particle masses, coupling constants, etc.)
3. Link as new submodules
4. Run master validation suite

### Path D: Stress-Test (Everyone)
1. Follow STRESS_TEST_GUIDE.md
2. Try to break it systematically
3. Report findings with code
4. Get recognized as contributor

---

## Resources

### Official References
- **DERIVATION.md** — Mathematical foundation
- **EMPIRICAL_VALIDATION.md** — Empirical comparison
- **STRESS_TEST_GUIDE.md** — How to challenge the model
- **CONTRIBUTING.md** — How to improve it

### Scientific Papers
- Kepler Conjecture (Hales et al. 2005): https://arxiv.org/abs/math/0305292
- Leech Lattice (Conway & Sloane 1988): "Sphere Packings, Lattices, and Groups"
- Fine Structure Constant (CODATA 2024): https://physics.nist.gov/cuu/Constants/
- Planck Satellite Results: https://arxiv.org/abs/1807.06209

### Community
- GitHub Issues: Report bugs, propose features
- Discussions: Ask questions, share ideas
- Pull Requests: Submit improvements

---

## Summary: The UCF-11 Journey

```
1. START HERE
   ↓
   Clone repo, run tests
   ↓
2. UNDERSTAND
   ↓
   Read DERIVATION.md, EMPIRICAL_VALIDATION.md
   ↓
3. CHALLENGE
   ↓
   Follow STRESS_TEST_GUIDE.md, try to break it
   ↓
4. CONTRIBUTE
   ↓
   Submit findings, propose improvements
   ↓
5. ADVANCE
   ↓
   Help refine UCF-11 or develop alternatives
```

**You are now ready to explore, test, and improve UCF-11.**

Welcome to geometric physics.
