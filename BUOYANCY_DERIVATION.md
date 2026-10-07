# Buoyancy Derivation from 24D→21D Projection

## Objective

This note derives a first-pass expression for the buoyant acceleration term used in the galaxy rotation model. The aim is to connect the framework's master exponent `η` to a physically dimensioned acceleration scale without introducing arbitrary tuning.

---

## 1. Starting Geometry

From the framework derivation, the master exponent is:

```python
eta = (ln(14) / (pi / sqrt(18) * 36)) * 2
```

Numerically:

```python
eta ≈ 0.19799886
```

This quantity is constructed from:
- `ln(14)`: the saturated lattice-state entropy contribution
- `pi / sqrt(18)`: the maximum 3D sphere-packing density (Kepler limit)
- `36`: the dimensional rotational boundary term derived from the projected topology

The framework interprets the universe as a 24-dimensional topological manifold whose observed interface reduces to a 21-dimensional active subspace.

The essential geometric statement is:

```text
24D manifold
  - 3 observable projection dimensions
  = 21 active dimensional substrate
```

The 3 removed dimensions represent the interaction artifacts through which we perceive the universe: spatial projection, temporal ordering, and gravitational curvature.

---

## 2. Projection Cost

A projection from a richer topological space into a lower-dimensional active surface cannot be lossless. The framework models this as a projection cost factor:

```text
projection_cost = 1 / (1 - eta)
```

This is the first structural correction factor. It captures the geometric amplification produced by the hidden 24D manifold when its effects are expressed through the active 21D substrate.

Numerically:

```python
projection_cost = 1 / (1 - eta)
               ≈ 1 / 0.80200114
               ≈ 1.2475
```

So the 24D→21D compression does not merely reduce dimensionality — it induces a nonlinear amplification in the effective response of the substrate.

---

## 3. Cosmological Acceleration Scale

The natural acceleration scale associated with the expanding universe is the characteristic acceleration of the Hubble flow:

```text
a_scale = c * H0 / (2π)
```

This form is chosen because:
- `c` provides the velocity scale
- `H0` provides the cosmological time scale
- `2π` is the angular normalization consistent with a rotationally bounded manifold

Using a representative Hubble parameter:

```python
H0 = 70 km/s/Mpc ≈ 2.268e-18 s^-1
c  = 2.99792458e8 m/s
```

Then:

```python
a_scale = (c * H0) / (2*pi)
        ≈ 1.08e-10 m/s^2
```

This is the correct order of magnitude for the observed MOND-like acceleration floor and is also close to the value used in the galaxy model.

---

## 4. Buoyant Acceleration Ansatz

The buoyant acceleration is modelled as the geometric projection cost acting on the cosmological acceleration scale:

```text
a_buoyant = projection_cost * a_scale
```

Substituting:

```text
a_buoyant = [1 / (1 - eta)] * [c * H0 / (2π)]
```

This gives:

```python
a_buoyant ≈ 1.2475 * 1.08e-10
          ≈ 1.35e-10 m/s^2
```

This is very close to the implementation constant used in the framework:

```python
a_buoyant = 1.30e-10
```

The difference is only on the order of ~4–5%, which is small enough to treat as a first-pass derivation rather than a final one.

---

## 5. Why This Is Physically Meaningful

The model interprets the galaxy rotation anomaly as a buoyancy effect from the active 21D substrate, not as hidden mass in the conventional sense.

The key logic is:

1. The universe is not observed in its full 24D topology.
2. We experience only the 3D projection of the underlying structure.
3. The 21D substrate remains physically active but not directly observable.
4. The geometric projection from 24D to 21D introduces an amplification factor.
5. This amplification acts on the natural cosmological acceleration scale `c * H0 / 2π`.
6. The resulting acceleration is the buoyant term entering the galaxy rotation model.

This makes the buoyant term a consequence of the geometry and the expansion scale, rather than an arbitrary constant inserted ad hoc.

---

## 6. Relation to the Galaxy Model

The galaxy code uses:

```python
a_N = (G * M_baryonic) / r^2

a_W = sqrt(a_N * a_buoyant)
```

The buoyant acceleration enters through the geometric mean, meaning the framework treats the effective response as a coupled gravitational-buoyancy interaction rather than a pure additional mass term.

This is consistent with the core interpretation that the galaxy is not simply orbiting in vacuum, but moving in a structured medium-like substrate whose effective response is determined by the projected geometric topology.

---

## 7. Interpretation

This derivation is not presented as final proof. It is a physically motivated first approximation that:

- derives `a_buoyant` from the framework's own master exponent `η`
- preserves the 24D→21D projection logic
- uses a natural cosmological acceleration scale
- reproduces the correct order of magnitude for the framework's observed constant

The strongest point is that the buoyant term is not invented in isolation. It is a direct consequence of:
- lattice geometry
- dimensional projection
- expansion-scale physics

---

## 8. Open Refinement Path

The derivation is still provisional. The next steps are:

1. Re-derive the exact geometric factor from the 24D→21D projection rather than using the phenomenological correction `1 / (1 - η)`
2. Confirm which Hubble parameter is the correct one for the model (Planck, local field, or a framework-specific value)
3. Test the resulting formula over multiple galaxy populations, not only spiral galaxies and ultra-diffuse systems
4. Compare the derived `a_buoyant` to the MOND acceleration scale and to galaxy rotation curve residuals in a systematic way

---

## Final Form (Current Working Hypothesis)

```text
a_buoyant ≈ [1 / (1 - η)] * [c * H0 / (2π)]
```

with:

```text
η ≈ 0.19799886
```

This is the current working derivation for the buoyant term in the framework.
