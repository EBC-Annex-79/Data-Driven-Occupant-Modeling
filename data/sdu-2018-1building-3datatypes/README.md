# Dataset Description

A dataset covering occupant counts based on 3D stereo vision camera, damper openness to represent airflow into each room and CO2 concentration measured by in-room sensors

| File              | Description |
|---|---|
|roominfo.txt       | Room information |
|co2_data_X.csv     | Room CO2 [ppm] for room X |
|occ_data_X.csv 	| Camera-based occupancy [persons] for room X |
|vav_data_X.csv     | Damper openess (per room) [%] for room X |
|brick_generator.py | Script for generating brick graph |
|brick_graph.ttl    | Generated brick graph represented in the turtle format |
|basic_visualization.py    | Generate basic visualization of data in pdf |
|data-descriptor.pdf | Detailed description of data |

Time periode 2017-03-22 00:00:00 - 2017-04-05 23:59:00

Contents of data files:

| Label | Description |
| --- | --- |
| DayID | random generated identifier |
| Time | Time of day |
| Weekday | Weekday as a decimal number, where Monday is 0 and Sunday is 6 |
| Holiday | 1 if national public holiday and 0 if not |

