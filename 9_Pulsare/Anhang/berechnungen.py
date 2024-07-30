import numpy as np

# Konstanten
alpha = 4148.8  # cm^3 pc^-1 MHz^2 s
skalierung = 2.9  # mm pro Sekunde
ne = 0.02  # Elektronendichte in cm^-3

# Frequenzen der Radiopulse in MHz
frequenzen = {
    "PSR B0809+74": [234, 256, 405],
    "PSR B0950+08": [234, 256, 405],
    "PSR B0329+54": [234, 256, 405, 1420]
}

# Abstände der Pulse in mm innerhalb einer Frequenz
pulse_abstaende_mm = {
    "PSR B0809+74": 35,
    "PSR B0950+08": 7,
    "PSR B0329+54": 20
}

# Verschiebungen in mm
verschiebungen_mm = {
    "PSR B0809+74": [-2, -8],
    "PSR B0950+08": [-1.5, 1.5],
    "PSR B0329+54": [-10, -9, -8]
}

# Umrechnung der Abstände in Sekunden (Perioden P)
pulse_perioden_s = {pulsar: abstand * (1/skalierung) for pulsar, abstand in pulse_abstaende_mm.items()}

# Umrechnung der Verschiebungen in Sekunden
verschiebungen_s = {pulsar: [v * (1/skalierung) for v in verschiebungen] for pulsar, verschiebungen in verschiebungen_mm.items()}

# Ausgabe der berechneten Perioden
for pulsar, periode in pulse_perioden_s.items():
    print(f"Pulsar: {pulsar} -> Periode P = {periode:.3f} s")

# Berechnung des Dispersionsmaßes ned und der Entfernung d
for pulsar, freqs in frequenzen.items():
    print(f"Pulsar: {pulsar}")
    ned_values = []
    for i in range(len(freqs) - 1):
        va = freqs[i]
        vb = freqs[i + 1]
        delta_t = verschiebungen_s[pulsar][i]
        inv_freq_term = (1 / va**2 - 1 / vb**2)
        ned = delta_t / (alpha * inv_freq_term)
        ned_values.append(ned)
        print(f"  Frequenzen: {va} MHz, {vb} MHz -> ned = {ned:.3f} pccm^-3")
    
    # Mittelwert des Dispersionsmaßes
    mean_ned = np.mean(ned_values)
    print(f"  Mittelwert des Dispersionsmaßes ned = {mean_ned:.3f} pccm^-3")
    
    # Berechnung der Entfernung d
    distance = mean_ned / ne
    print(f"  Entfernung d = {distance:.1f} pc\n")
