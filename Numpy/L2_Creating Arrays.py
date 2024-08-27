import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)  #[1 2 3 4 5]
print(type(arr))  #<class 'numpy.ndarray'>

#If list,tuple or any array like object is passed into array method,it will convert into array
arr1=np.array((1,2,4,5))
print(arr1) #[1 2 4 5]

#TYPES OF ARRAYS:
#0-D:
A=np.array(42)
print(A)

#1-D:
B=np.array([1,4,5,6])
print(B)

#2-D:
C=np.array([[1,2,3],[4,5,6]])
print(C)

#3-D:
D=np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(D)

#Check Number of Dimensi0ns:
print(A.ndim) #0
print(B.ndim) #1
print(C.ndim) #2
print(D.ndim) #3

#HIGHER DIMENSIONAL ARRAYS
#When the array is created, you can define the number of dimensions by using the ndmin argument.
Arr=np.array([1,2,3,4,5],ndmin=5)

print(Arr) #[[[[[1 2 3 4 5]]]]]
print("No.of Dimensions are: ",arr.ndim) #5

