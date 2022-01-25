import os
import shutil
import time

ctimes = os.stat('C:\\Users\\Gyaanendra\\Desktop\\jl\\test1\\new.txt').st_ctime

print(ctimes)

time.ctime(ctimes)

h = os.remove('C:\\Users\\Gyaanendra\\Desktop\\jl\\test1\\new.txt')

g = os.path.exists('C:\\Users\\Gyaanendra\\Desktop\\jl\\test1')
print(g)