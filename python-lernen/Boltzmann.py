import numpy as np
import matplotlib.pyplot as plt

def softmax(logits, T):
    """Berechnet die Boltzmann-Verteilung für ein Array von Werten."""
    exp_logits = np.exp(np.array(logits) / T)
    return exp_logits / np.sum(exp_logits)

# Beispiel-Energiezustände (oder KI-Logits)
logits = [5, 4, 3, 2, 1]
labels = [f"Zustand {i}" for i in range(len(logits))]

# Verschiedene Temperaturen definieren
temperatures = [0.2, 1.0, 5.0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(10, 6))

for T, color in zip(temperatures, colors):
    probs = softmax(logits, T)
    plt.plot(labels, probs, marker='o', linestyle='-', color=color,
             label=f'Temperatur T = {T}')

plt.title('Einfluss der Temperatur auf die Boltzmann-Verteilung')
plt.ylabel('Wahrscheinlichkeit P(i)')
plt.xlabel('Energiezustände (höhere Werte = niedrigere Energie)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()