
# Converting Infineon BGT60TR13C Radar Raw Data to Range-Angle MAP
## Converting Infineon Radar Raw Data to Range-Angle Map using MATLAB

### Overview

This guide outlines the process of converting raw radar data from an Infineon radar sensor into a range-angle map using MATLAB. The provided MATLAB script,  `convert_to_range_angle_map.m`, serves as a starting point.

### Steps Involved

1.  **Load Raw Data**:
    
    -   Open the MATLAB script `convert_to_range_angle_map.m`.
    -   Specify the path to your raw radar data file (`.npy` format) and configuration file (`.json` format) in the following lines:
        
        Matlab
        
        ```
        datasetnya = readNPY("sample_raw_radar_data\RadarIfxAvian_00\radar.npy");
        conf_fname = 'sample_raw_radar_data\RadarIfxAvian_00\config.json';
        
        ```
        
        
2.  **Define Frame Range**:
    
    -   Specify the starting and ending frame indices for processing:
        
        Matlab
        
        ```
        start_frame = 1;
        last_frame = 99;
        
        ```
        
        
3.  **Set Angle Acquisition Range**:
    
    -   Define the desired angle range for the map:
        
        Matlab
        
        ```
        start_angle = -90;
        stop_angle = 90;
        
        ```
        
        

### Additional Considerations

-   **Data Structure**: The script assumes the raw data is stored in a NumPy array (`.npy` format) and the configuration data is in a JSON file.
-   **Configuration File**: The configuration file likely contains information about the radar sensor, such as antenna layout, sampling frequency, and other relevant parameters. These parameters are essential for accurate range-angle mapping.
-   **Processing Algorithm**: The core algorithm for converting raw data to a range-angle map is not provided in the snippet. You'll need to implement this based on the radar sensor's characteristics and desired output format.
-   **Visualization**: Once the range-angle map is generated, consider using MATLAB's plotting functions to visualize the results.
## Converting Infineon Radar Raw Data to Range-Angle Map using PYTHON

## Converting Raw Data to Range-Angle Map with Python

### Prerequisites

-   **Python 3.12 or later**
-   **Basic understanding of Python programming**

### Setting Up the Environment

**1. Create a Virtual Environment**

-   **Windows:**
    
    Bash
    
    ```
    python -m venv venv
    venv\Scripts\activate
    
    ```
    
    Use code [with caution.](/faq#coding)
    
-   **macOS/Linux:**
    
    Bash
    
    ```
    python3 -m venv venv
    source venv/bin/activate
    
    ```
    
    

**2. Install Required Packages**

[](https://github.com/parthahere001/instagram-stats-visualizer)

1. github.com

[](https://github.com/parthahere001/instagram-stats-visualizer)

github.com

Create a `requirements.txt` file in your project directory with the following content:

```
numpy
scipy
matplotlib

```

Then install the packages:

Bash

```
pip install -r requirements.txt

```

**3. Load Raw Data**
-   Open the Python script `view_polar_dataset.py`.
    -   Specify the path to your raw radar data file (`.npy` format) and configuration file (`.json` format) in the following lines:
        
        Python
        
        
    

        # open Dataset
            datasetnya  =  "sample_raw_radar_data/RadarIfxAvian_00/radar.npy"
    conf_fname  =  "sample_raw_radar_data/RadarIfxAvian_00/config.json"
            

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5ODcyMTk3LC0xMzk4OTIxMzA3LC0xNT
YyMTAwNDMwLDE0MzIyMzc0OTYsMjA2MTM2MDE3NV19
-->