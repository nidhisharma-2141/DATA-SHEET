print('=========================lab=============================')

#list conversion into array
import numpy as n
list1=[1,2,3,4,5]
arr= n.array(list1)
print(arr)
print('===========================================================')
# list  convert into array and array  display ,first and last element display ,multiply by 2 a 

import numpy as np

# Convert list to Python array using array()
my_list = [6, 4, 8, 9, 10]
my_array =np. array( my_list)

# Display first and last elements
first_element = my_array[0]
last_element = my_array[-1]

# Multiply all elements by 2
my_array *= 2

print(f"Original list: {my_list}")
print(f"Converted array: {my_array}")
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
print(f"result:{my_array}")

print('===========================================================')
#numpy program to create an array of 10 zeros ,10 ones ,10 fives
import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)

# Create an array of 10 ones
ones_array = np.ones(10)

# Create an array of 10 fives
fives_array = np.ones(10) * 5

# Display the arrays
print("An array of 10 zeros:")
print(zeros_array)

print("\nAn array of 10 ones:")
print(ones_array)

print("\nAn array of 10 fives:")
print(fives_array)
print('===========================================================')
#wapp to  create a 3x3 materix with value 2 to10
import numpy as np


matrix = np.arange(2, 11).reshape(3, 3)

print("3x3 Matrix:")
print(matrix)







