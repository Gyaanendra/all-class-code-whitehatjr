import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np 
import csv


# # using matplotlib
data = pd.read_csv("c106/TV.csv",'r')
data.plot(kind = 'scatter', x ='Size', y = 'time')
plt.show()