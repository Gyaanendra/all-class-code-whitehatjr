import csv 
import pandas as pd
import plotly.graph_objects as go 

data = pd.read_csv("c107/data.csv")

# Fdata = data.groupby("level")["attempt"].mean()

# bar = go.Figure(go.Bar(x=Fdata, y=["level1","level2","level3","level4"], orientation="h"))
# # bar.show()

studentdata = data.loc[data["student_id"]=="TRL_987"]
sdata = studentdata.groupby("level")["attempt"].mean()

sdatagraph = go.Figure(go.Bar(x=sdata, y=["level1","level2","level3","level4"], orientation="h"))
sdatagraph.show()