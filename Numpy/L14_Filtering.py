#-----------Filtering Arrays----------------
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.


# Create an array from the elements on index 0 and 2
import numpy as np

arr=np.array([41,42,43,44])
x=[True,False,True,False]
newarr=arr[x]

print(newarr) #[41 43]

#Create a filter array that will return only values higher than 42:
filter_arr=[]
for ele in arr:
    if ele>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
newarr=arr[filter_arr]
print(filter_arr) #[False, False, True, True]
print(newarr)   #[43 44]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr=[]
for ele in arr:
    if ele%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr=arr[filter_arr]
print(filter_arr) #[False, True, False, True, False, True, False]
print(newarr) #[2 4 6]

#------------------Creating Filter Directly From Array---------

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr) #[False, True, False, True, False, True, False]
print(newarr) #[2 4 6]
