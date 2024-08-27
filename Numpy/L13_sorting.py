#-----------------Sorting Arrays----------
# The NumPy ndarray object has a function called sort(), that will sort a specified array.
import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) #[0 1 2 3]

##########----------NOTE----------#############
# Note: This method returns a copy of the array, leaving the original array unchanged.

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr)) #['apple' 'banana' 'cherry']

arr = np.array([True, False, True])
print(np.sort(arr)) #[False True True]


#------------Sorting a 2-D Array---------
# If you use the sort() method on a 2-D array, both arrays will be sorted:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr)) #[[2 3 4] [0 1 5]]