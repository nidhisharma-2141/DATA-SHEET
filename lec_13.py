#=====================randint()====================
'''to genrate random number'''
import numpy as n
rand=n.random.randint(0,10,2)
print(rand)



import numpy as n
rand=n.random.randint(4)
print(rand)

a=n.random.randint(2,3)
print(a)

arr=n.random.randint(0,100,10)
print(arr)



#=======================reshape()=====================
'''the reshape function in NumPy allows you to change the shape(dimenions) of an
array without changing its data.'''
import numpy as n
arr=n.random.randint(0,100,12)
print(arr)
arr=arr.reshape(4,3)
print(arr)
print('array value is',arr[0][1])
print('array value is ',arr[1][0])
print(arr.shape)
arr=arr.reshape(-1,4)
print(arr)
arr=arr.reshape(2,-1)
print(arr)

#====================seed()================================
import numpy as n
n.random.seed(145)
arr=n.random.randint(0,100,12)
print(arr)


import numpy as n
n.random.seed(145)
arr=n.random.randint(0,500,30).reshape(6,5)
print(arr)
print(arr[2:,2:])
print(arr[3:5,2:4])

import numpy as n
ar=n.array([1,20,5,9,3,4,8,5,6,2,25,2,2265,3,33])
slicing=arr[4:9]
print("new slicing",slicing)
print("new array",ar)
print(type(slicing))
print(type(ar))
slicing[:]=0
print("old slicing",slicing)
print("old array",ar)


#===========================arange()======================
# genrate sequence
import numpy as n
arr=n.arange(1,15)
print(ar)
print(ar[ar%2==0])
print(ar[ar%2!=0])
print(ar[ar>8])
ar[ar%2==0]=0
print(ar)
arr=n.arange(1,8)
print(arr+2)
print(arr*2)
print(arr**2)

#=====================some maths function=================
import numpy as n
arr=n.array([10,20,30,25,6,2])
print(n.min(arr))
print(n.max(arr))
print(n.argmin(arr))
print(n.argmax(arr))
print(n.sqrt(arr))
print(n.sin(arr))
print(n.cos(arr))

#============================================================
import numpy as n
n.random.seed(122)
mat=n.random.randint(1,21,9).reshape(3,3)
print(mat)
print(n.sum(mat))
print(n.cumsum(mat))
print(n.min(mat))
print(n.max(mat))
print('===================================------------===============================')
print(n.sum(mat,axis=0))
print(n.max(mat,axis=0))
print(n.min(mat,axis=0))
print(n.cumsum(mat,axis=0))

#=============================================================

import numpy as n
n.random.seed(122)
mat=n.random.randint(1,21,10)
print(mat)
n.random.shuffle(mat)
print(mat)
print(n.unique(mat,return_index=True,return_counts=True))
print(n.unique(mat).size)



