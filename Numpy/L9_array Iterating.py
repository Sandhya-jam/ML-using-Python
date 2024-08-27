#Iterate on the elements of the following 1-D array
import numpy as np
arr=np.array([1,2,3])

for x in arr:
    print(x)
# 1
# 2
# 3
#----------------2-D ARRAY---------------
#In a 2-D array it will go through all the rows.
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr: #this gives elements of each row
  print(x)
# [1 2 3]
# [4 5 6]

#To print every element do as below
for x in arr:
      for y in x:
        print(y)  #1 2 3 4 5 6

#----------------3-D ARRAY------------------------
#In 3d array it will go through all 2-d arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
#[[1 2 3][4 5 6]]
#[ 7  8  9] [10 11 12]]

for x in arr:
      for y in x:
        for z in y:
          print(z)  #1 2 3 4 5 6 7 8 9 10 11 12

#-----------------Iterating Arrays Using nditer()--------------
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)  #1 2 3 4 5 6 7 8
  

#-----------Iterating Array With Different Data Types--------

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
# np.bytes_(b'1')
# np.bytes_(b'2')
# np.bytes_(b'3')

#Iterating With Different Step Size
#Iterate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)  #1 3 5 7
  
#----Enumerated Iteration Using ndenumerate()------------
# Enumeration means mentioning sequence number of somethings one by one.
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)  #(0,)1 (1,)2 (2,)3
  
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
# (0, 0) 1
# (0, 1) 2
# (0, 2) 3
# (0, 3) 4
# (1, 0) 5
# (1, 1) 6
# (1, 2) 7
# (1, 3) 8
