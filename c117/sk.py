import seaborn as sns
from sklearn.metrics import confusion_matrix as CXM
import matplotlib.pyplot as plt 

actual_data = ["notsick","sick","notsick","sick","notsick","sick","notsick","sick","notsick","sick","notsick","sick","notsick","sick","notsick","sick","notsick","sick","notsick","sick"]

predicted_data = ["sick","sick","notsick","sick","sick","sick","sick","sick","sick","sick","sick","sick","sick","sick","sick","notsick","sick","notsick","sick","notsick"]

labels = ["notsick","sick"]

cm_result = CXM(actual_data,predicted_data)

graph_heat_map  = plt.subplot()
sns.heatmap(cm_result, annot=True, ax = graph_heat_map)
graph_heat_map.set_xlabel("predict")
graph_heat_map.set_ylabel("actual")
graph_heat_map.set_title("confusion matrix")
graph_heat_map.xaxis.set_ticklabels(labels); graph_heat_map.yaxis.set_ticklabels(labels)
# plt.show()

true_positve = 7
false_positve = 9
true_negative = 1
false_negative = 3

result = (true_positve+true_negative)/(true_positve+true_negative+false_negative+false_positve)
print(result)

