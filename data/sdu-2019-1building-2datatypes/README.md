# Dataset Description

An inspiration dataset covering occupant people tracking based on 3D stereo vision camera and UWB positioning sensors (poxyz). A person walks in circle while other occupants are also present in the area.


| File              | Description |
|---|---|
|raw_uwbtags.csv       | Raw position traces for uwb tags |
|raw_xovis.csv     | Raw position traces from XOVIS 3D camera |
|upsample.py 	| Script to combine raw data traces |
|XOVIS_UWB.csv | Combined data |
|Xovis_Uwb.png    | Plots of data (left Xovis and right UWB tags |

To cite the dataset and paper:
```
@inproceedings{Das:2019:DOPT,
author = {Das, Anooshmita and Schwee, Jens Hjort and Kolvig-Raun, Emil Stubbe and Kj\ae{}rgaard, Mikkel Baun},
title = {Dataset: Occupancy Presence and Trajectory Data from an Instrumented Public Building},
year = {2019},
isbn = {9781450369930},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3359427.3361909},
doi = {10.1145/3359427.3361909},
booktitle = {Proceedings of the 2nd Workshop on Data Acquisition To Analysis},
pages = {43–46},
numpages = {4},
keywords = {Dataset, Trajectories, Occupancy Presence},
location = {New York, NY, USA},
series = {DATA’19}
}
```

### License
The license for all the data is CC-BY-4.0
