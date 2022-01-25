import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

#using matplotlib
data = pd.read_csv("c103/line_chart.csv")
data.plot(kind = 'line', x = 'Year', y = 'Per capita income')
plt.show()



#usong poltly
data = pd.read_csv("c103/line_chart.csv")
line_chart = px.line(data, x="Year", y="Per capita income",
                     color="Country", title="linechart")
line_chart.show()
