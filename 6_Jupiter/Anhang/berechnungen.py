import numpy as np

# Konstante
G = 8.65e-4  # Gravitationskonstante in m^3 kg^-1 h^-2
d = 6.88e11  # Entfernung Erde-Jupiter in m

# Kalibrationsfaktor in °/mm
k = 0.0037

# Daten der Monde
mond_data = {
    "Io": {
        "distances_mm": np.array([6, 9, 19, 10, 9, 8, 7]),
        "times_hr": np.array([2, 4, 7, 8, 10, 11, 12])
    },
    "Europa": {
        "distances_mm": np.array([15, 17, 18, 18, 18, 4, 0.5]),
        "times_hr": np.array([2, 4, 7, 8, 10, 26, 30])
    },
    "Ganymed": {
        "distances_mm": np.array([1, 27, 8, 29, 31, 14, 8, 3]),
        "times_hr": np.array([5.167, 10.75, 30, 33.75, 51.333, 50.833, 54.75, 58.917])
    },
    "Kallisto": {
        "distances_mm": np.array([22, 40, 52, 54, 52, 26, 5, 1]),
        "times_hr": np.array([5.75, 5.167, 54, 50.833, 50.75, 54.75, 50.75, 58.167])
    }
}

def calculate_parameters(distances_mm, times_hr, k, G, d):
    # Umrechnung in Winkel in Grad
    angles_deg = distances_mm * k

    # Größte Elongation
    x0 = np.max(angles_deg)

    # Punkte links und rechts des Maximums
    x1 = angles_deg[0]
    x2 = angles_deg[-1]

    # Berechnung der Winkel θ1 und θ2
    theta1 = np.degrees(np.arccos(x1 / x0))
    theta2 = np.degrees(np.arccos(x2 / x0))

    # Delta θ und Delta t
    delta_theta = theta1 + theta2
    delta_t = times_hr[-1] - times_hr[0]

    # Berechnung der Orbitalperiode T
    T = 360 * (delta_t / delta_theta)

    # Berechnung des Bahnradius r
    alpha_rad = np.radians(x0)
    r = d * np.tan(alpha_rad)

    # Berechnung der Jupitermasse M
    M = (4 * np.pi**2 * r**3) / (G * T**2)
    
    return {
        "Max Elongation (x0) (deg)": x0,
        "Theta1 (deg)": theta1,
        "Theta2 (deg)": theta2,
        "Delta Theta (deg)": delta_theta,
        "Delta T (hr)": delta_t,
        "Orbitalperiode T (hr)": T,
        "Bahnradius r (m)": r,
        "Jupitermasse M (kg)": M
    }

# Berechnungen für jeden Mond
results = {}
for mond, data in mond_data.items():
    results[mond] = calculate_parameters(data["distances_mm"], data["times_hr"], k, G, d)

# Ausgabe der Ergebnisse
for mond, result in results.items():
    print(f"Ergebnisse für {mond}:")
    for key, value in result.items():
        print(f"{key}: {value}")
    print("\n")

# Durchschnittliche Jupitermasse berechnen
M_avg = np.mean([result["Jupitermasse M (kg)"] for result in results.values()])
print(f"Durchschnittliche Jupitermasse: {M_avg:.2e} kg")
