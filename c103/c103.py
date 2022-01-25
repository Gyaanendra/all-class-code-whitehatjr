import pandas as pd
import plotly.express as px

#to create a emty data frame object 
df = pd.DataFrame()
print(df)

# to create a list data frame 
colors  = ["blue",'red','green','cyan']
colorsdf = pd.DataFrame(colors)
print(colorsdf)