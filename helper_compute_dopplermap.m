function [doppler_map,doppler_model_new] = helper_compute_dopplermap(data, i_ant,doppler_model)
% Compute Range-Doppler map for i-th antennas

% Step 1 - Remove average from signal (mean removal)
data = double(data) - mean(data(:));

% Step 2 - MTI processing to remove static objects
data_mti = data - doppler_model.mti_history(:, :, i_ant);
doppler_model.mti_history(:, :, i_ant) = data * doppler_model.mti_alpha + doppler_model.mti_history(:, :, i_ant) * (1 - doppler_model.mti_alpha);

% Step 3 - calculate fft spectrum for the frame
fft1d = fft(data_mti .* doppler_model.range_window, [], 2);

% prepare for doppler FFT

% Transpose
% Distance is now indicated on y axis
fft1d = fft1d';

% Step 4 - Windowing the Data in doppler
fft1d = fft1d .* doppler_model.doppler_window;

% Zero padding
zp2 = [fft1d, zeros(size(fft1d, 1), doppler_model.num_chirps_per_frame)];
fft2d = fft(zp2, [], 2) / doppler_model.num_chirps_per_frame;

% re-arrange fft result for zero speed at centre
doppler_map = fftshift(fft2d, 2);
doppler_model_new = doppler_model;

end