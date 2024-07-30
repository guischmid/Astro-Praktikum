import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Umrechnung von Polarkoordinaten in kartesische Koordinaten
def pol2cart(alpha, l):
    # np.cos und np.sin erwarten radian, deshalb umrechnen
    x = l * np.cos(np.radians(np.array(alpha) + 90))
    y = l * np.sin(np.radians(np.array(alpha) + 90))
    return x, y

# Daten aus den Abbildungen 11.6 und 11.7
daten = {
    "Abbildung 11.6": {
        "jahre": [1968, 1970, 1972, 1974, 1976],
        "winkel": [325, 286, 260, 215, 200],
        "abstaende_mm": [18, 18, 19, 21, 23],
        "kalibration": 23
    },
    "Abbildung 11.7": {
        "jahre": [1933 + 295/365, 1938 + 321/365, 1944 + 200/365, 1948 + 339/365, 1955 + 274/365, 1962 + 335/365, 1965 + 322/365],
        "winkel": [335, 300, 280, 275, 240, 210, 160],
        "abstaende_mm": [5, 10, 10, 11, 10, 5, 4],
        "kalibration": 33
    }
}

# Berechnung der Abstände in Bogensekunden
for key in daten:
    kalibration = daten[key]["kalibration"]
    abstaende_mm = np.array(daten[key]["abstaende_mm"])
    daten[key]["abstaende_arcsec"] = abstaende_mm * (kalibration / np.max(abstaende_mm))

# Plotten der Datenpunkte
plt.figure(figsize=(8, 8))
for key in daten:
    winkel = daten[key]["winkel"]
    abstaende_arcsec = daten[key]["abstaende_arcsec"]
    x, y = pol2cart(winkel, abstaende_arcsec)
    plt.plot(x, y, 'o-', label=key)

# Einstellungen für das Diagramm
plt.xlabel('x (arcsec)')
plt.ylabel('y (arcsec)')
plt.title('Bewegung der Komponenten in KR 60AB')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
