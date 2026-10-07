import numpy as np
import matplotlib.pyplot as plt

class BuoyancyFramework:
    """
    Test the derived buoyancy formula against galaxy rotation curves.
    
    Formula: a_buoyant = [1 / (1 - η)] × [c × H0 / (2π)]
    """
    
    def __init__(self, H0_kmsMpc=70.0):
        # Framework constants
        self.ln14 = np.log(14)
        self.packing_density = np.pi / np.sqrt(18)
        self.delta_n = 36
        self.eta = (self.ln14 / (self.packing_density * self.delta_n)) * 2
        
        # Physical constants
        self.G = 6.6743e-11  # m^3 / (kg * s^2)
        self.c = 2.99792458e8  # m/s
        
        # Hubble parameter (convert km/s/Mpc to s^-1)
        self.H0_kmsMpc = H0_kmsMpc
        self.H0_SI = H0_kmsMpc * 1000 / 3.086e22  # convert to s^-1
        
        # Derive a_buoyant from the formula
        projection_cost = 1.0 / (1.0 - self.eta)
        a_scale = (self.c * self.H0_SI) / (2.0 * np.pi)
        self.a_buoyant = projection_cost * a_scale
        
        print(f"Framework Initialization:")
        print(f"  η = {self.eta:.8f}")
        print(f"  Projection Cost (1/(1-η)) = {projection_cost:.8f}")
        print(f"  H0 = {self.H0_kmsMpc} km/s/Mpc = {self.H0_SI:.6e} s^-1")
        print(f"  a_scale (c*H0/2π) = {a_scale:.6e} m/s^2")
        print(f"  a_buoyant (derived) = {self.a_buoyant:.6e} m/s^2")
        print()
    
    def predict_rotation_curve(self, M_baryonic_kg, radius_kpc, dimensional_state=3.0):
        """
        Predict galaxy rotation velocity using the buoyancy model.
        
        a_N = Newtonian acceleration from baryonic mass
        a_W = buoyant acceleration (scaled by dimensional state)
        v = orbital velocity
        """
        r_m = radius_kpc * 3.086e19  # kpc to meters
        
        a_N = (self.G * M_baryonic_kg) / (r_m**2)
        a_W = np.sqrt(a_N * self.a_buoyant) * (dimensional_state / 3.0)
        
        v_predicted = np.sqrt((a_N + a_W) * r_m) / 1000.0  # convert to km/s
        
        return {
            'a_N': a_N,
            'a_W': a_W,
            'v_predicted': v_predicted,
            'ghost_mass': (a_W * r_m**2) / self.G,
            'ghost_ratio': (a_W * r_m**2) / (self.G * M_baryonic_kg)
        }
    
    def test_galaxies(self, galaxy_data):
        """Test against a dictionary of galaxy data."""
        results = []
        
        for name, data in galaxy_data.items():
            pred = self.predict_rotation_curve(
                data['M_baryonic'],
                data['radius_kpc'],
                data.get('dim_state', 3.0)
            )
            
            v_obs = data['v_observed']
            error_pct = abs(pred['v_predicted'] - v_obs) / v_obs * 100
            
            result = {
                'name': name,
                'type': data.get('type', 'spiral'),
                'dim_state': data.get('dim_state', 3.0),
                'v_predicted': pred['v_predicted'],
                'v_observed': v_obs,
                'error_pct': error_pct,
                'ghost_ratio': pred['ghost_ratio'],
                'a_W': pred['a_W'],
                'a_N': pred['a_N']
            }
            results.append(result)
        
        return results

# ============================================================================
# COMPREHENSIVE GALAXY TEST SET
# ============================================================================

