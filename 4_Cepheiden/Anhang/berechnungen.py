import numpy as np
import matplotlib.pyplot as plt

# Daten aus Tabelle 4.1 (Scheinbare Helligkeiten)
tab41_data = [
    {"logP": 1.52, "m": 13.4}, {"logP": 0.35, "m": 16.3}, {"logP": 1.44, "m": 13.8},
    {"logP": 0.45, "m": 16.1}, {"logP": 0.63, "m": 15.6}, {"logP": 1.63, "m": 13.1},
    {"logP": 1.11, "m": 14.7}, {"logP": 1.70, "m": 13.1}, {"logP": 1.22, "m": 13.8},
    {"logP": 0.71, "m": 15.6}, {"logP": 0.81, "m": 15.2}, {"logP": 0.50, "m": 16.0},
    {"logP": 0.21, "m": 16.8}, {"logP": 0.30, "m": 16.7}, {"logP": 0.41, "m": 16.0},
    {"logP": 1.01, "m": 14.3}, {"logP": 1.60, "m": 13.6}
]

# Daten aus Tabelle 4.2 (Absolute Helligkeiten)
tab42_data = [
    {"logP": 0.86, "M": -3.5}, {"logP": 0.65, "M": -3.1}, {"logP": 0.90, "M": -3.7},
    {"logP": 0.69, "M": -3.4}, {"logP": 1.17, "M": -4.5}, {"logP": 0.90, "M": -3.7},
    {"logP": 0.29, "M": -1.7}, {"logP": 0.58, "M": -2.8}, {"logP": 0.64, "M": -2.8},
    {"logP": 1.04, "M": -4.1}, {"logP": 0.81, "M": -3.4}, {"logP": 1.34, "M": -5.6},
    {"logP": 0.73, "M": -3.0}, {"logP": 0.99, "M": -3.7}, {"logP": 1.23, "M": -5.3},
    {"logP": 0.49, "M": -2.4}, {"logP": 0.56, "M": -2.4}, {"logP": 0.83, "M": -3.5},
    {"logP": 0.71, "M": -3.0}, {"logP": 1.65, "M": -6.4}
]

# Extrahieren der logP und m/M Werte
logP_tab41 = [cepheid["logP"] for cepheid in tab41_data]
m_tab41 = [cepheid["m"] for cepheid in tab41_data]

logP_tab42 = [cepheid["logP"] for cepheid in tab42_data]
M_tab42 = [cepheid["M"] for cepheid in tab42_data]

# Berechnung der Ausgleichsgeraden
m_slope_correct = -2.46
m_intercept_correct = 17.21
M_slope_correct = -3.52
M_intercept_correct = 0.60

extended_logP_values = np.linspace(0.2, 1.8, 100)
m_values_extended = m_slope_correct * extended_logP_values + m_intercept_correct
M_values_extended = M_slope_correct * extended_logP_values + M_intercept_correct

# Plot
plt.figure(figsize=(10, 6))

# Messwerte von Tab. 4.1 und Tab. 4.2
plt.scatter(logP_tab41, m_tab41, label='Messwerte (Tab. 4.1)', color='red')
plt.scatter(logP_tab42, M_tab42, label='Messwerte (Tab. 4.2)', color='blue')

# Plot der Ausgleichsgeraden
plt.plot(extended_logP_values, m_values_extended, '-', label='Ausgleichsgerade m1', color='orange')
plt.plot(extended_logP_values, M_values_extended, '-', label='Ausgleichsgerade m2', color='green')

# Achsenbeschriftung und Titel
plt.xlabel('logP')
plt.ylabel('Helligkeit (m, M)')
plt.ylim(-7, 17)
plt.title('logP-m-Diagramm für Cepheiden')
plt.legend()
plt.grid(True)

plt.show()
