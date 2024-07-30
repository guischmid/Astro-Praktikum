import matplotlib.pyplot as plt
import numpy as np

# Gegebene Daten für Cepheiden
cepheids = [
    {"P": 10, "m_max": 12.0, "m_min": 14.0},
    {"P": 5, "m_max": 14.5, "m_min": 16.5},
    {"P": 8, "m_max": 13.0, "m_min": 15.0},
    {"P": 12, "m_max": 11.5, "m_min": 13.5},
]

# Berechnung der mittleren Helligkeit m und des logarithmischen Werts logP
logP = []
m = []
for c in cepheids:
    m_avg = (c["m_max"] + c["m_min"]) / 2
    logP.append(np.log10(c["P"]))
    m.append(m_avg)

# Ausgleichsgeraden für m und M
m_slope = -2.5616
m_intercept = 17.0710
M_slope = -3.5160
M_intercept = -0.6008

# Berechnung der Werte
logP_values = np.linspace(min(logP), max(logP), 100)
m_values = m_slope * logP_values + m_intercept
M_values = M_slope * logP_values + M_intercept

# Plotten des logP-m-Diagramms
plt.figure(figsize=(10, 6))
plt.plot(logP, m, 'o', label='Beobachtete Cepheiden (m)')
plt.plot(logP_values, m_values, '-', label='Ausgleichsgerade (m)')
plt.plot(logP_values, M_values, '--', label='Ausgleichsgerade (M)')
plt.xlabel('logP')
plt.ylabel('Helligkeit (m, M)')
plt.title('logP-m-Diagramm für Cepheiden')
plt.legend()
plt.grid(True)
plt.show()