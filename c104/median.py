import csv


with open("c104/SOCR-HeightWeight.csv",newline='') as f:
    v = csv.reader(f)
    #to convert data in list 
    data_file = list(v)
    
# to remove the title
data_file.pop(0)

for i in range(len(data_file)):
    Height = data_file[i][1]
    data_file.append(Height)
    
# to find median
data_file.sort()

num =  len(data_file)

if num%2 == 0 :
    m1 = float(data_file[num//2])
    m2 = float(data_file[num//2-1])
    median = (m1+m2)/2
else :
    median = data_file[num//2]
    
print(str(median))