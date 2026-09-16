import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0.0, 4.0, 801)
envelope = np.exp(-0.7 * time)
amplitude = envelope * np.cos(2 * np.pi * 1.5 * time)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(time, amplitude, color="navy", linewidth=1.8,
        label="Damped oscillation")
ax.plot(time, envelope, color="darkorange", linestyle="--",
        label="Exponential envelope")
ax.plot(time, -envelope, color="darkorange", linestyle="--")
ax.set(xlabel="Time (s)", ylabel="Amplitude",
       title="Damped oscillation", xlim=(0, 4), ylim=(-1.1, 1.1))
ax.grid(alpha=0.25)
ax.legend(loc="upper right")
fig.tight_layout()
plt.show()
