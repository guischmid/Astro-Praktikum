
import numpy as np

# Gegebene Daten aus der Tabelle 3.1
data = {
    'nr': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'parallax_arcsec': [0.182, 0.028, 0.123, 0.292, 0.108, 0.056, 0.014, 0.077, 0.179, 0.015, 0.303, 0.110, 0.013, 0.021],
    'mv': [3.6, 5.4, 0.1, 5.2, 3.5, 2.1, 2.8, 4.2, 4.7, 3.8, 3.8, 5.5, 4.0, 2.9],
    'lk': ['V', 'III', 'V', 'V', 'IV', 'III', 'I', 'V', 'V', 'III', 'V', 'V', 'I', 'III']
}

# Berechnung der Entfernung in Parsec (pc) aus Parallaxe in Bogensekunden
def parallax_to_distance(parallax_arcsec):
    return 1 / parallax_arcsec

# Berechnung der absoluten Helligkeit M_V
def apparent_to_absolute_magnitude(mv, distance_pc):
    return mv + 5 - 5 * np.log10(distance_pc)

# Berechnung der bolometrischen Helligkeit M_bol
def calculate_mbol(Mv, BC):
    return Mv + BC

# Berechnung der Leuchtkraft L* in Einheiten der Sonnenleuchtkraft
def calculate_luminosity(Mbol_star, Mbol_sun):
    return 10**(-0.4 * (Mbol_star - Mbol_sun))

# Berechnung des Sternradius in Einheiten der Sonnenradien
def calculate_radius(L_star, Teff_star):
    Teff_sun = 5800  # Effektive Temperatur der Sonne in Kelvin
    return (L_star ** 0.5) * ((Teff_sun / Teff_star) ** 2)

# Konstanten
Mbol_sun = 4.74  # Bolometrische Helligkeit der Sonne

# Berechnung für jeden Stern
results = []

for i in range(len(data['nr'])):
    # Annahme: Spektralklasse und BC-Werte sind zu bestimmen
    parallax_arcsec = data['parallax_arcsec'][i]
    mv = data['mv'][i]
    lk = data['lk'][i]
    
    # Entfernung in Parsec
    distance_pc = parallax_to_distance(parallax_arcsec)
    
    # Absolute Helligkeit
    Mv = apparent_to_absolute_magnitude(mv, distance_pc)
    
    # Beispiel BC-Wert für Demonstration; tatsächlich basierend auf Spektralklasse bestimmen
    BC = -0.12  # Platzhalterwert, sollte basierend auf tatsächlicher Spektralklasse angepasst werden
    Mbol = calculate_mbol(Mv, BC)
    
    # Leuchtkraft in Sonnenleuchtkräften
    luminosity_star = calculate_luminosity(Mbol, Mbol_sun)
    
    # Annahme: Effektivtemperatur Teff_star für Spektralklasse (Platzhalter)
    Teff_star = 5800  # Beispielwert, tatsächliche Temperatur muss bestimmt werden
    radius_star = calculate_radius(luminosity_star, Teff_star)
    
    # Speichern der Ergebnisse
    results.append({
        'nr': data['nr'][i],
        'distance_pc': distance_pc,
        'Mv': Mv,
        'Mbol': Mbol,
        'luminosity_star': luminosity_star,
        'radius_star': radius_star
    })

# Ausgabe der Ergebnisse
for result in results:
    print(result)
