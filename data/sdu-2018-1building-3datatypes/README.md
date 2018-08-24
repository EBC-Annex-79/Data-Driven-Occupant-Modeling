# Dataset Description

A dataset covering occupant counts based on 3D stereo vision camera, damper openness to represent airflow into each room and CO2 concentration measured by in-room sensors

Time periode 2017-03-21 00:00:00 - 2017-04-05 23:59:00

Labels of the data files:
DayID: random generated identifier.
Time: Time of day.
Weekday: Weekday as a decimal number, where Monday is 0 and Sunday is 6.
Holiday: 1 if national public holiday and 0 if not.

| File:              | Description: |
|---|---|
|roominfo.txt       | Room information |
|co2_data_X.csv     | Room CO2 [ppm] for room X |
|occ_data_X.csv 	| Camera-based occupancy [persons] for room X |
|vav_data_X.csv     | Damper openess (per room) [%] for room X |
|brick_generator.py | Script for generating brick graph |
|brick_graph.ttl    | Generated brick graph represented in the turtle format |