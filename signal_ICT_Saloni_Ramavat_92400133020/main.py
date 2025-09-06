import numpy as np
from signal_ICT_SaloniRamavat_92400133020 import *

# Discrete domain for unit signals
n = np.arange(-10, 10)

# 1. Unit Step
step = unit_step(n)

# 2. Unit Impulse
impulse = unit_impulse(n)

# 3. Ramp Signal
ramp = ramp_signal(n)

# Time domain for trigonometric & exponential signals
t = np.linspace(0, 1, 1000)

# 4. Sine Wave
sine = sine_wave(2, 5, 0, t)

# 5. Cosine Wave
cos = cosine_wave(2, 5, 0, t)

# 6. Exponential Signal
expo = exponential_signal(1, -2, t)

# 7. Time Shifting (Sine shifted by +5)
shifted_sine = time_shift(sine, 5)

# 8. Addition of Unit Step + Ramp
added = signal_addition(step, ramp)

# 9. Multiplication of Sine × Cosine
multiplied = signal_multiplication(sine, cos)

# 10. Time Scaling (on sine wave)
scaled = time_scale(sine, 2)
