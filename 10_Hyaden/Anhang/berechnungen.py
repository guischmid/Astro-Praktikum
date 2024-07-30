import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Daten aus Tabelle 10.1
bv_main_sequence = np.array([-0.35, -0.31, -0.16, 0.00, 0.13, 0.27, 0.42, 0.58, 0.70, 0.89, 1.18, 1.45, 1.63, 1.80])
Mv_main_sequence = np.array([-5.8, -4.1, -1.1, 0.7, 2.0, 2.6, 3.4, 4.4, 5.1, 5.9, 7.3, 9.0, 11.8, 16.0])

# Daten aus Tabelle 10.2
bv_hyades = np.array([0.14, 0.15, 0.16, 0.19, 0.22, 0.23, 0.26, 0.29, 0.35, 0.41, 0.43, 0.46, 0.55, 0.64, 0.67, 0.74,
                      0.76, 0.83, 0.87, 0.93, 0.94, 0.98, 0.99, 1.00, 1.01, 1.13])
mv_hyades = np.array([4.21, 4.80, 4.63, 3.41, 5.09, 5.28, 5.37, 5.57, 5.95, 6.30, 6.58, 6.95, 7.75, 8.05, 8.28, 8.58,
                      8.57, 8.93, 9.10, 9.48, 3.84, 3.76, 3.65, 9.81, 3.53, 10.47])

# Farben-Helligkeits-Diagramm
plt.figure(figsize=(10, 6))
plt.scatter(bv_main_sequence, Mv_main_sequence, color='blue', label='Hauptreihensterne (MV)')
plt.scatter(bv_hyades, mv_hyades, color='red', label='Hyaden-Sterne (mV)')

# Achsenbeschriftung und Titel
plt.xlabel('B−V')
plt.ylabel('Helligkeit (MV, mV)')
plt.title('Farben-Helligkeits-Diagramm (FHD)')
plt.gca().invert_yaxis()  # Helligkeit nach unten ansteigend
plt.legend()
plt.grid(True)

# Berechnung der Ausgleichsgeraden im Bereich [0.5, 1.0]
mask_main_sequence = (bv_main_sequence >= 0.5) & (bv_main_sequence <= 1.0)
mask_hyades = (bv_hyades >= 0.5) & (bv_hyades <= 1.0)

bv_main_seq_fit = bv_main_sequence[mask_main_sequence].reshape(-1, 1)
Mv_main_seq_fit = Mv_main_sequence[mask_main_sequence]

bv_hyades_fit = bv_hyades[mask_hyades].reshape(-1, 1)
mv_hyades_fit = mv_hyades[mask_hyades]

# Hauptreihensterne Ausgleichsgerade
model_main_seq = LinearRegression().fit(bv_main_seq_fit, Mv_main_seq_fit)
y_fit_main_seq = model_main_seq.predict(bv_main_seq_fit)
plt.plot(bv_main_seq_fit, y_fit_main_seq, color='blue', linestyle='--')

# Hyaden-Sterne Ausgleichsgerade
model_hyades = LinearRegression().fit(bv_hyades_fit, mv_hyades_fit)
y_fit_hyades = model_hyades.predict(bv_hyades_fit)
plt.plot(bv_hyades_fit, y_fit_hyades, color='red', linestyle='--')

# Berechnung des Entfernungsmoduls m - M
m_minus_M = model_hyades.intercept_ - model_main_seq.intercept_

# Verschiebung der Hyaden-Sterne um m - M
mv_hyades_corrected = mv_hyades - m_minus_M

# Neue Darstellung der Hyaden-Sterne nach Korrektur
plt.scatter(bv_hyades, mv_hyades_corrected, color='green', label='Hyaden-Sterne (verschoben)')
plt.legend()

# Abknickpunkte und waagerechte Linien einzeichnen
abknickpunkte_mv = np.array([-3.0, -2.1, -1.6, -1.2, -0.9, -0.2, 1.7, 2.0, 2.8, 3.7, 4.2, 4.5, 4.8])
for abknick in abknickpunkte_mv:
    plt.axhline(y=abknick, color='gray', linestyle=':')

plt.show()

# Entfernung d des Hyaden-Haufens
d_pc = 10**((m_minus_M + 5)/5)

# Ausgabe der Entfernung
print(f"Entfernungsmodul (m - M): {m_minus_M:.2f}")
print(f"Entfernung d: {d_pc:.2f} pc")
