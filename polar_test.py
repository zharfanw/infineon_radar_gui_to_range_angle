import matplotlib.pyplot as plt
import numpy as np
import time
import json

# Buat data
start_th = -(1/4)*np.pi
stop_th = (1/4)*np.pi
theta = np.linspace(start_th, stop_th, 100)
r = np.linspace(0, 5, 100)
theta, r = np.meshgrid(theta, r)

# Hitung nilai z (misalnya, fungsi sinus)
z = np.sin(theta) * np.cos(r)


print("shape z : ",end="")
print(np.shape(z))

# Buat plot polar dengan mesh
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
plt.pcolormesh(theta, r, z)
plt.colorbar()
plt.show()



# while(plt.fignum_exists(fig.number)):
#     print("Running")
#     time.sleep(3)