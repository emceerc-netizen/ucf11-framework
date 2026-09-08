# UCF-11: Universally Consistent Formula

A geometric first-principles framework for deriving fundamental physical constants from Leech lattice topology, Kepler packing limits, and golden ratio invariants.

**No free parameters. No tuning matrices. Just pure geometry.**

---

## What UCF-11 Does

Instead of fitting ~20+ empirical parameters (Lambda-CDM approach), UCF-11 derives fundamental constants directly from topological invariants:

- **Fine Structure Constant (1/α)** → 137.0365... vs. CODATA 137.0360 (PPM precision)
- **Dark Energy Density (Ω_Λ)** → 0.6865 vs. Planck 0.6879 (sub-percent accuracy)
- **MOND Acceleration Floor (a₀)** → Cosmic buoyancy from surface tension scaling
- **Hubble Field Variance (H₀)** → Local scalar field structure

All predictions flow from:
- **Leech Lattice (Λ₂₄)**: 24D optimal packing, kissing number = 196,560
- **Kepler Packing Density**: π/√18 ≈ 0.7405 (proven maximum in 3D)
- **Master Exponent (η)**: (ln(14) / (packing_density × 36)) × 2 ≈ 0.198

---

## How It's Organized

```
ucf11-framework/
├── README.md                             (This file)
├── DERIVATION.md                         (How η emerges from geometry)
├── EMPIRICAL_VALIDATION.md              (All predictions vs. observations)
├── CONTRIBUTING.md                       (How to add engines or refine)
│
├── engines/                              (Linked via git submodules)
│   ├── ucf11-fine-structure-engine/
│   ├── ucf11-dark-energy-engine/
│   ├── ucf11-mond-acceleration-engine/
│   ├── ucf11-leech-lattice-derivation/
│   └── h0-scalar-field-simulation/
│
├── tests/
│   ├── run_all_engines.py
│   ├── validate_cross_domain.py
│   └── sensitivity_analysis.py
│
└── docs/
    ├── ARCHITECTURE.md
    ├── STRESS_TEST_GUIDE.md
    └── GETTING_STARTED.md
```

---

## Quick Start

### 1. Clone the framework

```bash
git clone --recurse-submodules https://github.com/emceerc-netizen/ucf11-framework.git
cd ucf11-framework
```

### 2. Run all prediction engines

```bash
python tests/run_all_engines.py
```

### 3. Stress-test with sensitivity analysis

```bash
python tests/sensitivity_analysis.py
```

---

## The Core Constants

| Constant | Value | Origin |
|----------|-------|--------|
| **Leech Dimensions** | 24 | Λ₂₄ optimal packing |
| **Active Subspace** | 21 | 24 - 3 dimensional reduction |
| **Packing Density** | π/√18 ≈ 0.7405 | Kepler Conjecture (proven) |
| **Kissing Number** | 196,560 | Contact points per sphere |
| **Local Cluster** | 14 | Leech substructure |
| **Rotational Planes** | 36 | C(24,2) - C(21,2) - 30 |
| **Master Exponent (η)** | (ln(14) / (0.7405 × 36)) × 2 | Derived |
| **Golden Ratio (φ)** | (1+√5)/2 ≈ 1.618 | Cosmic balance |

---

## Philosophy

Lambda-CDM requires ~20 free parameters and ~10⁵⁰⁰ string vacua. UCF-11 asks: **What if fundamental constants are forced by geometry?**

Then we derive, not fit. We have one framework, not 10⁵⁰⁰ vacua. Anyone can verify or break it.

---

## Next Steps

- Read **[DERIVATION.md](./DERIVATION.md)** — Step-by-step proof that η must take its value
- Read **[EMPIRICAL_VALIDATION.md](./EMPIRICAL_VALIDATION.md)** — Full comparison against observations
- Run the tests and stress-test the framework
- Contribute refinements

---

## License

MIT. Use, modify, test, and distribute freely.

---

**Made by Rick Collard. Open for collaborative verification and refinement.**
