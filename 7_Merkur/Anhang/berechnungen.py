import numpy as np

# Konstante
c = 3e8  # Lichtgeschwindigkeit in m/s
R = 2.44e6  # Radius des Merkurs in m

# Abstände der Maxima in mm, Zeiten in µs und Kalibration in Hz/mm
maxima_data = {
    "times_us": np.array([120, 210, 300, 390]),
    "left_max_mm": np.array([9.85, 8.21, 7.66, 8.21]),
    "right_max_mm": np.array([56.93, 60.22, 62.96, 59.12]),
    "left_max_hz": np.array([1.27, 1.06, 1.00, 1.06]),
    "right_max_hz": np.array([7.35, 7.75, 8.13, 7.56])
}

# Umrechnung von Zeit in µs zu d in m
times_s = maxima_data["times_us"] * 1e-6  # in Sekunden
d_values = 0.5 * times_s * c  # in Metern

# Berechnung der geometrischen Größen x und y
x_values = R - d_values
y_values = np.sqrt(R**2 - x_values**2)

# Frequenzverschiebung ∆f
f = 430e6  # Originalfrequenz in Hz
delta_f_values = 0.5 * (maxima_data["right_max_hz"] + maxima_data["left_max_hz"])

# Berechnung der Radialgeschwindigkeit v0
v0_values = (delta_f_values / f) * c

# Berechnung der Geschwindigkeit v
v_values = (R / y_values) * v0_values

# Berechnung der Rotationsperiode P
P_values = 2 * np.pi * R / v_values

# Ausgabe der Ergebnisse
results = {
    "Versatz d (m)": d_values,
    "Geometrische Größen x (m)": x_values,
    "Geometrische Größen y (m)": y_values,
    "Radialgeschwindigkeit v0 (m/s)": v0_values,
    "Geschwindigkeit v (m/s)": v_values,
    "Rotationsperiode P (s)": P_values
}

for key, value in results.items():
    print(f"{key}: {value}")

# Durchschnittliche Rotationsperiode
P_avg = np.mean(P_values)
print(f"Durchschnittliche Rotationsperiode: {P_avg:.2f} s")
