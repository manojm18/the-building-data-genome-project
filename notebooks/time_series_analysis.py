# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:19:06 2017

@author: MANOJ
"""

import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
from datetime import date, timedelta
import numpy as np
params = {'legend.fontsize': 'x-large',
          'axes.labelsize': 'x-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'xx-large',
         'font.size': 17}
plt.rcParams.update(params)

repos_path = "C:/Users/MANOJ/the-building-data-genome-project/"

temp = pd.read_csv(os.path.join(repos_path,"data/raw/temp_open_utc.csv"), index_col="timestamp", parse_dates=True)
meta = pd.read_csv(os.path.join(repos_path,"data/raw/meta_open.csv"), index_col='uid', parse_dates=["datastart","dataend"], dayfirst=True)

office = temp[['Office_Elizabeth']]['2012-01':'2012-03']
weather = pd.read_csv(os.path.join(repos_path,"data/external/weather/weather22.csv"),index_col="timestamp", parse_dates=True)
temperature = weather[['TemperatureC']]['2012-01':'2012-03']

temperature = temperature.resample('H').mean()

office.join(temperature).plot()