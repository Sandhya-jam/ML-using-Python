#COPY:
#Make a copy, change the original array, and display both arrays:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) #[42 2 3 4 5]
print(x)   #[1 2 3 4 5]

#VIEW
x = arr.view()
arr[0] = 21

print(arr) #[21 2 3 4 5]
print(x)   #[21 2 3 4 5]

#Make a view, change the view, and display both arrays:
x = arr.view()
x[0] = 31

print(arr) #[31  2  3  4  5]
print(x)   #[31  2  3  4  5]

#Check if Array Owns its Data
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

x = arr.copy()
y = arr.view()

print(x.base) #None
print(y.base) #[1 2 3 4 5]


