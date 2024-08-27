#-----------------Searching Arrays-------
# To search an array, use the where() method.
import numpy as np

arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)

print(x) #(array([3, 5, 6]),)   Which means that the value 4 is present at index 3, 5, and 6

#Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x=np.where(arr%2==0)
print(x) #(array([1, 3, 5, 7]),)

#----------Search Sorted---------------
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

# The searchsorted() method is assumed to be used on sorted arrays

import numpy as np

arr = np.array([6, 7, 8, 9])
x=np.searchsorted(arr,7)
print(x) #1

#The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

#-------Search From the Right Side----------------
# By default the left most index is returned, but we can give side='right' to return the right most index instead.

x = np.searchsorted(arr, 7, side='right')
print(x) #2


#--------Multiple Values----------------
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x) #[1 2 3]