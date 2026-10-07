import numpy as np

class UCF11RefinementTest:
    def __init__(self, h0_km_s_mpc=67.4):
        self.c = 2.9979e8
        self.G = 6.6743e-11
        self.H0 = h0_km_s_mpc * 1000.0 / 3.086e22

        self.ln14 = np.log(14.0)
        self.packing_density = np.pi / np.sqrt(18.0)
        self.delta_n = 36.0
        self.eta = (self.ln14 / (self.packing_density * self.delta_n)) * 2.0

        self.a_buoyant = (1.0 / (1.0 - self.eta)) * (self.c * self.H0) / (2.0 * np.pi)
        self.k_factor = 1.0 + self.eta

    def enclosed_mass_fraction(self, r_kpc, R_scale):
        return 1.0 - (1.0 + r_kpc / R_scale) * np.exp(-r_kpc / R_scale)

    def compute_mode_1(self, M_total, r_kpc):
        """Point-mass, geometric mean coupling"""
        r_m = r_kpc * 3.086e19
        a_N = (self.G * M_total) / (r_m**2)
        a_E = np.sqrt(a_N * self.a_buoyant)
        v = np.sqrt(a_E * r_m) / 1000.0
        return v

    def compute_mode_2(self, M_total, r_kpc, R_scale=4.6):
        """Distributed-mass envelope, geometric mean coupling"""
        r_m = r_kpc * 3.086e19
        frac = self.enclosed_mass_fraction(r_kpc, R_scale)
        M_enclosed = M_total * frac
        a_N = (self.G * M_enclosed) / (r_m**2)
        a_E = np.sqrt(a_N * self.a_buoyant)
        v = np.sqrt(a_E * r_m) / 1000.0
        return v

    def compute_mode_3(self, M_total, r_kpc, R_scale=4.6):
        """Distributed-mass envelope, coupled-field refinement"""
        r_m = r_kpc * 3.086e19
        frac = self.enclosed_mass_fraction(r_kpc, R_scale)
        M_enclosed = M_total * frac
        a_N = (self.G * M_enclosed) / (r_m**2)
        a_E = np.sqrt(a_N**2 + self.k_factor * self.a_buoyant * a_N)
        v = np.sqrt(a_E * r_m) / 1000.0
        return v


# Galaxy dataset with measured scale radii
galaxy_data = {
    "Milky Way": {
        "type": "spiral",
        "M_baryonic": 1.0e41,
        "radius_kpc": 26.0,
        "v_observed": 230.0,
        "R_scale": 3.5,  # disk scale length
    },
    "Andromeda": {
        "type": "spiral",
        "M_baryonic": 1.5e41,
        "radius_kpc": 32.0,
        "v_observed": 225.0,
        "R_scale": 5.0,
    },
    "NGC 3198": {
        "type": "spiral",
        "M_baryonic": 4.0e40,
        "radius_kpc": 25.0,
        "v_observed": 165.0,
        "R_scale": 4.0,
    },
    "NGC 2841": {
        "type": "spiral",
        "M_baryonic": 8.0e40,
        "radius_kpc": 28.0,
        "v_observed": 180.0,
        "R_scale": 4.5,
    },
    "DDO 154": {
        "type": "dwarf",
        "M_baryonic": 1.0e39,
        "radius_kpc": 8.0,
        "v_observed": 40.0,
        "R_scale": 2.0,
    },
    "NGC 2976": {
        "type": "dwarf",
        "M_baryonic": 2.0e39,
        "radius_kpc": 10.0,
        "v_observed": 50.0,
        "R_scale": 2.5,
    },
    "Dragonfly 44": {
        "type": "ultra_diffuse",
        "M_baryonic": 4.0e39,
        "radius_kpc": 15.0,
        "v_observed": 47.0,
        "R_scale": 8.0,  # much larger scale for diffuse systems
    },
    "Dragonfly 17": {
        "type": "ultra_diffuse",
        "M_baryonic": 3.0e39,
        "radius_kpc": 12.0,
        "v_observed": 34.0,
        "R_scale": 7.0,
    },
    "VV 124": {
        "type": "ultra_diffuse",
        "M_baryonic": 5.0e38,
        "radius_kpc": 8.0,
        "v_observed": 20.0,
        "R_scale": 5.0,
    },
    "M87": {
        "type": "elliptical",
        "M_baryonic": 5.0e41,
        "radius_kpc": 50.0,
        "v_observed": 250.0,
        "R_scale": 10.0,  # ellipticals have extended profiles
    },
    "NGC 1052-DF2": {
        "type": "ultra_diffuse",
        "M_baryonic": 1.0e39,
        "radius_kpc": 10.0,
        "v_observed": 35.0,
        "R_scale": 6.0,
    },
}


