import numpy as np
from signal_ICT_SaloniRamavat_92400133020.unitary_signals import unit_step
from signal_ICT_SaloniRamavat_92400133020.trigonometric_signals import sine_wave
from signal_ICT_SaloniRamavat_92400133020.operations import (
    time_shift,
    time_scale,
    signal_addition,
    signal_multiplication
)

# Unit step
u = unit_step(5)
print("Unit step:", u)

# Sine wave
t = np.linspace(0, 1, 5)
s = sine_wave(A=1, f=1, phi=0, t=t)
print("Sine wave:", s)

# Example operations
shifted = time_shift(s, 1)
scaled = time_scale(s, 1)
added = signal_addition(u[:len(s)], s)
multiplied = signal_multiplication(u[:len(s)], s)
