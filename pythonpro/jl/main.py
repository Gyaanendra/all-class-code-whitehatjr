import os
import shutil
import time

with open("hello.txt",'r') as f:
   g = f.read()

print(g)

# f = os.open("hello.txt",'r')
# g = os.read(f)
# print(g)

hl = os.listdir()
print(hl)
cwd = os.getcwd()
print(cwd)

os.mkdir('C:\\Users\\Gyaanendra\\Desktop\\jl\\new')


source = 'C:\\Users\\Gyaanendra\\Desktop\\jl\\test2\\new.txt'
receiver = 'C:\\Users\\Gyaanendra\\Desktop\\jl\\test'


shutil.copy(source, receiver)

k = time.time() 
print(k)