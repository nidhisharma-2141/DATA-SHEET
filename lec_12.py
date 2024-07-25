#============================================NUMPY======================================================
'''NumPy, which stands for "Numerical Python," is a popular Python library for numerical and scientific computing.
It provides support for working with large, multi-dimensional arrays and matrices of data, along with a collection of
mathematical functions to operate on these arrays.
NumPy is a fundamental library for data manipulation and analysis in Python and is widely used in various fields such
as data science, machine learning, scientific research, and engineering.

Here are some key features and aspects of NumPy:

* Multi-dimensional Arrays: NumPy's core data structure is the ndarray (short for n-dimensional array). It allows you
to create arrays of various dimensions, including 1D, 2D, and higher-dimensional arrays.

* Efficient and Fast: NumPy is implemented in C and optimized for performance, making it much faster than standard
Python lists when performing array operations. This efficiency is crucial for handling large datasets and complex mathematical computations.'''


import numpy as np

l=[10,30,25,43,21]
array=np.array(l)
print(array)

#=======================================ARRAY CONVERTION===================================
import numpy as np
a=np.array(42)
b=np.array([10,30,25,43,21])
c=np.array([[10,30,25,43,21],[10,30,25,43,21]])
d=np.array([[[10,30,25,43,21],[10,30,25,43,21],[10,30,25,43,21]]])

print("a array",a)
print("b array",b)
print("c array",c)
print("d array",d)

#ndim= used to determine the dimension of array
print("a array dimen",a.ndim)
print("b array dimen",b.ndim)
print("c array dimen",c.ndim)
print("d array dimen",d.ndim)



#shape= determine the number of rows and column
#1-dimension=vector
#2-dimension=metrix
#3-dimension=tensor

#=============================================slicing array=================================
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
sarr=arr[1:5]
print(arr)
print(sarr)

sarr[2]=100
print(arr)
print(sarr)
#============================================copy and view=====================================
'''The Difference Between Copy and View
The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will
not affect the copy.
The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original
array will affect the view.'''
#COPY()
import numpy as np
arr =np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)

#VIEW()
import numpy as mp
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42
print(arr)
print(x)
#============================================numpy.zeros()=====================================
'''The numpy.zeros() function is one of the most significant functions which is used in machine learning
programs widely. This function is used to generate an array containing zeros.
The numpy.zeros() function provide a new array of given shape and type, which is filled with zeros.'''
import numpy as np
a=np.zeros(6)



#========================================numpy.ones()===============================================
'''The NumPy ones() function in Python is used to create an array of the specified shape and type, where all the elements are set to 1.
This function is very similar to zeros(). The ones() function takes three arguments and returns the array filled with value 1.
In this article, I will explain how to use the NumPy ones() function with examples.'''
import numpy as np
arr3=[1,2,3,4,5,6,7,8,9]
arr3-np.ones((5,2))

print(arr3)

arr np.ones(7)

#Example 2: Create a 10 array of ones #with 5 elements and integer data type

arr np.ones (5, dtype int)

#Example 3: An aray with 6 ones and integer data type

arr np.ones((6,), pitype=int)

#Example 4: Create two-dimensional array with ones

arr np.ones((3, 4))

#Example 5: Use two-dimensional array with ones

arr = (3,4)

#=========================================================numpy.eye()=======================
'''The eye tool returns a 2-D array with 1's as the diagonal and e's elsewhere.
The diagonal can be main, upper, or lower depending on the optional parameter k.
A positive k is for the upper diagonal, a negative k is for the lower, and a 0 ek (default) is for the main diagonal.'''
import numpy as np
aar4=[]
arr4=np.eye(3)
print(arr4)

arr4=np.eye(3,4)
print(arr4)






