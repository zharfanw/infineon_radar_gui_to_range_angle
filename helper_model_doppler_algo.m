function model_output = helper_model_doppler_algo(num_samples, num_chirps_per_frame, num_ant, mti_alpha)
    doppler_algo_setting.num_chirps_per_frame = num_chirps_per_frame;
    doppler_algo_setting.mti_alpha = mti_alpha;
    doppler_algo_setting.range_window = blackmanharris(num_samples);
    doppler_algo_setting.doppler_window = blackmanharris(num_chirps_per_frame);
    doppler_algo_setting.mti_history = zeros(num_chirps_per_frame, num_samples, num_ant);
    model_output = doppler_algo_setting;
end