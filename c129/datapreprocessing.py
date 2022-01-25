import pandas as pd 
import csv 


data = []

with open("c129/dataset_2.csv") as f:
    f_read = csv.reader(f)
    for i in f_read:
         data.append(i)
 
headers = data[0]
planet_data = data[1:]       

# to convert all planet names to lower case
for n in planet_data:
    n[2]=n[2].lower()
    
# to sort the data in alpabetical order
planet_data.sort(key=lambda planet_data:planet_data[2])


# to write the modified data in csv file 
with open("sorted_data.csv","a+") as t:
    t_writer = csv.writer(t)
    t_writer.writerow(headers)
    t_writer.writerows(planet_data)
    
    