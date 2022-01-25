import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np 
import csv


# # using matplotlib
# data = pd.read_csv("c106/icecream.csv")
# data.plot(kind = 'scatter', x = 'Temperature', y = 'Ice-creamSales')
# plt.show()

# usong poltly
# data = pd.read_csv("c106/icecream.csv")
# line_chart = px.scatter(data, x="Temperature", y="Ice-creamSales",)
# line_chart.show()

def getdata(data_path):
    ice_cream = []
    temperature = []
    
    with open(data_path)as f:
        freader= csv.DictReader(f)
        for i in freader:
            temperature.append(float(i["Temperature"]))
            ice_cream.append(float(i["Ice-creamSales"]))
    
    return{"x":ice_cream,"y":temperature}

def findcorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])
    
def setup():
    data_path = "c106/icecream.csv"
    data_source = getdata(data_path)
    findcorrelation(data_source)
    
setup()