galaxy_data = {
    # --- LARGE SPIRAL GALAXIES ---
    "Milky Way": {
        "type": "large_spiral",
        "M_baryonic": 1.0e41,       # ~6e10 solar masses
        "radius_kpc": 26.0,          # inner measurement point
        "v_observed": 230.0,
        "dim_state": 3.0,
        "notes": "Local standard of rest"
    },
    
    "Andromeda (M31)": {
        "type": "large_spiral",
        "M_baryonic": 1.5e41,
        "radius_kpc": 32.0,
        "v_observed": 225.0,
        "dim_state": 3.0,
        "notes": "Nearest major galaxy"
    },
    
    # --- MEDIUM SPIRALS (Well-measured rotation curves) ---
    "NGC 3198": {
        "type": "medium_spiral",
        "M_baryonic": 4.0e40,        # ~2.7e10 solar masses
        "radius_kpc": 25.0,
        "v_observed": 165.0,
        "dim_state": 3.0,
        "notes": "Classic extended rotation curve"
    },
    
    "NGC 2841": {
        "type": "medium_spiral",
        "M_baryonic": 8.0e40,
        "radius_kpc": 28.0,
        "v_observed": 180.0,
        "dim_state": 3.0,
        "notes": "High-mass spiral"
    },
    
    # --- DWARF GALAXIES ---
    "DDO 154": {
        "type": "dwarf_spiral",
        "M_baryonic": 1.0e39,        # ~0.7e9 solar masses
        "radius_kpc": 8.0,
        "v_observed": 40.0,
        "dim_state": 3.0,
        "notes": "Low-mass dwarf irregular"
    },
    
    "NGC 2976": {
        "type": "dwarf_spiral",
        "M_baryonic": 2.0e39,
        "radius_kpc": 10.0,
        "v_observed": 50.0,
        "dim_state": 3.0,
        "notes": "Dwarf spiral"
    },
    
    # --- ULTRA-DIFFUSE GALAXIES (Partial 2D collapse) ---
    "Dragonfly 44": {
        "type": "ultra_diffuse",
        "M_baryonic": 4.0e39,        # ~2.7e9 solar masses
        "radius_kpc": 15.0,
        "v_observed": 47.0,
        "dim_state": 2.0,            # Partial collapse
        "notes": "Extreme ultra-diffuse, gas-poor"
    },
    
    "Dragonfly 17": {
        "type": "ultra_diffuse",
        "M_baryonic": 3.0e39,
        "radius_kpc": 12.0,
        "v_observed": 34.0,
        "dim_state": 2.0,
        "notes": "Ultra-diffuse, low surface brightness"
    },
    
    "VV 124 (UGC 731)": {
        "type": "ultra_diffuse",
        "M_baryonic": 5.0e38,        # Extremely low mass
        "radius_kpc": 8.0,
        "v_observed": 20.0,
        "dim_state": 2.0,
        "notes": "Faintest galaxy with HI"
    },
    
    # --- ELLIPTICAL GALAXIES (Different dynamics) ---
    "M87": {
        "type": "elliptical",
        "M_baryonic": 5.0e41,        # Very massive
        "radius_kpc": 50.0,
        "v_observed": 250.0,         # Velocity dispersion proxy
        "dim_state": 3.0,
        "notes": "Giant elliptical, supermassive BH"
    },
    
    # --- EDGE CASES ---
    "NGC 1052-DF2": {
        "type": "ultra_diffuse_no_dm",
        "M_baryonic": 1.0e39,
        "radius_kpc": 10.0,
        "v_observed": 35.0,          # Surprisingly high for its mass
        "dim_state": 2.0,
        "notes": "Ultra-diffuse with apparently no dark matter halo"
    },
}

# ============================================================================
# RUN VALIDATION
# ============================================================================

print("=" * 100)
print("BUOYANCY FRAMEWORK GALAXY VALIDATION")
print("=" * 100)
print()

# Test with Planck H0
print("Testing with H0 = 67.4 km/s/Mpc (Planck CMB):")
print()
framework_planck = BuoyancyFramework(H0_kmsMpc=67.4)
results_planck = framework_planck.test_galaxies(galaxy_data)

print(f"{'Galaxy':<25} | {'Type':<18} | {'Dim':<4} | {'Pred v':<10} | {'Obs v':<10} | {'Error %':<10} | {'Ghost Ratio':<12}")
print("-" * 120)

