import pandas
import matplotlib.pyplot as plt
from datetime import datetime


def make_timestamp(t):
        time = list(str(datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f').timestamp()).replace(".", ""))

        for i in range(int(13 - len(time))): 
                time += ['0']

        return int(''.join(time))

pcoord = pandas.DataFrame.from_csv("raw_xovis.csv", sep=";")
uwb = pandas.DataFrame.from_csv("raw_uwbtags.csv", sep=";")

data_combined = {"XOVIS_TIME":[], "UWB_TIME":[], "UWB_X":[], "UWB_Y":[], "XOVIS_X":[], "XOVIS_Y":[], "XOVIS_PERSON_ID":[]}

for i in range(len(uwb.time)):
        uwb_y = uwb.iloc[i].x
        uwb_x = uwb.iloc[i].y
        uwb_time = make_timestamp(uwb.iloc[i].time)
        try:
                uwb_next_time = make_timestamp(uwb.iloc[i+1].time)
                # other visitors were at the testsite during the experiment,
                # unnessecary occupant data (ids) are sorted out
                indexes = pcoord[(pcoord.time >= uwb_time) & (pcoord.time < uwb_next_time) & (pcoord.id != 27978) & (pcoord.id != 27979) & (pcoord.id != 27974) & (pcoord.id != 27976) & (pcoord.id != 27971) & (pcoord.id != 27981)].time.index
        except:
                indexes = pcoord[(pcoord.time >= uwb_time) & (pcoord.id != 27978) & (pcoord.id != 27979) & (pcoord.id != 27974) & (pcoord.id != 27976) & (pcoord.id != 27971) & (pcoord.id != 27981)].time.index
        
        for j in indexes:
                data_combined["UWB_X"].append(uwb_x)
                data_combined["UWB_Y"].append(uwb_y)
                data_combined["UWB_TIME"].append(uwb_time)    
                data_combined["XOVIS_X"].append(pcoord.iloc[j].x)     
                data_combined["XOVIS_TIME"].append(pcoord.iloc[j].time)     
                data_combined["XOVIS_Y"].append(pcoord.iloc[j].y)      
                data_combined["XOVIS_PERSON_ID"].append(pcoord.iloc[j].id)  

df = pandas.DataFrame.from_dict(data_combined)
df.to_csv("XOVIS_UWB.csv", sep=";")
