import csv


with open("class104.csv",newline='') as f:
    v = csv.reader(f)
    #to convert data in list 
    data_file = list(v)
    
# to remove the title
data_file.pop(0)

new_data=[]
for i in range(len(data_file)):
    Height = data_file[i][1]
    new_data.append(float(Height))
    
# to find mean 
n = len(new_data)
total = 0

for g in new_data:
    total +=g
    
mean = total/n
print(str(mean))
