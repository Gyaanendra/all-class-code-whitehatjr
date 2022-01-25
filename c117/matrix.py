from numpy.core.fromnumeric import ravel
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import statistics as st
import random as rd
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split as tts 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score as AS
from sklearn.metrics import confusion_matrix as CXM

data_file = pd.read_csv("c117/heart.csv")

age =  data_file["age"]
target =  data_file["target"]

age_train,age_test,target_train,target_test =  tts(age,target,test_size=0.25,random_state=0)

# to train the data using reshape()
X = np.reshape(age_train.ravel(),(len(age_train),1))
Y = np.reshape(target_train.ravel(),(len(target_train),1))

classifier = LogisticRegression(random_state=0)
classifier.fit(X,Y)

X_test = np.reshape(age_test.ravel(),(len(age_test),1))
Y_test = np.reshape(target_test.ravel(),(len(target_test),1))

y_predict = classifier.predict(X_test)
predict_values = []

for i in y_predict:
    if i == 0:
        predict_values.append("no")
    else:
        predict_values.append("yes")
        
actual_values = []

for x in Y_test.ravel():
    if x == 0:
        actual_values.append("no")
    else:
        actual_values.append("yes")
        
        
# to plot graph data

labels = ["no","yes"]

cm_result = CXM(actual_values,predict_values)

graph_heat_map  = plt.subplot()
sns.heatmap(cm_result, annot=True, ax = graph_heat_map)
graph_heat_map.set_xlabel("predict")
graph_heat_map.set_ylabel("actual")
graph_heat_map.set_title("confusion matrix")
graph_heat_map.xaxis.set_ticklabels(labels); graph_heat_map.yaxis.set_ticklabels(labels)
# plt.show()

true_positve = 36
false_positve = 17
true_negative = 16
false_negative = 7

result = (true_positve+true_negative)/(true_positve+true_negative+false_negative+false_positve)
print(result)
