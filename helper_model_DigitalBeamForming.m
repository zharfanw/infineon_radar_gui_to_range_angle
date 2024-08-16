function model_DigitalBeamForming = helper_model_DigitalBeamForming(num_antennas, num_beams, max_angle_degrees, d_by_lambda)
    % Create a Digital Beam Forming object
    
    % Parameters:
    %     - num_antennas: number of (virtual) RX antennas
    %     - num_beams: number of beams
    %     - max_angle_degrees: maximum   
    %                           angle in degrees, angles will range from -max_angle_degrees .. +max_angle_degrees
    %     - d_by_lambda: separation of RX antennas divided by the wavelength
    
    angle_vector = deg2rad(linspace(-max_angle_degrees, max_angle_degrees, num_beams));
    
    % weights = zeros(num_antennas, num_beams, 'complex');
    weights = zeros(num_antennas, num_beams);
    
    for iBeam = 1:num_beams
        angle = angle_vector(iBeam);
        for iAntenna = 1:num_antennas
            weights(iAntenna, iBeam) = exp(1j * 2 * pi * (iAntenna - 1) * d_by_lambda * sin(angle));  % /sqrt(num_antennas)
        end
    end

    obj.weights = weights;
    model_DigitalBeamForming = obj;
end