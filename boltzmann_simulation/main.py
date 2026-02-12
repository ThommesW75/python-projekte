import numpy as np
import matplotlib.pyplot as plt


def boltzmann_softmax(logits, temperature):
    """
    Berechnet die Boltzmann-Verteilung.
    Höhere Temperatur = flachere Verteilung (Zufall)
    Niedrige Temperatur = steilere Verteilung (Fokus auf Maximum)
    """
    logits = np.array(logits)
    # Formel: exp(logits / T) / sum(exp(logits / T))
    exp_logits = np.exp(logits / temperature)
    return exp_logits / np.sum(exp_logits)


def main():
    # Unsere Testdaten (z.B. verschiedene Optionen oder Energieniveaus)
    states = ['Zustand A', 'Zustand B', 'Zustand C', 'Zustand D', 'Zustand E']
    logits = [5.0, 4.0, 3.0, 2.0, 1.0]

    # Verschiedene Temperaturen zum Vergleich
    # 0.2: Sehr "fokussiert" | 1.0: Normal | 5.0: Fast gleichverteilt
    temperatures = [0.2, 1.0, 5.0]

    plt.figure(figsize=(10, 6))

    for temp in temperatures:
        probabilities = boltzmann_softmax(logits, temp)
        plt.plot(states, probabilities, marker='o', label=f'Temperatur T = {temp}')

    # Grafik hübsch machen
    plt.title('Einfluss der Temperatur auf die Boltzmann-Verteilung')
    plt.xlabel('Zustände')
    plt.ylabel('Wahrscheinlichkeit')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    print("Simulations-Grafik wird erstellt...")
    plt.show()


if __name__ == "__main__":
    main()
