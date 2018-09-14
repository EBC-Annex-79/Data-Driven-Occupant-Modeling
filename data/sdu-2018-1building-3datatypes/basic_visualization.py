#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.ticker
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import FuncFormatter
import matplotlib
import time

#Script for generating daily profiles for different data types and rooms

#Dataset parameters
rooms = ["room_1","room_2","room_3","room_4"]
sensors = ["co2","occ","vav"]
sensortypes = {"co2":"Concentration [ppm]","occ":"Persons","vav":"Openess [%]"}
ylimit = {"co2":1500,"occ":75,"vav":100}

#Group time-series per day
def groupPerDay(sr):
    sr.index = pd.to_datetime(sr.index)
    rs = []
    for group in sr.groupby(sr.index.day+31*sr.index.month+365*sr.index.year):
        if len(group[1][0]) == 1440:
            rs.append(group[1][0])
    return rs

#Load sensor data from csv files
def load_data(sensor):
    results = {}
    for room in rooms:
        roomresults = {"data": [], "ts": []}
        inputvals = np.genfromtxt(sensor + "_data_" + room + ".csv", dtype=str, delimiter=',', skip_header=1, skip_footer=0)
        j = 1
        dayID = None
        for val in inputvals:
            #Hack for working with anonymized data in Pandas. Assumes that the time-series is less than one month
            concatval = "2016-09-" + str(j) + " " + val[1]
            if dayID != val[0]:
                j = j + 1
                dayID = val[0]
            ts = pd.to_datetime(concatval,infer_datetime_format=True)
            roomresults["ts"].append(ts)
            roomresults["data"].append(float(str(val[4])))
        results[room] = pd.DataFrame(roomresults["data"], index=roomresults["ts"])
    return results

#Compute rolling mean on graph
def rolling_mean(data, axis=0):
    result = pd.rolling_mean(data, 4, axis=1).mean(axis=axis)
    return result

#Make visualizations of data
for sensor in sensors:
    results = load_data(sensor)
    pp = PdfPages('basic_vis_data_%s.pdf' % (sensor))
    for i in range(len(rooms)):
        rs = groupPerDay(results[rooms[i]])
        plt.subplot(4,1,i+1)

        sns.set(style="darkgrid", palette="Set2")

        colors = ["#999999","#999999","#999999"]
        cp = sns.color_palette(colors, 8,0.01)
        ax = sns.tsplot(rs,err_style="unit_traces", color='k',err_palette=cp, n_boot=500, estimator=rolling_mean)

        ax.get_xaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format((int(x/60))%24, ',')))

        ax.tick_params(labelsize=6)
        plt.xlabel('Time of day [Hours]', fontsize=6)
        plt.ylabel(sensortypes[sensor], fontsize=6)
        plt.ylim(0,ylimit[sensor])

    plt.tight_layout()
    plt.savefig(pp, format='pdf', bbox_inches="tight") #
    pp.close()
    plt.close()