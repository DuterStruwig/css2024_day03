# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:34:56 2024

@author: duter
"""
import numpy as np
import matplotlib.pyplot as plt

# Conventional python - for loop

for i in range(1,11):
    print(i)
    
"""
1
2
3
4
5
6
7
8
9
10
"""

# numpy - arange

for i in np.arange(1,11,0.5):
    print(i)
    
"""
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
5.5
6.0
6.5
7.0
7.5
8.0
8.5
9.0
9.5
10.0
10.5
"""

# squaring the numbers from 1 to 5

squares = []
for i in range(1,6):
    squares.append(i**2)
    
print(squares)

"""
[1, 4, 9, 16, 25]
"""

squares2 = np.arange(1,6)**2
print(squares2)

"""
[ 1  4  9 16 25]
"""

x = np.arange(1,6)

print(x)

"""
[1 2 3 4 5]
"""

y = x ** 2
print(y)

"""
[ 1  4  9 16 25]
"""

plt.plot(x, y, "r*")
plt.show()

print("Shape of x:")
print(x.shape)
print("Shape of y:")
print(y.shape)

"""
Shape of x:
(5,)
Shape of y:
(5,)
"""

print(x + y)

"""
[ 2  6 12 20 30]
"""

print(x * y)

"""
[  1   8  27  64 125]
"""
#Dot product
print(x.dot(y))

"""
225
"""
#Cross product
print(np.matmul(x,y))

"""
225
"""

alist = [1, 2, 5, 6, 15, 22]
data = np.array(alist)
print(data)

"""
[ 1  2  5  6 15 22]
"""

data2 = data.reshape([2,3])
print(data2)

"""
[[ 1  2  5]
 [ 6 15 22]]
"""

data3 = np.reshape(data,[2,3])
print(data3)

"""
[[ 1  2  5]
 [ 6 15 22]]
"""

data4 = data2 + data3
print(data4)

"""
[[ 2  4 10]
 [12 30 44]]
"""

alist2 = [[1,2,5],[6,15,22]]
data5 = np.array(alist2)
print(data5)

"""
[[ 1  2  5]
 [ 6 15 22]]
"""

print(data5.T)

"""
[[ 1  6]
 [ 2 15]
 [ 5 22]]
"""

data6 = np.matmul(data2.T,data3) #matrix multiplication
print(data6)

"""
[[ 37  92 137]
 [ 92 229 340]
 [137 340 509]]
"""

crossdata = np.cross(data2[0,:],data3[1,:])
print(crossdata)

"""
[-31   8   3]
"""

a = np.array([[1,2,3],[4,5,6],[7,8,-9]])
b = np.array([3,-4,2])
d = np.linalg.det(a)
if(d>0):
    print(f"d = {d}, so this matrix is solvable")
    
"""
d = 53.999999999999986, so this matrix is solvable
"""

sol = np.linalg.solve(a,b)
print(sol)

"""
[-8.38888889  6.77777778 -0.72222222]
"""



