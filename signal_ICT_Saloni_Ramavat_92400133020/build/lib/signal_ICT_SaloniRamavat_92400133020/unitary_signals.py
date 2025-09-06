import numpy as np
import matplotlib.pyplot as plt 

# 	unit_step(n) – Generates a unit step signal.
# 	unit_impulse(n) – Generates a unit impulse signal.
# 	ramp_signal(n) – Generates a ramp signal.

# A unit step signal can exist only for positive values and zero for negative values.
def unit_step(n):
    signal = np.array([1 if i >= 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal

#It exists only at t= 0 and the area under impulse function is unity.
def unit_impulse(n) :
    signal = np.array([1 if i == 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal


#defined as zero for t < 0 and increases linearly as t for t >= 0, commonly used in systems analysis. 
def ramp_signal(n):
    signal = np.array([i if i >= 0 else 0 for i in n])
    plt.stem(n, signal)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    return signal