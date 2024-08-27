#DATATYPES IN STRING:
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

#CHECKING DATA TYPES:
#The NumPy array object has a property called dtype that returns the data type of the array:
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype) #int64

arr1=np.array(['apple', 'banana', 'cherry'])
print(arr1.dtype) #<U6

#Creating Arrays With a Defined Data Type
#Create an array with data type string:
arr2 = np.array([1, 2, 3, 4], dtype='S')

print(arr2) #[b'1' b'2' b'3' b'4']
print(arr2.dtype) #|S1

# Create an array with data type 4 bytes integer:
arr3 = np.array([1, 2, 3, 4], dtype='i4')

print(arr3) #[1 2 3 4]
print(arr3.dtype) #int32

# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
#A non integer string like 'a' can not be converted to integer (will raise an error):
# arr = np.array(['a', '2', '3'], dtype='i')


# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method
a = np.array([1.1, 2.1, 3.1])

newarr = a.astype('i')

print(newarr) #[1 2 3]
print(newarr.dtype) #int32
newarr = a.astype(int) #we can do this aslo

newarr = arr.astype(bool)


