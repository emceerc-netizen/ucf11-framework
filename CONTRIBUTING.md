# Contributing to UCF-11

Thank you for your interest in improving UCF-11! This document explains how to contribute responsibly.

---

## Core Principle

UCF-11 is a **testable, falsifiable geometric framework**. Contributions should either:

1. **Strengthen the foundation** — prove assumptions more rigorously
2. **Extend the model** — derive new constants or phenomena from η
3. **Refine predictions** — improve accuracy or explain discrepancies
4. **Stress-test** — attempt to break it with rigor

Contributions that do none of these will be politely declined.

---

## Before You Start

1. **Read DERIVATION.md** — understand how η is derived
2. **Read EMPIRICAL_VALIDATION.md** — see current state and gaps
3. **Read STRESS_TEST_GUIDE.md** — understand how to challenge the model
4. **Run tests locally**:
   ```bash
   python tests/run_all_engines.py
   python tests/sensitivity_analysis.py
   ```

---

## Contribution Types

### Type 1: Bug Reports

**Report bugs in code, math, or documentation.**

**Template**:
```
Title: [BUG] Brief description

What I did:
[Code or step to reproduce]

What I expected:
[Expected result]

What happened:
[Actual result]

Environment:
- Python version
- OS
- Dependencies (pip freeze)
```

**Example**:
```
Title: [BUG] η calculation gives wrong result in sensitivity_analysis.py

What I did:
python tests/sensitivity_analysis.py

What I expected:
η = 0.19799886

What happened:
η = 0.19799885 (differs at 8th decimal)

This may be a floating-point precision issue.
```

---

### Type 2: Mathematical Refinements

**Strengthen the derivation of η or its constants.**

