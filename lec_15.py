#===========================numpy.split()=====================================
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
# Split the array into 3 equal-sized sub-arrays
sub_arrays = np.split(arr, 3)
# Print the sub-arrays
for sub_arr in sub_arrays:
    print(sub_arr)

print("====================================================================")
    
#============================numpy. sort()====================================
import numpy as np
arr = np.array([3, 1, 2, 4, 5])
# Sort the array in ascending order (creates a new sorted array)
sorted_arr = np.sort(arr)
# Print the sorted array
print("Sorted array (ascending):", sorted_arr)

print("====================================================================")

# Sort the array in descending order
sorted_arr_desc = np.sort(arr)[::-1]
# Print the sorted array in descending order
print("Sorted array (descending):", sorted_arr_desc)

print("====================================================================")

#matrix sort
import numpy as np
matrix =np.array([[3,2,1],[6,5,4]])
sorted_materix=np.sort(matrix,axis=1)
print("sorted matrix")
print(sorted_materix)

#====================================numpy.concatenate()===================================
print("====================================================================")

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
# Concatenate arr1 and arr2 along rows (vertical)
result = np.concatenate((arr1, arr2), axis=0)
# Print the concatenated array
print(result)

print("====================================================================")


#===================================numpy.vstack()=============================
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Stack arr1 and arr2 vertically
result = np.vstack((arr1, arr2))
# Print the vertically stacked array
print(result)
print("====================================================================")

#====================================numpy.hstack()============================
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Stack arr1 and arr2 horizontally
result = np.hstack((arr1, arr2))
# Print the horizontally stacked array
print(result)
print("====================================================================")

#=================================Filter===================================
import numpy as np
# Temperature readings (in Celsius)
temperatures = np.array([20.5, 22.0, 19.8, 23.5, 18.0, 24.2, 26.1])
# Filter temperatures within the range of 20°C to 25°C
filtered_temperatures = temperatures[(temperatures >= 20) & (temperatures <= 25)]
print("Filtered Temperatures:")
print(filtered_temperatures)
print("====================================================================")

#========================NumPy Statistical Functions==============================
#============================numpy.mean()====================================
#=============================numpy.median()==================================
#=============================numpy.var()(variance)============================
#=============================np.std() - Standard Deviation:===================
import numpy as np
temperatures = np.array([72, 68, 74, 80, 79, 82, 75])
average_temperature = np.mean(temperatures)
median_tem = np.median(temperatures)
std_temp= np.std(temperatures)
var_temp=np.var(temperatures)
print(temperatures)
print('mean value:',average_temperature)
print('median value:',median_tem)
print(' Standard Deviation:',std_temp)
print('variance:',var_temp)
print("====================================================================")

#==============================numpy.percentile()=================================
'''#numpy.percentile(a, q):a=a: This is the input array or sequence:q= This parameter specifies the percentile(s) to be calculated.:
import numpy as np
test_scores = np.array([65, 75, 80, 85, 90, 92, 94, 95, 96, 98, 100, 102, 104, 106, 108,
110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138])
median = np.percentile(test_scores, 50)
print("Median (50th Percentile):", median)'''
print("====================================================================")

#===================================load(),dump()===================================
import numpy as np
# Sample student scores
scores = np.array([85, 92, 78, 88, 95, 72, 89])
# Save the scores to a file
np.save('student_scores.npy', scores)
# Load the scores from the file
loaded_scores = np.load('student_scores.npy')
print("Original Scores:", scores)
print("Loaded Scores:", loaded_scores)


