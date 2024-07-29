#============================LAB=============================
'''question.1 pyhton program based on multiple condition by using numpy.'''
'''find day temp between 35(hot day) to 5(cold day)'''
import numpy as np

# Given temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identifying hot days (temperature > 35 degrees Celsius)
hot_days = np.where(temperatures > 35)[0]

# Identifying cold days (temperature < 5 degrees Celsius)
cold_days = np.where(temperatures < 5)[0]

# Combining the indices of hot and cold days
extreme_days = np.sort(np.concatenate((hot_days, cold_days)))
print("Hot days (indices):", hot_days)
print("Cold days (indices):", cold_days)
print("Extreme temperature days (indices):", extreme_days)

print("===================================================================")
#=============================================================================
#question 2
import numpy as np

# Given monthly sales data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the array to have 4 rows (quarters) and 3 columns (months per quarter)
quarterly_sales = monthly_sales.reshape(4, 3)

print("Quarterly Sales Data:")
print(quarterly_sales)
print("===================================================================")
#=============================================================================
#question 3
import numpy as np

# Given customer data
customer_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
last_purchase_days_ago = np.array([5, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Customers who made a purchase in the last 30 days
recent_customers = customer_ids[last_purchase_days_ago <= 30]

# Customers who haven't made a purchase in the last 30 days
non_recent_customers = customer_ids[last_purchase_days_ago > 30]

print("Customers who made a purchase in the last 30 days:", recent_customers)
print("Customers who haven't made a purchase in the last 30 days:", non_recent_customers)
print("===================================================================")
#=============================================================================
import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine the two datasets
all_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

print("Comprehensive Employee Dataset:\n", all_employees)

print("===================================================================")
#=============================================================================
#...........................ASSIGNMENT......................................
#ques.1

import numpy as np

# Given list of NumPy arrays
arrays_list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

# Compute the mean of each array
means = [np.mean(arr) for arr in arrays_list]

# Print the means
print("Means of each array:", means)
print("===================================================================")
#=============================================================================

#ques.2
import numpy as np

# Given NumPy array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Compute the median of the array
median_value = np.median(x_odd)

print("Median of the array:", median_value)
print("===================================================================")
#==================================================================

#ques3
import numpy as np

# Given list
arr = [20, 2, 7, 1, 34]

# Convert the list to a NumPy array
arr = np.array(arr)

# Compute the standard deviation of the array
std_dev = np.std(arr)

print("Standard deviation of the array:", std_dev)
#==================================================================


