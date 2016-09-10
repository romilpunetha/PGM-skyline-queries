import csv
import operator
import math
from scipy.integrate import quad
import scipy.integrate as integrate
def integrand(x,y):
    return math.sqrt(x*x+y*y)
def func(x,x1,x2):
    return quad(integrand, x1, x2, args=(x))[0]


f= open('points.txt','r')
lines=csv.reader(f)

data=list(lines)
x_cord=[]
y_cord=[]
labels=[]
for i in range(len(data)):
    d=data[i][0].split()
    labels.append(d[0])
    dist=[]
    for i in range (len(data)):
        d=data[i][0].split()
        values1=[]
        values2=[]
        flag1=False
        flag2=False
        for j in range(0,3):
            if(j==1):
                x_cord.append(d[j])
            if( not d[j].isdigit()):
                flag1=True
                values1=d[j].split('-')
                if(j==2):
                    y_cord.append(d[j])
                    if( not d[j].isdigit()):
                        flag2=True
                        values2=d[j].split('-')
                        if flag1 and flag2:
                            result = quad(lambda x: func(x,int(values1[0]),int(values1[1])), int(values2[0]), int(values2[1]))[0]/((int(values1[1])-int(values1[0]))*(int(values2[1])-int(values2[0])))
                        elif flag1:
                            result= integrate.quad(lambda x: math.sqrt(x**2+int(d[2])**2),int(values1[0]),int(values1[1]))[0]/((int(values1[1])-int(values1[0])))
                        elif flag2:
                            result= integrate.quad(lambda x: math.sqrt(x**2+int(d[1])**2),int(values2[0]),int(values2[1]))[0]/((int(values2[1])-int(values2[0])))
                        else:
                            result=math.sqrt(int(d[1])**2+int(d[2])**2)
                    dist.append((d[0],result))
                    dist.sort(key=lambda x:x[1],reverse=True)
print (dist)

'''
plt.plot(x_cord,y_cord,'ro')
i=0
for label in labels:

    plt.annotate(label, xy = (x_cord[i], y_cord[i]), xytext = (-20, 20),textcoords = 'offset points', ha = 'right', va = 'bottom',        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),arrowprops = dict(arrowstyle = '->',connectionstyle = 'arc3,rad=0'))
    i=i+1
    plt.axis([0,max(x_cord) + 2,0,max(y_cord) + 2])
    plt.show()
    '''
