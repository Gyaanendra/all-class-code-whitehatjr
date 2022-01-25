import csv
from collections import Counter

from numpy import greater

with open("SOCR-HeightWeight.csv", newline='') as f:
    v = csv.reader(f)
    # to convert data in list
    data_file = list(v)

# to remove the title
data_file.pop(0)

for i in range(len(data_file)):
    Height = data_file[i][1]
    data_file.append(Height)


# to find mode
data_counter = Counter(data_file)
mode_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0,
}

for i,occur in data_counter.items():
    if 50 < float(i)<60:
        mode_range["50-60"]+=occur
    elif 60 < float(i)<70:
        mode_range["60-70"]+=occur
    elif 70 < float(i)<80:
        mode_range["70-80"]+=occur
        
        
range,occurrence = 0,0

for r ,o in mode_range.items():
    if o >occurrence:
        range,occurrence =[int(range.split("-")[0]), int(range.split("-")[1])], o
    
mode =  float((range[0]+range[1])/2)
print(mode)