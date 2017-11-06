#get raw data from txt file
'''
import Mystring as ss
#open this file, and read raw data from it
src = open("acc_raw_data.txt", 'r')

#will write raw data to this file
dst = open("dst.txt", 'w')

line = src.readline()

while line:
    b = ss.GetWantedPartH( line, "[", "]" )
    dst.write( b+'\n' )
    print(b)
    line = src.readline()
# b = ss.GetWantedPartH( a, "[", "]" )

src.close()
dst.close()
'''

import matplotlib.pyplot as plt
import numpy as np

x = []   #x axis raw data
y = []   #y axis raw data
z = []   #z axis raw data

#data in the txt should be as the format x,y,z, comma seperate each data
src = open("dst.txt", 'r')

line = src.readline()

print(line)
line_num = 1
# get x, y, z data, save them in array
while line:
    comma = []
    for i in range( 0, len(line) ):
        if line[i] == ',':
            comma.append(i)
    # print(comma)
    # print("{0},{1},{2}".format(float(line[0:comma[0]-1]), float(line[comma[0]+1:comma[1]]), float(line[comma[1]+1:len(line)]) ))
    x.append(float(line[0:comma[0]-1]))
    y.append(float(line[comma[0]+1:comma[1]]))
    z.append(float(line[comma[1]+1:len(line)]))
    line = src.readline()
    line_num += 1
x_axis = range(0, line_num-1, 1)


#Draw each line in the same x-axis
#x raw data
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_axis, x, 'r')
ax.set_xlabel("pointer number")
ax.set_ylabel("x raw data")

#y raw data
ay = ax.twinx()
ay.set_ylabel("y raw data")
ay.plot(x_axis, y, 'g')

#z raw data
az = ax.twinx()
az.set_ylabel("z raw data")
az.plot(x_axis, z, 'b')
plt.show()

