# UCF-11 Multi-Layer Architecture

This repository now follows a clean three-layer design model to preserve separation of responsibilities and avoid overlap between mathematical exploration, physical validation, and hardware realization.

## 1) Python Layer: Future / Exploration / Prediction
Purpose:
- model high-dimensional manifold behavior
- generate candidate geometry states
- stress-test fractal boundaries
- optimize pin formations and coordinate layouts
- provide a reference model for future hardware validation

This layer does not implement the embedded system. It explores the geometry and produces test vectors, boundary maps, and candidate routes.

## 2) C++ Layer: Proven / Real-World / Physical Lock
Purpose:
- validate against real or synthetic ADC/physical manifold data
- compute residual drift against the icosahedral manifold
- execute fixed-point Q16.16 arithmetic in hardware-like conditions
- provide the reliable physical baseline for locking and drift analysis

This layer is the embedded/manifold-lock truth model.

## 3) Verilog Layer: Hardware / Fractal Core / RTL
Purpose:
- realize the fractal core in hardware
- implement Fibonacci-gated stepping
- evaluate bounded vs escape regions
- synthesize a hardware-validated manifold decision path

This layer is the implementation target for the mathematical boundary evaluation.

---

# Repository Structure

```text
ucf11-framework/
├── README.md
├── DEVELOPMENT_ROADMAP.md
├── DESIGN_NOTES.md
├── ucf11_top_fractal_core.v
├── cpp/
│   ├── arm_icosahedral_processor.cpp
│   ├── fixed_point_utils.h
│   ├── icosahedral_manifold.h
│   └── tests/
│       └── test_icosahedral_lock.cpp
├── python/
│   ├── __init__.py
│   ├── manifold_optimizer.py
│   ├── fractal_reference_model.py
│   ├── boundary_generator.py
│   ├── pin_formation_validator.py
│   ├── fibonacci_scheduler.py
│   ├── integration_test_driver.py
│   └── tests/
│       ├── test_boundary_accuracy.py
│       ├── test_drift_prediction.py
│       ├── test_fibonacci_timing.py
│       └── test_pin_formations.py
├── verilog/
│   ├── ucf11_fibonacci_prime_clock_manager.v
│   ├── ucf11_top_fractal_core.v
│   └── tests/
│       └── fractal_core_tb.v
├── tests/
│   └── integration/
│       ├── test_manifold_lock.py
│       ├── test_pipeline_consistency.py
│       └── test_boundary_vs_drift.py
└── docs/
    └── architecture_overview.md
```

---

# Python Layer Specification

## manifold_optimizer.py
This is the geometry exploration engine.

Responsibilities:
- initialize high-dimensional candidate nodes
- apply dimensionally-aware regularization
- optimize geometry toward a stable manifold
- generate candidate layouts for pin formations
- produce highly structured output ready for downstream validation

Recommended functions:
- `initialize_nodes(n_nodes, n_dimensions)`
- `compute_pairwise_distances(nodes)`
- `soften_distances(distances, softening)`
- `optimize_geometry(steps)`
- `export_candidate_layout(path)`

## fractal_reference_model.py
This is the mathematical reference model.

Responsibilities:
- compute high-precision Mandelbrot-style boundary conditions
- mark bounded vs escape regions
- generate synthetic coordinate vectors for hardware validation
- compare Q16.16 truncation errors against high-precision math

Recommended functions:
- `mandelbrot_escape(c_r, c_i, max_iter, escape_threshold)`
- `generate_reference_grid(x_range, y_range, samples)`
- `compare_q16q_precision(reference, q_fixed)`

## boundary_generator.py
This generates the test vectors that the Verilog core must consume.

Responsibilities:
- create complex coordinate seeds near the boundary
- produce bounded/escape edge cases
- stress the threshold region
- generate deterministic test sets for reproducible hardware validation

Recommended functions:
- `generate_boundary_vectors(center, span, samples)`
- `generate_escape_cases(count)`
- `generate_bounded_cases(count)`

## pin_formation_validator.py
This applies the manifold logic to candidate pin formations.

Responsibilities:
- map candidate node layouts to routing or pin arrangements
- identify which formations remain bounded
- reject unstable formations
- estimate which icosahedral-like layouts are physically valid

Recommended functions:
- `validate_pin_layout(layout)`
- `rank_formations(formations)`
- `export_valid_layouts(layouts)`

