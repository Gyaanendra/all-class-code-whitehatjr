import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import statistics as st
import random
import pandas as pd
import csv

data = pd.read_csv("c112/savings.csv")
data_plot_graph = px.scatter(data , y = "quant_saved" , color= "rem_any" )
# data_plot_graph.show()


saving_list = data["rem_any"].tolist()
total_data = len(saving_list)
rem_given = 0

for i in saving_list:
    if i == 1:
        rem_given +=1
    
rem_notgiven = total_data - rem_given

data_bar_graph = go.Figure(go.Bar(x=["remineded","not-remineded"], y =[rem_given,rem_notgiven]))
# data_bar_graph.show()

quant_saved_list = data["quant_saved"].tolist()

quant_saved_list_mean = st.mean(quant_saved_list)
print(quant_saved_list_mean)

quant_saved_list_median = st.median(quant_saved_list)
print(quant_saved_list_median)

quant_saved_list_mode = st.median(quant_saved_list)
print(quant_saved_list_mode) 

data_age_max = data["age"].tolist()

print(max(data_age_max))
# data_age_max_plot =  px.scatter(data_age_max )
# data_age_max_plot.show()


