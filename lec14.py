#=================================where()===========================

'''1. np.where():
np.where() is used to find the indices where a specified condition is True in an array.
Syntax:
numpy.where(condition, x, y)'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# Find indices where elements are greater than 3
indices = np.where(arr > 3)
print(indices)

#======================================transpose()=========================
'''2.np.transpose():
np.transpose() is used to transpose or permute the dimensions of an array. It swaps
rows and columns.'''
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
# Transpose the array (swap rows and columns)
transposed_arr = np.transpose(arr)
print(transposed_arr)

#========================================mean()==============================
'''3. np.mean():
np.mean() calculates the mean (average) value of the elements in an array along a
specified axis.'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# Calculate the mean of the array
mean_value = np.mean(arr)
print(mean_value)


#=======================================argmax()=============================
'''4. np.argmax() and np.argmin():These functions are used to find the indices of the
maximum and minimum values in an array, respectively.'''
import numpy as np
arr = np.array([1, 4, 2, 9, 7, 5])
# Find the index of the maximum value
max_index = np.argmax(arr)
# Find the index of the minimum value
min_index = np.argmin(arr)
print("Index of maximum value:", max_index)
print("Index of minimum value:", min_index)


#=======================================searchsort()==========================
'''. np.searchsorted():The np.searchsorted() function is used to find the indices at which
elements should be inserted to maintain the array's sorted order. It is often used for
binary searching in sorted arrays.'''
import numpy as np
sorted_array = np.array([1, 3, 5, 7, 9])
# Find the index where 6 should be inserted to maintain the sorted order
index = np.searchsorted(sorted_array, 6)
print("Index to insert 6:", index)

#=======================================extract()==============================
'''np.extract():The np.extract() function is used to extract elements from an array that
satisfy a given condition.'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
# Extract elements greater than 3
extracted_elements = np.extract(arr > 3, arr)
print("Elements greater than 3:", extracted_elements)


