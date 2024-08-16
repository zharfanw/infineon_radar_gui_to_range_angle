clc
clear all
close all

%% Load Raw Radar Data
% Talking Condition
anal_name = "mat_Talking_1";
datasetnya = readNPY(".dataset\BGT60TR13C_record_220240423-143957\RadarIfxAvian_00\radar.npy");
conf_fname =         '.dataset\BGT60TR13C_record_220240423-143957\RadarIfxAvian_00\config.json'; 

conf_fid = fopen(conf_fname); 
conf_raw = fread(conf_fid,inf); 
conf_str = char(conf_raw'); 
fclose(conf_fid); 
conf_confignya = jsondecode(conf_str);

Radar_Parameter.Num_Tx_Antennas = conf_confignya.device_config.fmcw_single_shape.tx_antennas;
Radar_Parameter.Num_Rx_Antennas= length(conf_confignya.device_config.fmcw_single_shape.rx_antennas);
Radar_Parameter.Mask_Tx_Antennas = 1;
Radar_Parameter.Mask_Rx_Antennas = 7;
Radar_Parameter.Are_Rx_Antennas_Interleaved = 1;
Radar_Parameter.Modulation_Type_Enum = 1;
Radar_Parameter.Chirp_Shape_Enum= 0;
Radar_Parameter.Lower_RF_Frequency_kHz = conf_confignya.device_config.fmcw_single_shape.start_frequency_Hz;
Radar_Parameter.Upper_RF_Frequency_kHz = conf_confignya.device_config.fmcw_single_shape.end_frequency_Hz;
Radar_Parameter.Sampling_Frequency_kHz = conf_confignya.device_config.fmcw_single_shape.sample_rate_Hz/1000;
Radar_Parameter.ADC_Resolution_Bits=12;
Radar_Parameter.Are_ADC_Samples_Normalized =1;
Radar_Parameter.Data_Format_Enum=0;
Radar_Parameter.Chirps_per_Frame=conf_confignya.device_config.fmcw_single_shape.num_chirps_per_frame;
Radar_Parameter.Samples_per_Chirp= conf_confignya.device_config.fmcw_single_shape.num_samples_per_chirp;
Radar_Parameter.Samples_per_Frame=Radar_Parameter.Chirps_per_Frame*Radar_Parameter.Samples_per_Chirp*Radar_Parameter.Num_Rx_Antennas;
Radar_Parameter.Chirp_Time_sec=conf_confignya.device_config.fmcw_single_shape.frame_repetition_time_s;
Radar_Parameter.Pulse_Repetition_Time_sec=conf_confignya.device_config.fmcw_single_shape.chirp_repetition_time_s;
Radar_Parameter.Frame_Period_sec=conf_confignya.device_config.fmcw_single_shape.frame_repetition_time_s;

dummy_size = size(datasetnya);
Frame_Number = dummy_size(1);
NumRXAntenna = Radar_Parameter.Num_Rx_Antennas;
Frame = datasetnya;

%% Setup Configuration
% fprintf('Radar SDK Version: %s\n', get_version_full());
% fprintf('Sensor: %s\n', device.get_sensor_type());

% Get metrics and print them
% chirp_loop = sequence.loop.sub_sequence.contents;
% metrics = device.metrics_from_sequence(chirp_loop);   
% 
% disp(metrics);
% 
% % Get maximum range
% max_range_m = metrics.max_range_m;

% chirp = chirp_loop.loop.sub_sequence.contents.chirp;
% num_rx_antennas = num_rx_antennas_from_rx_mask(chirp.rx_mask);

% Create objects for Range-Doppler, Digital Beam Forming, and plotting.
config_chirp_num_samples = Radar_Parameter.Samples_per_Chirp;   
config_num_chirps = Radar_Parameter.Chirps_per_Frame;
num_rx_antennas = Radar_Parameter.Num_Rx_Antennas;
num_beams = 27;
max_angle_degrees = 40 ;
mti_alpha = 0.8;
d_by_lambda = 0.5;

c = 3e8; % Speed of light (m/s)
CRR = 1/Radar_Parameter.Chirp_Time_sec; % Chirp repetition rate (Hz)
% FRR=1/Radar_Parameter.Frame_Period_sec;% Frame repetition rate (Hz)
BW = (Radar_Parameter.Upper_RF_Frequency_kHz-Radar_Parameter.Lower_RF_Frequency_kHz)*1000; % Bandwidth (Hz)

range_res = c/(2*BW);
max_range = range_res*fix(Radar_Parameter.Sampling_Frequency_kHz*1e3/CRR)/2;

%% Create The Model
doppler_modelnya = helper_model_doppler_algo(config_chirp_num_samples, config_num_chirps, num_rx_antennas,mti_alpha);
dbf_modelnya = helper_model_DigitalBeamForming(num_rx_antennas, num_beams, max_angle_degrees,d_by_lambda);
% plot = LivePlot(max_angle_degrees, max_range_m);



raw_i = 1; % First Index of Frame
end_raw_i = dummy_size(1); % Last Index of Frame
% 
figure("Name","Range Angle Map")
while raw_i<end_raw_i
    % Get frame data
    frame = squeeze(Frame(raw_i,:, :, :));

    % Initialize variables
    rd_spectrum = zeros(config_chirp_num_samples, 2 * config_num_chirps, num_rx_antennas);
    % beam_range_energy = zeros(config_chirp_num_samples*2, num_beams);
    beam_range_energy = zeros(config_chirp_num_samples*2, num_beams);

    for i_ant = 1:num_rx_antennas  % Loop through antennas (1-based indexing in MATLAB)
        % Current RX antenna
        mat = squeeze(frame(i_ant, :, :));  % Extract antenna data

        % Compute Doppler spectrum
        % dfft_dbfs = doppler.compute_doppler_map(mat, i_ant);
        [dfft_dbfs,doppler_modelnya] = helper_compute_dopplermap(mat, i_ant,doppler_modelnya);
        rd_spectrum(:, :, i_ant) = dfft_dbfs;
    end

    % Compute Range-Angle map
    % rd_beam_formed = dbf.run(rd_spectrum);
    [rd_beam_formed,dbf_modelnya] = helper_DigitalBeamForming_run(rd_spectrum,dbf_modelnya);

    for i_beam = 1:num_beams
        % Extract Doppler for current beam
        doppler_i = rd_beam_formed(:, :, i_beam);

        % Beamforming - accumulate energy across range bins
        beam_range_energy(:, i_beam) = sum(abs(doppler_i), 1) / sqrt(num_beams);
    end

    % Maximum energy in Range-Angle map
    max_energy = max(beam_range_energy(:));

    % Rescale map (consider a proper peak detection algorithm for improvement)
    scale = 150;
    beam_range_energy = scale * (beam_range_energy / max_energy - 1);

    % Find dominant angle
    % [~, idx] = find(beam_range_energy == max(beam_range_energy(:)));
    % angle_degrees = linspace(-max_angle_degrees, max_angle_degrees, num_beams)(idx);
    % 
    % % Call your plotting function (replace with your implementation)
    % % plot.draw(beam_range_energy, f"Range-Angle map using DBF, angle={angle_degrees:+02.0f} degrees");
    surf(beam_range_energy)
    view(2)
    colormap default
    colorbar
    % hold on
    drawnow
    raw_i = raw_i + 1;
end
