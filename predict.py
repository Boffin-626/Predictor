import numpy as np 
import pandas as pd 
import os 

import warnings 
warnings.filterwarnings('ignore')

df = pd.read_csv('soccerData.csv')

df['date']= pd.to_datetime(df['date'])

