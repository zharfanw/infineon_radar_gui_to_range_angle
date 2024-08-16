import matplotlib.pyplot as plt
import numpy as np
import time
import json

# open Dataset 
datasetnya = ".dataset/BGT60TR13C_record_220240423-143957/RadarIfxAvian_00/radar.npy"
conf_fname =         '.dataset/BGT60TR13C_record_220240423-143957/RadarIfxAvian_00/config.json'

# Membuka file JSON
with open(conf_fname, 'r') as f:
    conf_json = json.load(f)
print("\nData dari file JSON:")
print(conf_json["device_config"]['fmcw_single_shape']['aaf_cutoff_Hz'])

datanya = np.load(datasetnya)

# Buat data
start_th = -(1/4)*np.pi
stop_th = (1/4)*np.pi
theta = np.linspace(start_th, stop_th, 100)
r = np.linspace(0, 5, 100)
theta, r = np.meshgrid(theta, r)

# Hitung nilai z (misalnya, fungsi sinus)
z = np.sin(theta) * np.cos(r)

print("Shape datanya : ",end="")
print(np.shape(datanya))
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