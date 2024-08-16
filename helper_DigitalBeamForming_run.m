function [rd_beam_formed,model_DigitalBeamForming_new] = helper_DigitalBeamForming_run(range_doppler,model_DigitalBeamForming)
    % Compute virtual beams
    
    % Parameters:
    %     - range_doppler: Range Doppler spectrum for all RX antennas
    %                    (dimension: num_samples_per_chirp x num_chirps_per_frame x num_antennas)
    
    % Returns:
    %     - Range Doppler Beams (dimension: num_samples_per_chirp x num_chirps_per_frame x num_beams)
    
    [num_samples, num_chirps, num_antennas]= size(range_doppler);
    
    [num_antennas_internal, num_beams] = size(model_DigitalBeamForming.weights);
    
    assert(num_antennas == num_antennas_internal);
    
    rd_beam_formed = zeros(num_samples, num_chirps, num_beams);
    
    for iBeam = 1:num_beams
        acc = zeros(num_samples, num_chirps);
        for iAntenna = 1:num_antennas
            acc = acc + range_doppler(:, :, iAntenna) * model_DigitalBeamForming.weights(num_antennas - iAntenna + 1, iBeam);
        end
        rd_beam_formed(:, :, iBeam) = acc;
    end
    model_DigitalBeamForming_new = model_DigitalBeamForming;
end