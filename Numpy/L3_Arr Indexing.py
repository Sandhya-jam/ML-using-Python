#Array indexing is the same as accessing an array element.
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0]) #1
print(arr[1]) #2

#2D ARRAYS:
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
arr1=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("1st element on 2nd row",arr1[1,0]) #1st element on 2nd row 6

#3D ARRAYS:
arr2=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2[0,1,2]) #6


#NEGATIVE INDEXING:
#Use negative indexing to access an array from the end.

print('Last element from 2nd dim',arr1[1,-1]) #Last element from 2nd dim 10

