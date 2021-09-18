import numpy as nm
print(nm.__version__)
arr = nm.array([1,2,3,4,6,8])
print(arr)
print(type(arr))

#Creation of zero dimentional array
arr = nm.array(10)
print(arr)
print(arr.ndim)


#Creation of one dimentional array
arr = nm.array([1000,2,3,4,6,8])
print(arr)
print(arr.ndim)
print(arr[0])
print(arr[1])

#Creation of two dimentional array
arr = nm.array([[1,2,3,4,6,8],[3,4,5,6,7,9]])
print(arr.ndim)

print("This will print fourth element from 1st dimension(n x m, where index for n,m starts with 0):"+str(arr[0,3]))
#Creation of three dimentional array
arr = nm.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#The first number represents the first dimension which contains two array's
#That number is [[1,2],[3,4]]
#The second number represents the second dimension which contains two array's
#That number is [1,2]
#The third number represents the third dimension which contains two elements
# #That number is [1,2]
#Now to extract last elelment from the last column we will use nxmxp where n=0,m=1,p=1
print(arr.ndim)
print("This will print fourth element from 1st dimension(n x m x p, where index for n,m starts with 0):"+str(arr[1,1,1]))
#Creation of n dimentional array
arr = nm.array([1,2,3,4,6,8],ndmin=7)
print(arr)
print(arr.ndim)