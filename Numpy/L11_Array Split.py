#-------------Splitting NumPy Arrays---------------
# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

#Split the array in 3 parts:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr) #[array([1, 2]), array([3, 4]), array([5, 6])]

#If the array has less elements than required, it will adjust from the end accordingly.
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr) #[array([1, 2]), array([3, 4]), array([5]), array([6])]

#----------------NOTE-----------------
# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.

# Access the splitted arrays:

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)

print(newarr[0]) #[1 2]
print(newarr[1]) #[3 4]
print(newarr[2]) #[5 6]

#------------2-D ARRAY-------------
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)
print(newarr) #[array([[1, 2],[3, 4]]), array([[5, 6], [7, 8]]), array([[ 9, 10],[11, 12]])]

# Split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)
print(newarr)
# [array([[ 1],[ 4],[ 7],[10],[13],[16]]), array([[ 2],[ 5],[ 8],[11],[14],[17]]), array([[ 3],[ 6],[ 9],[12],[15],[18]])]


#-----NOTE------------------
# An alternate solution is using hsplit() opposite of hstack()
#  Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