errors_planck = []
for r in results_planck:
    errors_planck.append(r['error_pct'])
    print(f"{r['name']:<25} | {r['type']:<18} | {r['dim_state']:<4.1f} | {r['v_predicted']:<10.2f} | {r['v_observed']:<10.2f} | {r['error_pct']:<10.2f} | {r['ghost_ratio']:<12.2f}")

print()
print(f"Mean Error (Planck H0):     {np.mean(errors_planck):.2f}%")
print(f"Median Error (Planck H0):   {np.median(errors_planck):.2f}%")
print(f"Std Dev Error (Planck H0):  {np.std(errors_planck):.2f}%")
print(f"Max Error (Planck H0):      {np.max(errors_planck):.2f}%")
print()
print()

# Test with local H0 (SH0ES)
print("Testing with H0 = 73.0 km/s/Mpc (SH0ES local measurement):")
print()
framework_local = BuoyancyFramework(H0_kmsMpc=73.0)
results_local = framework_local.test_galaxies(galaxy_data)

print(f"{'Galaxy':<25} | {'Type':<18} | {'Dim':<4} | {'Pred v':<10} | {'Obs v':<10} | {'Error %':<10} | {'Ghost Ratio':<12}")
print("-" * 120)

errors_local = []
for r in results_local:
    errors_local.append(r['error_pct'])
    print(f"{r['name']:<25} | {r['type']:<18} | {r['dim_state']:<4.1f} | {r['v_predicted']:<10.2f} | {r['v_observed']:<10.2f} | {r['error_pct']:<10.2f} | {r['ghost_ratio']:<12.2f}")

print()
print(f"Mean Error (SH0ES H0):     {np.mean(errors_local):.2f}%")
print(f"Median Error (SH0ES H0):   {np.median(errors_local):.2f}%")
print(f"Std Dev Error (SH0ES H0):  {np.std(errors_local):.2f}%")
print(f"Max Error (SH0ES H0):      {np.max(errors_local):.2f}%")
print()
print()

# ============================================================================
# ANALYSIS BY GALAXY TYPE
# ============================================================================

print("=" * 100)
print("BREAKDOWN BY GALAXY TYPE (Planck H0)")
print("=" * 100)
print()

types = {}
for r in results_planck:
    gtype = r['type']
    if gtype not in types:
        types[gtype] = []
    types[gtype].append(r['error_pct'])

for gtype in sorted(types.keys()):
    errs = types[gtype]
    print(f"{gtype:<25}: Mean={np.mean(errs):6.2f}%  Median={np.median(errs):6.2f}%  StdDev={np.std(errs):6.2f}%  N={len(errs)}")

print()
print("=" * 100)
print("KEY OBSERVATIONS")
print("=" * 100)
print("""
1. CHECK DIMENSIONALITY: Do ultra-diffuse galaxies (dim_state=2.0) predict better than spirals (dim_state=3.0)?

2. CHECK H0 SENSITIVITY: Does the model work better with one H0 value vs. another?
   - If SH0ES (73.0) works better, the model may be encoding local H0, not CMB H0.
   - If Planck (67.4) works better, the model is more aligned with the global cosmology.

3. CHECK SYSTEMATIC BIAS: Are all predictions systematically high or low?
   - If high: missing a damping factor or incorrect projection cost.
   - If low: missing an amplification or mismodeled dimensional state.

4. CHECK GALAXY-TYPE DEPENDENCE: Do certain galaxy types (spirals vs dwarfs vs ellipticals) have larger errors?
   - This may indicate the dimensional state assignment is wrong for some classes.
   - Or the model may need a mass-dependent correction.

5. CHECK OUTLIERS: Which galaxies have the largest errors?
   - NGC 1052-DF2 is known to have anomalously little dark matter — does the model catch this?
   - Ultra-diffuse systems should be better predicted if dim_state=2.0 is correct.

""")

print("=" * 100)
