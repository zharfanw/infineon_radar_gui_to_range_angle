import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fungsi untuk membuat data polar
def polar_data(r_max, theta_max, freq):
    r = np.linspace(0, r_max, 10)
    theta = np.linspace(0, theta_max, 100)
    R, Theta = np.meshgrid(r, theta)
    Z = np.sin(R * freq) * np.cos(Theta)
    return R, Theta, Z

# Buat figure dan subplot
fig, axs = plt.subplots(1, 3, subplot_kw={'projection': 'polar'})

# Inisialisasi data dan plot
r_max, theta_max = 10, 2*np.pi
freqs = [1, 2, 3]
lines = []
for ax, freq in zip(axs, freqs):
    R, Theta, Z = polar_data(r_max, theta_max, freq)
    line = ax.pcolormesh(Theta, R, Z, cmap='viridis')
    lines.append(line)

# Fungsi animasi
def animate(i):
    print("Frame ",end=":");print(i)
    for line, freq in zip(lines, freqs):
        R, Theta, Z = polar_data(r_max, theta_max, freq)
        print(np.shape(Z))
        Z += i * 0.1
        line.set_array(Z.ravel())
    return lines

# Buat animasi
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()