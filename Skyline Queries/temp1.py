import csv
import operator
import math
import matplotlib.pyplot as plt


f= open('points.txt','rb')
lines=csv.reader(f)
data=list(lines)
# print data
# print len(data)
x_cord=[]
y_cord=[]
print data[1]
print len(data[1])
for i in range (len(data)):
	for j in range(0,3):
		if(j != 0):
			data[i][j]=int(data[i][j])
		if(j==1):
			x_cord.append(data[i][j])
		if(j==2):
			y_cord.append(data[i][j])
print data
print x_cord
print y_cord
plt.plot(x_cord,y_cord,'ro')
plt.axis([0,max(x_cord) + 2,0,max(y_cord) + 2])
plt.show()