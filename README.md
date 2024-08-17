# infineon_radar_gui_to_range_angle
 Convert Raw Data to range angle map with MATLAB or Python. But recommend using MATLAB.
 
open `./convert_to_range_angle_map.m`

edit line below for set dataset path

    datasetnya  =  readNPY("sample_raw_radar_data\RadarIfxAvian_00\radar.npy");
    conf_fname  =  'sample_raw_radar_data\RadarIfxAvian_00\config.json';

for edit frame index   

    start_frame  =  1;
    last_frame  =  99;

  
for editing angle Aqusition
start_angle  =  -90;
stop_angle  =  90;


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTUzNDYwNDddfQ==
-->