## fibonacci_scheduler.py
This models the non-uniform pulse schedule.

Responsibilities:
- analyze Fibonacci pulse timing
- predict iteration pacing across valid and invalid regions
- compare uniform-vs-Fibonacci stepping
- supply scheduling parameters to the Verilog design

Recommended functions:
- `generate_fibonacci_sequence(limit)`
- `simulate_timing(schedule, iterations)`
- `compare_step_efficiency()`

## integration_test_driver.py
This is the orchestrator for full pipeline validation.

Responsibilities:
- generate candidate geometric states
- feed them to the fractal reference model
- feed them to the Verilog testbench or hardware simulation
- compare hardware outputs to Python reference
- pass physical drift outputs through the C++ manifold lock model

Recommended functions:
- `run_reference_suite()`
- `run_verilog_suite()`
- `run_cpp_suite()`
- `generate_report()`

---

# C++ Layer Specification

## fixed_point_utils.h
Purpose:
- define Q16.16 integer arithmetic helpers
- safe multiply operations for fixed-point values
- conversion helpers between integer and normalized values

Example API:
- `q16_from_int32(value)`
- `q16_multiply(a, b)`
- `q16_shift_right(value, shift)`
- `q16_abs(value)`

## icosahedral_manifold.h
Purpose:
- define the 12-node manifold table
- hardcode the icosahedral geometry in fixed-point integer form
- provide a direct mapping from ADC channels to manifold coordinates

## arm_icosahedral_processor.cpp
Purpose:
- compute residual drift for the current physical state
- interpret ADC inputs against the ideal manifold
- return zero when aligned or drift magnitude when unstable

Suggested API:
- `int32_t process_arm_icosahedral_channels(const int16_t* raw_adc_voltages);`

This is the real-world physical lock baseline.

---

# Verilog Layer Specification

## ucf11_fibonacci_prime_clock_manager.v
Purpose:
- generate the Fibonacci-driven pulse gate
- freeze pulse generation when `system_fracture` is asserted

## ucf11_top_fractal_core.v
Purpose:
- iterate the Mandelbrot-style recurrence
- gate iteration on Fibonacci pulses
- evaluate bounded vs escape state
- produce `manifold_bounded` and `manifold_escape`

This module is the hardware implementation of the mathematical validity boundary.

---

# Integration Strategy

## Step 1: Build Python reference and candidate geometry generators
- Develop the exact high-precision fractal and manifold reference model
- Generate bounded, escape, and threshold-close test cases
- Feed these into the Verilog simulation pipeline

## Step 2: Validate Verilog against Python boundary reference
- For each generated coordinate, check:
  - is the fractal core bounded or escape?
  - does it match the Python reference?
- Evaluate off-by-one and Q16.16 threshold drift

## Step 3: Validate C++ physical lock against the same input classes
- Feed synthetic ADC values representing stable vs unstable physical positions
- Confirm the residual drift correlates with the fractal classification

## Step 4: Build full integration harness
- Python generates candidate layouts and coordinate sets
- Verilog validates the mathematical valid manifold
- C++ validates the physical manifold lock
- Integration tests determine whether the system is truly stable or if it has crossed the boundary

---

# Validation Matrix

| Function | Python | C++ | Verilog |
|----------|--------|-----|---------|
| High-precision fractal boundary | Yes | No | No |
| Q16.16 fixed-point manifold lock | No | Yes | Yes |
| Candidate geometry exploration | Yes | No | No |
| Physical ADC drift measurement | No | Yes | No |
| Hardware escape/bounded decision | Reference only | No | Yes |
| Integration validation | Yes | Yes | Yes |

This matrix preserves separation while allowing full-system validation.

---

# Philosophy: No Overlap

The architecture intentionally avoids overlap:
- Python is for discovery and prediction
- C++ is for physical real-world validation
- Verilog is for hardware implementation

No single layer tries to do all three jobs.

This preserves clarity, keeps the repo maintainable, and creates a clean pipeline for future contributors.

---

# Recommended Next Actions

1. Create `python/` directory and populate the reference models
2. Implement Python generation of boundary test vectors
3. Create a minimal `integration_test_driver.py` to orchestrate validation
4. Ensure Verilog outputs match the Python reference expectations
5. Ensure C++ residual drift matches physical manifold assumptions
6. Run an end-to-end pipeline check across all three layers

This is the proper path for turning the architecture into a reviewable, testable, and extensible system.
