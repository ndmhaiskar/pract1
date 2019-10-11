def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    y = []
    for i in range(n):
        for j in x[i:i+width]]
    return y
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.

x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))





















def intersect(list1,list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result



from math import sqrt
import random


def distance(x,y):
    distance = sqrt((y[0]-x[0])**2+(y[1]-x[1])**2)
    return distance

def rand():
   # define `rand` here!
    rnum = random.uniform(-1,1)
    return rnum

def in_circle(x,origin=[0,0]):
    # distance = sqrt((x[0]-origin[0])**2+(x[1]-origin[1])**2)
    space = distance(x,[0,0])
    if space < 1:
        return True
    else:
        return False

in_circle((1,1),[0,0])

inside = []
R = 10000
for i in range(R):
    inside.append((rand(),rand()))

results = []
for i in inside:
    results.append(in_circle(i,[0,0]))
proportion = results.count(True)/R
print("The proportion of two areas is: "+str(proportion))

difference = proportion - (math.pi/4)
