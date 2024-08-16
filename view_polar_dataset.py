import matplotlib.pyplot as plt
import numpy as np
import time
import json
import matplotlib.animation as animation
import matplotlib.transforms as mtransforms
import mpl_toolkits.axisartist.floating_axes as floating_axes

# from helpers.DistanceAlgo import *
from helpers.DopplerAlgo import *
from helpers.DigitalBeamForming import *


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
frame_num, num_ant, chirp_num, samples_num = np.shape(datanya)
print("Jumlah Frame : ",end="");print(frame_num)
print("Jumlah Antenna : ",end="");print(num_ant)
print("Jumlah Chirps/Frame : ",end="");print(chirp_num)
print("Jumlah Samples/Chirp : ",end="");print(samples_num)



x = np.arange(chirp_num)  # Membuat array dari 0 hingga 63
y = np.arange(samples_num)  # Membuat array dari 0 hingga 63
framesya = np.arange(frame_num)

num_beams = 27  # number of beams
max_angle_degrees = 40  # maximum angle, angle ranges from -40 to +40 degrees


doppler = DopplerAlgo(samples_num, chirp_num, num_ant)
dbf = DigitalBeamForming(num_ant, num_beams=num_beams, max_angle_degrees=max_angle_degrees)

# for sig_frame in datanya:
#     # print(sig_frame[0,:,:])
#     frame = sig_frame

#     rd_spectrum = np.zeros((samples_num, 2 * chirp_num, num_ant), dtype=complex)

#     beam_range_energy = np.zeros((samples_num, num_beams))

#     for i_ant in range(num_ant):  # For each antenna
#         # Current RX antenna (num_samples_per_chirp x num_chirps_per_frame)
#         mat = frame[i_ant, :, :]

#         # Compute Doppler spectrum
#         dfft_dbfs = doppler.compute_doppler_map(mat, i_ant)
#         rd_spectrum[:, :, i_ant] = dfft_dbfs

#     # Compute Range-Angle map
#     rd_beam_formed = dbf.run(rd_spectrum)
#     for i_beam in range(num_beams):
#         doppler_i = rd_beam_formed[:, :, i_beam]
#         beam_range_energy[:, i_beam] += np.linalg.norm(doppler_i, axis=1) / np.sqrt(num_beams)

#     # Maximum energy in Range-Angle map
#     max_energy = np.max(beam_range_energy)

#     # Rescale map to better capture the peak The rescaling is done in a
#     # way such that the maximum always has the same value, independent
#     # on the original input peak. A proper peak search can greatly
#     # improve this algorithm.
#     scale = 150
#     beam_range_energy = scale * (beam_range_energy / max_energy - 1)

#     # Find dominant angle of target
#     _, idx = np.unravel_index(beam_range_energy.argmax(), beam_range_energy.shape)
#     angle_degrees = np.linspace(-max_angle_degrees, max_angle_degrees, num_beams)[idx]
#     print(np.shape(beam_range_energy))

c = 3e8; # Speed of light (m/s)
Chirp_Time_sec = conf_json['device_config']['fmcw_single_shape']['frame_repetition_time_s']
Upper_RF_Frequency_kHz = conf_json['device_config']['fmcw_single_shape']['end_frequency_Hz']
Lower_RF_Frequency_kHz = conf_json['device_config']['fmcw_single_shape']['start_frequency_Hz']
Sampling_Frequency_kHz = conf_json['device_config']['fmcw_single_shape']['sample_rate_Hz']/1000
CRR = 1/Chirp_Time_sec # Chirp repetition rate (Hz)
# FRR=1/Radar_Parameter.Frame_Period_sec;# Frame repetition rate (Hz)
BW = (Upper_RF_Frequency_kHz-Lower_RF_Frequency_kHz)*1000 # Bandwidth (Hz)

range_res = c/(2*BW)
max_range = range_res*np.fix(Sampling_Frequency_kHz*1e3/CRR)/2

polar_fig, polar_axs = plt.subplots(subplot_kw={'projection': 'polar'})
# polar_fig, polar_axs = plt.subplots()

# Inisialisasi data dan plot
# start_th = -(1/4)*np.pi
# stop_th = (1/4)*np.pi

freqs = [1, 2, 3]

r = np.linspace(0, max_range , samples_num)

# start_th = -(1/4)*np.pi
# stop_th = (1/4)*np.pi
start_th = -np.pi/2
stop_th = np.pi/2
rot_th = np.pi/2

