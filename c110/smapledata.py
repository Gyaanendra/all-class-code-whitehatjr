import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random as ran 

data_read = pd.read_csv("c110/data.csv")

data_list = data_read["temp"].to_list()

mean = st.mean(data_list)

data_plot = ff.create_distplot([data_list],["smapledata"],show_hist=False)
data_plot.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.5], mode="lines", name="MEAN"))
# data_plot.show()

samples = []

for i in range(0,100):
    random_index = ran.randint(0,len(data_list))
    value = data_list[random_index]
    samples.append(value)
    
samples_mean = st.mean(samples)
samples_std = st.stdev(samples)

print( samples_mean, samples_std)

# to colllect hundred random data sample for 1000 time

def randommean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = ran.randint(0,len(data_list))
        value = data_list[random_index]
        data_set.append(value)
    data_set_mean = st.mean(data_set)
    return data_set_mean
    
    
def plot_the_graph(mean_set):
    data_sample_set_mean = mean_set
    data_sample_set_mean_plot_graph = ff.create_distplot([data_sample_set_mean],["data_sample_set_mean"],show_hist=False)
    data_sample_set_mean_plot_graph.show()
    
    
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = randommean(100)
        mean_list.append(set_of_mean)
    plot_the_graph(mean_list)
    
    
setup()