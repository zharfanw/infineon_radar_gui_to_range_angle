import random
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as animation

import time
import json

import inspect

# open Dataset 
datasetnya = ".dataset/BGT60TR13C_record_220240423-143957/RadarIfxAvian_00/radar.npy"
conf_fname =         '.dataset/BGT60TR13C_record_220240423-143957/RadarIfxAvian_00/config.json'

# Membuka file JSON
with open(conf_fname, 'r') as f:
    conf_json = json.load(f)
print("\nData dari file JSON:")
print(conf_json["device_config"]['fmcw_single_shape']['aaf_cutoff_Hz'])

datanya = np.load(datasetnya)

print("Shape datanya : ",end="")
print(np.shape(datanya))
frame_num, i_ant, chirp_num, samples_num = np.shape(datanya)
print("Jumlah Frame : ",end="");print(frame_num)
print("Jumlah Antenna : ",end="");print(i_ant)
print("Jumlah Chirps/Frame : ",end="");print(chirp_num)
print("Jumlah Samples/Chirp : ",end="");print(samples_num)

x = np.arange(chirp_num)  # Membuat array dari 0 hingga 63
y = np.arange(samples_num)  # Membuat array dari 0 hingga 63
framesya = np.arange(frame_num)

fps = 30
nSeconds = 5
snapshots = [ np.random.rand(5,6) for _ in range( nSeconds * fps ) ]
snapshots2 = [ np.random.rand(5,6) for _ in range( nSeconds * fps ) ]
snapshots3 = [ np.random.rand(5,6) for _ in range( nSeconds * fps ) ]

# Buat figure dan subplot
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# # Inisialisasi plot
# x, y1, y2, y3 = generate_data(0)
lines = [ax.plot(x, y)[0] for ax, y in zip(axes, [datanya[0][0][0], datanya[0][0][0], datanya[0][0][0]])]

# Fungsi untuk animasi
def animate(i):
    lines[0].set_data(x,datanya[i][0][0])
    lines[1].set_data(x,datanya[i][1][0])
    lines[2].set_data(x,datanya[i][2][0])
    # x, y1, y2, y3 = generate_data(i)
    # for line, y in zip(lines, [y1, y2, y3]):
    #     line.set_data(x, y)
    return lines

# Buat animasi
anim = animation.FuncAnimation(fig, animate, frames=100, interval=0.1, blit=True)

plt.show()