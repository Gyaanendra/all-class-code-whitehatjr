import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#using matplotlib
data = pd.read_csv("c103/data.csv")
data.plot(kind = 'bar', x = 'Population', y = 'InternetUsers')
plt.show()

#usong poltly
data = pd.read_csv("c103/data.csv")
line_chart = px.bar(data, x="Population", y="InternetUsers",)
line_chart.show()