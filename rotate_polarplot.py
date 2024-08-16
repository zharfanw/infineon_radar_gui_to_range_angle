import numpy as np
import matplotlib.pyplot as plt

# Buat data polar
theta = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 5, 100)
Theta, R = np.meshgrid(theta, r)
Z = np.sin(R) * np.cos(Theta)

# Buat plot polar
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
im = ax.pcolormesh(Theta, R, Z, cmap='viridis')

# # Ganti label radial
# ax.set_rlabel_position(-22.5)  # Posisi label radial
# ax.set_rticks([1, 2, 3, 4, 5])  # Nilai-nilai untuk label radial
# ax.set_rticklabels(['1 km', '2 km', '3 km', '4 km', '5 km'])  # Label kustom

# Ganti label sudut
ax.set_theta_offset(np.pi / 4)  # Offset sudut awal
ax.set_theta_direction(-1)  # Arah berlawanan jarum jam
ax.set_thetagrids(np.arange(0, 360, 45), labels=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

plt.show()