def run_comparison():
    print("=" * 130)
    print("UCF-11 REFINEMENT COMPARISON: THREE MODES")
    print("=" * 130)
    print()

    for h0_label, h0_val in [("Planck (67.4)", 67.4), ("Local (73.0)", 73.0)]:
        print(f"\n{'='*130}")
        print(f"Testing with H0 = {h0_label} km/s/Mpc")
        print(f"{'='*130}\n")

        test = UCF11RefinementTest(h0_km_s_mpc=h0_val)

        print(
            f"{'Galaxy':<20} | {'Type':<15} | "
            f"{'Mode 1 (v)':<12} | {'Mode 1 (err%)':<12} | "
            f"{'Mode 2 (v)':<12} | {'Mode 2 (err%)':<12} | "
            f"{'Mode 3 (v)':<12} | {'Mode 3 (err%)':<12} | "
            f"{'Obs v':<10}"
        )
        print("-" * 130)

        results_by_mode = {1: [], 2: [], 3: []}
        results_by_type = {"spiral": {}, "dwarf": {}, "ultra_diffuse": {}, "elliptical": {}}

        for name, data in galaxy_data.items():
            M = data["M_baryonic"]
            r = data["radius_kpc"]
            v_obs = data["v_observed"]
            R_scale = data["R_scale"]
            gtype = data["type"]

            # Compute all three modes
            v1 = test.compute_mode_1(M, r)
            err1 = abs(v1 - v_obs) / v_obs * 100.0

            v2 = test.compute_mode_2(M, r, R_scale)
            err2 = abs(v2 - v_obs) / v_obs * 100.0

            v3 = test.compute_mode_3(M, r, R_scale)
            err3 = abs(v3 - v_obs) / v_obs * 100.0

            results_by_mode[1].append(err1)
            results_by_mode[2].append(err2)
            results_by_mode[3].append(err3)

            if gtype not in results_by_type[gtype]:
                results_by_type[gtype] = {1: [], 2: [], 3: []}
            results_by_type[gtype][1].append(err1)
            results_by_type[gtype][2].append(err2)
            results_by_type[gtype][3].append(err3)

            print(
                f"{name:<20} | {gtype:<15} | "
                f"{v1:<12.2f} | {err1:<12.2f} | "
                f"{v2:<12.2f} | {err2:<12.2f} | "
                f"{v3:<12.2f} | {err3:<12.2f} | "
                f"{v_obs:<10.2f}"
            )

        # Summary statistics
        print()
        print("SUMMARY BY MODE (all galaxies):")
        print("-" * 130)
        for mode in [1, 2, 3]:
            errs = results_by_mode[mode]
            print(
                f"Mode {mode}: Mean={np.mean(errs):6.2f}% | Median={np.median(errs):6.2f}% | "
                f"Max={np.max(errs):6.2f}% | Min={np.min(errs):6.2f}% | StdDev={np.std(errs):6.2f}%"
            )

        print()
        print("SUMMARY BY GALAXY TYPE:")
        print("-" * 130)
        for gtype in sorted(results_by_type.keys()):
            type_results = results_by_type[gtype]
            if any(type_results.values()):
                print(f"\n{gtype.upper()}:")
                for mode in [1, 2, 3]:
                    if type_results[mode]:
                        errs = type_results[mode]
                        print(
                            f"  Mode {mode}: Mean={np.mean(errs):6.2f}% | Median={np.median(errs):6.2f}% | Max={np.max(errs):6.2f}%"
                        )

        print()
        print("WHICH MODE WINS BY GALAXY TYPE:")
        print("-" * 130)
        for gtype in sorted(results_by_type.keys()):
            type_results = results_by_type[gtype]
            if any(type_results.values()):
                means = {m: np.mean(type_results[m]) if type_results[m] else 999 for m in [1, 2, 3]}
                best_mode = min(means, key=means.get)
                print(f"{gtype:<20}: Mode {best_mode} wins (mean error {means[best_mode]:.2f}%)")


if __name__ == "__main__":
    run_comparison()
