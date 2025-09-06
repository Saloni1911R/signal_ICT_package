import numpy as np
import matplotlib.pyplot as plt

#  time_shift(signal, k) – Shifts the signal by k units
def time_shift(signal, k):
    shifted = np.roll(signal, k)
    n = np.arange(len(signal))

    plt.stem(n, signal, linefmt='b-', markerfmt='bo', basefmt=' ')
    plt.stem(n, shifted, linefmt='r-', markerfmt='ro', basefmt=' ')
    plt.title(f"Time Shift (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend(["Original", "Shifted"])
    plt.grid(True)
    plt.show()

    return shifted

#  time_scale(signal, k) – Scales the time axis of the signal
def time_scale(signal, k):
    if k <= 0:
        raise ValueError("Scaling factor k must be positive")
    
    n = np.arange(len(signal))
    scaled = signal[::k]  # pick every k-th sample

    plt.stem(n, signal, linefmt='b-', markerfmt='bo', basefmt=' ')
    plt.stem(np.arange(0, len(signal), k), scaled, linefmt='r-', markerfmt='ro', basefmt=' ')
    plt.title(f"Time Scaling (k={k})")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.legend(["Original", "Scaled"])
    plt.grid(True)
    plt.show()

    return scaled

#  signal_addition(signal1, signal2) – Adds two signals
def signal_addition(signal1, signal2):
    min_len = min(len(signal1), len(signal2))
    added = signal1[:min_len] + signal2[:min_len]
    n = np.arange(min_len)

    plt.stem(n, added)
    plt.title("Signal Addition")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    return added

#  signal_multiplication(signal1, signal2) – Multiplies two signals
def signal_multiplication(signal1, signal2):
    min_len = min(len(signal1), len(signal2))
    multiplied = signal1[:min_len] * signal2[:min_len]
    n = np.arange(min_len)

    plt.stem(n, multiplied)
    plt.title("Signal Multiplication")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    return multiplied