**What counts**:
- Prove why ln(14) *must* be the information entropy (don't just assert it)
- Show group-theoretic proof that 30 icosahedral struts are necessary
- Derive 36 from first principles in lattice topology
- Alternative lattices with equivalent rigor

**What doesn't count**:
- "I think the formula is wrong" (show the error)
- "This seems like numerology" (demonstrate how)
- Replacing constants without justification

**Process**:
1. Open an issue describing your refinement
2. Link to papers/proofs supporting your claim
3. Provide code showing the new η value and predictions
4. Discuss implications with maintainers
5. If accepted, submit PR with updated docs

**Example PR**:
```
Title: [MATH] Prove 36 rotational planes from E8 automorphism group

Description:
Currently, Δₙ = 36 is derived as C(24,2) - C(21,2) - 30.
I show that 36 is the rank of the root system of the Leech lattice automorphism group.

Files changed:
- DERIVATION.md: Expanded section on rotational planes
- docs/leech_automorphisms.md: New file with group-theoretic proof

Validation:
- All existing tests pass
- 1/α still matches CODATA to PPM precision
```

---

### Type 3: New Engine Modules

**Derive new physical constants from η.**

**What counts**:
- Clear derivation from η and geometric constants
- Comparison against empirical data
- Uncertainty analysis
- Documentation

**What doesn't count**:
- Guessing constants and fitting to data
- "This should work" without derivation
- Constants unrelated to Leech geometry

**Process**:
1. Create a new repo: `ucf11-[constant]-engine`
2. Structure it like `ucf11-fine-structure-engine`:
   ```
   ucf11-constant-engine/
   ├── README.md
   ├── requirements.txt
   ├── engine.py
   └── tests/
       ├── test_predictions.py
       └── fixtures/empirical_data.json
   ```
3. Link to master framework as submodule
4. Run validation against empirical baselines
5. Submit PR to add submodule to master framework

**Example**: Derive muon-to-electron mass ratio (m_μ / m_e ≈ 206.77)

```python
# ucf11_muon_mass_engine.py
import numpy as np

class UCF11MuonMassEngine:
    def __init__(self):
        self.eta = 0.19799886
        self.n_dimensions = 11.0
        self.phi = (1 + np.sqrt(5)) / 2.0
    
    def derive_muon_electron_ratio(self):
        # Derive from η and M-Theory geometry
        # Must show: why this derivation is forced, not chosen
        muon_electron_ratio = ...
        return muon_electron_ratio
```

---

### Type 4: Sensitivity & Robustness Tests

**Extend tests/sensitivity_analysis.py with new test cases.**

**What counts**:
- Systematic variation of one constant while others fixed
- Clear documentation of what's being tested
- Quantified results (deviation %, ratio, etc.)
- Interpretation of findings

**What doesn't count**:
- Random parameter sweeps
- "I tried lots of values, nothing worked"
- Tests without clear hypothesis

**Process**:
1. Add function to `tests/sensitivity_analysis.py`:
   ```python
   def test_golden_ratio_variation(self):
       """Test impact of golden ratio perturbations"""
       phi_variations = [...]
       # Run predictions, measure deviations
       # Plot results
       # Interpret
   ```
2. Document clearly: what varies, what's fixed, why this matters
3. Submit PR with results and interpretation

---

### Type 5: Documentation & Communication

**Improve clarity without changing code.**

**What counts**:
- Clearer explanations of derivations
- More examples or visualizations
- Better structure/organization
- Corrections to typos/errors
- Additional context/background

**What doesn't count**:
- Opinions on whether UCF-11 is "right"
- Complaints about presentation style
- Generic "could be better"

**Process**:
1. Edit the relevant `.md` file
2. Submit PR with changes
3. Maintainers review and merge if clarity improves

---

## Workflow

### For Small Changes (typo, clarification, minor fix)

1. Fork the repo
2. Create branch: `git checkout -b fix/typo-in-derivation`
3. Edit and commit: `git commit -m "Fix typo in DERIVATION.md"`
4. Push: `git push origin fix/typo-in-derivation`
5. Open PR: describe the change
6. Wait for review and merge

### For Substantial Contributions (new engine, major refinement)

1. **Open an issue first** — describe what you want to do
2. **Get feedback** — ensure it aligns with project vision
3. **Fork and develop**:
   ```bash
   git checkout -b feature/new-engine-name
   # Make changes, test thoroughly
   python tests/run_all_engines.py
   python tests/sensitivity_analysis.py
   ```
4. **Commit with clear messages**:
   ```bash
   git commit -m "[FEATURE] Derive X constant from η

   Derivation:
   - Start from Leech geometry
   - Apply Born rule scaling
   - Result: X ≈ [value]
   
   Empirical comparison:
   - Predicted: [pred]
   - Observed: [obs]
   - Error: [err]%
   
   Related issue: #42"
   ```
5. **Push and open PR**:
   ```bash
   git push origin feature/new-engine-name
   ```
6. **Respond to code review** — maintainers may ask questions
7. **Merge** once approved

---

## Code Style

- **Python**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- **Comments**: Explain *why*, not what
- **Docstrings**: Include at top of class/function
- **Tests**: Run before submitting PR
- **Reproducibility**: All results must be reproducible from code

---

## What Gets Rejected

- ❌ "This should be changed" without explanation
- ❌ Alternative frameworks that ignore Leech geometry
- ❌ Fitting constants to match observations (defeats the point)
- ❌ Unsubstantiated claims ("I think η should be 0.2 instead")
- ❌ Personal opinions on whether physics "should" work this way
- ❌ Contributions not under MIT license

---

## What Gets Accepted

- ✅ Rigorous mathematical proofs
- ✅ Empirical validation against peer-reviewed data
- ✅ Clear documentation and reproducibility
- ✅ Tests that strengthen or challenge the model
- ✅ Honest discussion of limitations and open questions

---

## Governance

**Maintainer**: Rick Collard (@emceerc-netizen)

Decisions on major changes (core constants, framework restructuring) rest with maintainers, but are made openly with community input.

Minor contributions (docs, tests, bug fixes) are typically fast-tracked.

---

## License

By contributing, you agree that your contributions are licensed under the MIT License. You retain copyright, but grant others the right to use, modify, and distribute your work under MIT terms.

---

## Questions?

- **How do I...?** → Read STRESS_TEST_GUIDE.md
- **Is this a valid contribution?** → Open an issue and ask
- **Can I modify the core constants?** → Only with mathematical proof
- **Can I propose a different derivation?** → Yes, if equally rigorous

---

## Thank You

Every contribution—from fixing typos to deriving new constants—makes UCF-11 stronger, more tested, and more credible.

The goal is collaborative verification of a testable model.

Welcome aboard.
