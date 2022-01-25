import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# using matplotlib
data = pd.read_csv("c103/data.csv")
data.plot(kind = 'scatter', x = 'Country', y = 'Per capita')
plt.show()

# usong poltly
data = pd.read_csv("c103/data.csv")
line_chart = px.scatter(data, x="Country", y="Per capita",size="Percentage",
                        color="Country", size_max=120)
line_chart.show()
