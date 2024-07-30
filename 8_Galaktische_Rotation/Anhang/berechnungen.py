import numpy as np
import matplotlib.pyplot as plt

# Konstante
R0 = 8.5  # kpc, Sonnenabstand zum galaktischen Zentrum
omega0 = 220 / R0  # km/s/kpc, angenommene Rotationsgeschwindigkeit der Sonne

# Gemessene Abstände der Maxima in mm aus den bereitgestellten Daten
abstaende_links_mm = np.array([0, 0, 0, 4, 4, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9, 8, 5, 5, 5, 7, 6, 7, 6, 6, 5, 6, 5, 5, 4, 4, 3, 2.5, 2, 1, 0, 0])
abstaende_rechts_mm = np.array([0, 1, 1, 2, 2, 5, 6, 6, 2, 5, 3, 2.5, 2, 2, 1, 1.1, 1, 0.5, 0.5, 0, 0, 0, 3, 2, 3, 5.5, 5, 5, 5, 0, 0, 0])

# Kalibrationsfaktor: 200 km/s entspricht 24 mm
kalibration_faktor = 200 / 24  # km/s pro mm

# Umrechnung der Abstände in km/s
v_rel_links = -abstaende_links_mm * kalibration_faktor
v_rel_rechts = abstaende_rechts_mm * kalibration_faktor

# Winkel l in Grad (angepasst an die Anzahl der Messungen)
l_deg_links = np.linspace(3.1, 179.8, len(abstaende_links_mm))
l_deg_rechts = np.linspace(184.8, 328.5, len(abstaende_rechts_mm))

# Winkel in Radiant umrechnen
l_rad_links = np.radians(l_deg_links)
l_rad_rechts = np.radians(l_deg_rechts)

# Berechnung der Differenz der Winkelgeschwindigkeiten ω1 - ω0
# Hier wird ein Problem vermieden, wenn sin(l) = 0
sin_l_links = np.sin(l_rad_links)
sin_l_rechts = np.sin(l_rad_rechts)

# Vermeidung von Division durch Null
delta_omega_links = np.divide(v_rel_links, (R0 * sin_l_links), out=np.zeros_like(v_rel_links), where=sin_l_links!=0)
delta_omega_rechts = np.divide(v_rel_rechts, (R0 * sin_l_rechts), out=np.zeros_like(v_rel_rechts), where=sin_l_rechts!=0)

# Berechnung der Winkelgeschwindigkeit ω1
omega1_links = delta_omega_links + omega0
omega1_rechts = delta_omega_rechts + omega0

# Bestimmung der Zentrumsabstände R1
R1_links = np.divide(R0 * sin_l_links, delta_omega_links, out=np.zeros_like(sin_l_links), where=delta_omega_links!=0)
R1_rechts = np.divide(R0 * sin_l_rechts, delta_omega_rechts, out=np.zeros_like(sin_l_rechts), where=delta_omega_rechts!=0)

# Umrechnung in kartesische Koordinaten
r_links = R0 * np.cos(l_rad_links) + np.sqrt(np.maximum(R1_links**2 - R0**2 * sin_l_links**2, 0))
r_rechts = R0 * np.cos(l_rad_rechts) + np.sqrt(np.maximum(R1_rechts**2 - R0**2 * sin_l_rechts**2, 0))

x_links = r_links * np.cos(np.radians(l_deg_links + 90))
y_links = r_links * np.sin(np.radians(l_deg_links + 90))

x_rechts = r_rechts * np.cos(np.radians(l_deg_rechts + 90))
y_rechts = r_rechts * np.sin(np.radians(l_deg_rechts + 90))

# Plotten des Diagramms
plt.figure(figsize=(8, 8))
plt.plot(x_links, y_links, 'bo-', label='Position der H I-Wolken (0° < l < 180°)')
plt.plot(x_rechts, y_rechts, 'ro-', label='Position der H I-Wolken (180° < l < 360°)')
plt.xlabel('x (kpc)')
plt.ylabel('y (kpc)')
plt.title('Verteilung der H I-Wolken in der Milchstraße')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
