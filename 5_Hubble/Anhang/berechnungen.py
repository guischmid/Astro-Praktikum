
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Gegebene Ruhewellenlängen der He I-Linien in Å
lambda_a = 3888.7
lambda_b = 3964.7
lambda_c = 4026.2
lambda_d = 4143.8
lambda_e = 4471.5
lambda_f = 4713.1
lambda_g = 5015.7

# Gemessene Abstände der He I-Linien zur Linie a in mm
abstaende_ab = 4
abstaende_ac = 7
abstaende_ad = 14
abstaende_ae = 35
abstaende_af = 49#
abstaende_ag = 68

# Länge des Maßstabs in mm für 150″
masstab_winkel = 150  # Bogensekunden
masstab_laenge = 22  # mm

# Berechnung der Dispersion für jede Linie
dispersion_b = (lambda_b - lambda_a) / abstaende_ab
dispersion_c = (lambda_c - lambda_a) / abstaende_ac
dispersion_d = (lambda_d - lambda_a) / abstaende_ad
dispersion_e = (lambda_e - lambda_a) / abstaende_ae
dispersion_f = (lambda_f - lambda_a) / abstaende_af
dispersion_g = (lambda_g - lambda_a) / abstaende_ag

# Mittelung der Dispersion
dispersion_mittel = np.mean([dispersion_b, dispersion_c, dispersion_d, dispersion_e, dispersion_f, dispersion_g])

# Ruhewellenlängen der Ca II Linien
lambda_K_0 = 3933.7  # Å
lambda_H_0 = 3968.5  # Å

# Gemessene Abstände der K- und H-Linien zu a (in mm)
abstaende_K_H = {
    'Virgo': (4, 5),
    'Ursa Major': (14, 17),
    'Corona Borealis': (21, 24),
    'Bootes': (33, 36),
    'Hydra': (51, 53)
}

# Berechnung der beobachteten Wellenlängen λ_K und λ_H
def berechne_beobachtete_wellenlaenge(abstand, lambda_0):
    return lambda_0 + abstand * dispersion_mittel

# Berechnung der Fluchtgeschwindigkeit
def berechne_fluchtgeschwindigkeit(lambda_beobachtet, lambda_0):
    c = 3 * 10**5  # Lichtgeschwindigkeit in km/s
    return c * (lambda_beobachtet - lambda_0) / lambda_0

# Ergebnisse speichern
fluchtgeschwindigkeiten = {}

# Berechnungen durchführen
for galaxie, (abstand_K, abstand_H) in abstaende_K_H.items():
    lambda_K = berechne_beobachtete_wellenlaenge(abstand_K, lambda_K_0)
    lambda_H = berechne_beobachtete_wellenlaenge(abstand_H, lambda_H_0)
    
    v_K = berechne_fluchtgeschwindigkeit(lambda_K, lambda_K_0)
    v_H = berechne_fluchtgeschwindigkeit(lambda_H, lambda_H_0)
    
    # Mittelwert der Fluchtgeschwindigkeiten
    v_mittel = np.mean([v_K, v_H])
    fluchtgeschwindigkeiten[galaxie] = v_mittel

# Gegebener Maßstab: 150″ entsprechen 22 mm
masstab_winkel = 150  # Bogensekunden
masstab_laenge = 22  # mm

# Umrechnung in Bogensekunden pro mm
winkel_pro_mm = masstab_winkel / masstab_laenge

# Gemessene Durchmesser in mm
durchmesser_mm = {
    'Virgo': 19,
    'Ursa Major': 5,
    'Corona Borealis': 3,
    'Bootes': 1,
    'Hydra': 1
}

# Gegebener tatsächlicher Durchmesser der Galaxien
s = 0.02  # Mpc

# Berechnung der Durchmesser in Bogensekunden und der Entfernung d
def berechne_entfernung(durchmesser_mm, winkel_pro_mm):
    alpha = durchmesser_mm * winkel_pro_mm  # Durchmesser in Bogensekunden
    alpha_rad = np.deg2rad(alpha / 3600)  # Umrechnung in Radiant
    d = s / np.tan(alpha_rad)  # Entfernung in Mpc
    return d

entfernungen = {}

for galaxie, dm_mm in durchmesser_mm.items():
    d = berechne_entfernung(dm_mm, winkel_pro_mm)
    entfernungen[galaxie] = d

# Hubble-Diagramm erstellen
d_values = np.array(list(entfernungen.values())).reshape(-1, 1)
v_values = np.array(list(fluchtgeschwindigkeiten.values()))

# Lineare Regression zur Bestimmung der Hubble-Konstanten
model = LinearRegression().fit(d_values, v_values)
hubble_konstante = model.coef_[0]

# Weltalter T und Weltradius D berechnen
c = 3 * 10**5  # Lichtgeschwindigkeit in km/s
T = 1 / hubble_konstante  # Weltalter in Gyr (Gigajahren)
D = c / hubble_konstante  # Weltradius in Mpc

# Erstellen des Hubble-Diagramms
plt.scatter(d_values, v_values, label='Datenpunkte')
plt.plot(d_values, model.predict(d_values), color='red', label='Ausgleichsgerade')
plt.xlabel('Entfernung (Mpc)')
plt.ylabel('Fluchtgeschwindigkeit (km/s)')
plt.title('Hubble-Diagramm')
plt.legend()
plt.grid(True)
#plt.savefig('/mnt/data/hubble_diagram.png')
plt.show()

# Ergebnisse
print("Hubble-Konstante:", hubble_konstante)
print("Weltalter (Gyr):", T)
print("Weltradius (Mpc):", D)
