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


To cite the dataset and paper:
```
@inproceedings{Arendt:2018:ROC:3277868.3277875,
 author = {Arendt, Krzysztof and Johansen, Aslak and J{\o}rgensen, Bo N{\o}rregaard and Kj{\ae}rgaard, Mikkel Baun and Mattera, Claudio Giovanni and Sangogboye, Fisayo Caleb and Schwee, Jens Hjort and Veje, Christian T.},
 title = {Room-level Occupant Counts, Airflow and CO2 Data from an Office Building},
 booktitle = {Proceedings of the First Workshop on Data Acquisition To Analysis},
 series = {DATA '18},
 year = {2018},
 isbn = {978-1-4503-6049-4},
 location = {Shenzhen, China},
 pages = {13--14},
 numpages = {2},
 url = {http://doi.acm.org/10.1145/3277868.3277875},
 doi = {10.1145/3277868.3277875},
 acmid = {3277875},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {CO2, data, occupant sensing},
} 
```

### License

The license for all the data is CC-BY-4.0