theta = np.linspace(start_th, stop_th, num_beams)
theta = theta + rot_th

R, Theta = np.meshgrid(r, theta)
print(np.shape(R))
Z = np.zeros((num_beams,samples_num))
# Z = np.sin(R * freq) * np.cos(Theta)
# R, Theta, Z = polar_data(r_max, theta_max, freq)
print(r)



line = polar_axs.pcolormesh(Theta, R, Z, cmap='viridis')

real_grid_start = np.rad2deg(theta[0])
real_grid_stop = np.rad2deg(theta[-1])
real_grid_space = 5
rot_grid = np.rad2deg(rot_th)

real_grid = np.linspace(real_grid_start,real_grid_stop, real_grid_space )
new_grid = real_grid - rot_grid



polar_axs.set_thetagrids(real_grid,labels=new_grid)


# polar_axs.set_rlabel_position(45)  # Posisi label radial
polar_axs.set_rticks(np.arange(0, max_range , 0.5))  # Nilai-nilai untuk label radial
polar_axs.set_yticklabels(np.arange(0, max_range , 0.5))  # Label kustom
polar_axs.set_xlabel("X LABEL")  # Label kustom
polar_axs.set_ylabel("Y LABEL")  # Label kustom
polar_axs.set_label("JUST LABEL")  # Label kustom
polar_axs.ThetaAxis.set_label_text("JANCOK")





polar_axs.set_thetamin(real_grid_start)  # Batas theta minimum
polar_axs.set_thetamax(real_grid_stop)  # Batas theta maksimum

plt.text(0.1,0.1, 'I am cartesian coordinate', transform=plt.gcf().transFigure)

# plt.gca().set_transform(mtransforms.Affine2D().rotate_deg(45) + plt.gca().transData)


# line = polar_axs.imshow(Z, interpolation='none', aspect='auto', vmin=0, vmax=1)

# Fungsi animasi
def animate(i):
    print("Frame ",end=": ");print(i)
    frame = datanya[i]
    polar_axs.set_title("Polar Angle Map Frame : "+str(i))
    rd_spectrum = np.zeros((samples_num, 2 * chirp_num, num_ant), dtype=complex)

    beam_range_energy = np.zeros((samples_num, num_beams))

    for i_ant in range(num_ant):  # For each antenna
        # Current RX antenna (num_samples_per_chirp x num_chirps_per_frame)
        mat = frame[i_ant, :, :]

        # Compute Doppler spectrum
        dfft_dbfs = doppler.compute_doppler_map(mat, i_ant)
        rd_spectrum[:, :, i_ant] = dfft_dbfs

    # Compute Range-Angle map
    rd_beam_formed = dbf.run(rd_spectrum)
    for i_beam in range(num_beams):
        doppler_i = rd_beam_formed[:, :, i_beam]
        beam_range_energy[:, i_beam] += np.linalg.norm(doppler_i, axis=1) / np.sqrt(num_beams)

    # Maximum energy in Range-Angle map
    max_energy = np.max(beam_range_energy)

    # Rescale map to better capture the peak The rescaling is done in a
    # way such that the maximum always has the same value, independent
    # on the original input peak. A proper peak search can greatly
    # improve this algorithm.
    scale = 150
    beam_range_energy = scale * (beam_range_energy / max_energy - 1)
    beam_range_energy = np.transpose(beam_range_energy)

    # Find dominant angle of target
    # _, idx = np.unravel_index(beam_range_energy.argmax(), beam_range_energy.shape)
    # angle_degrees = np.linspace(-max_angle_degrees, max_angle_degrees, num_beams)[idx]
    # print(np.shape(beam_range_energy))
    line.set_array(beam_range_energy.ravel())
    # line.set_array(beam_range_energy)
    line.autoscale()
    return line

# Buat animasi
ani = animation.FuncAnimation(polar_fig, animate, frames=frame_num, interval=1)


plt.show()

# plt.show()

# # Buat data
# start_th = -(1/4)*np.pi
# stop_th = (1/4)*np.pi
# theta = np.linspace(start_th, stop_th, 100)
# r = np.linspace(0, 5, 100)
# theta, r = np.meshgrid(theta, r)


# # Hitung nilai z (misalnya, fungsi sinus)
# z = np.sin(theta) * np.cos(r)


# print("shape z : ",end="")
# print(np.shape(z))

# # view

# # Buat plot polar dengan mesh
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# plt.pcolormesh(theta, r, z)
# plt.colorbar()
# plt.show()
