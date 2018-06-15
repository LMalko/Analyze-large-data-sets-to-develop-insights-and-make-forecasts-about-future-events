import numpy

my_list = [1, 2, 3]
np_list = numpy.array(my_list)

print(np_list)
my_mat = numpy.array([[1,2,3], [4,5,6], [7,8,9]])

print(my_mat)

print(numpy.arange(0, 10))
print(numpy.arange(0, 10, 3))
print(numpy.zeros(3))
print(numpy.zeros((5, 7)))
print(numpy.ones((5, 7)))

print(numpy.ones(10) * 5)

# lineary spaced points
print("LINSPACE\n\n", numpy.linspace(0, 26, 10))

print("EYE\n\n" , numpy.eye(5))

print(numpy.random.rand(6))
print(numpy.random.rand(3, 6))

print(numpy.random.randn(6))
print(numpy.random.randn(3, 6))

print(numpy.random.randint(1, 20, 5))

print("\nMATRIX\n")
print(numpy.linspace(0.01, 1, 100).reshape(10, 10))

print(numpy.arange(1,101).reshape(10,10) / 100)




print("\nRESHAPE\n\n")

arr = numpy.arange(0, 25)
print(arr)

print(arr.reshape(5,5))

print(arr.max())
# Index location
print(arr.argmax())
print(arr.min())
print(arr.argmin())

print(arr.shape)
arr = arr.reshape(5,5)
print(arr.shape)

print(arr.dtype)


arr = numpy.arange(0, 11)

print("BROADCAST\n\n")

arr[0:5] = 100

print(arr)

arr_2d = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print(arr_2d)

print(arr_2d[0][0])
print(arr_2d[0, 0])

# Grab first 2 columns, from element 1 till end.
print(arr_2d[:2, 1:])

print("\nCONDITIONAL SELECTION\n")

arr = numpy.arange(0, 11)
bool_arr = numpy.arange(0, 11)

print(bool_arr > 5)

print(arr[arr > 5])


print(numpy.arange(50).reshape(5, 10))

print("\nNUMPY OPERATIONS\n")

arr = numpy.arange(0, 11)

print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr + 100)
# print(arr / arr)
print(numpy.sqrt(arr))
print(numpy.exp(arr))
print(numpy.std(arr))
print(numpy.max(arr))


print(numpy.sin(arr))


print("-" * 30)

print(numpy.arange(1,26).reshape(5,5))
print(numpy.linspace(1, 25, 25).reshape(5,5))

print(numpy.arange(1,26).reshape(5,5)[:3,1:2])
print(numpy.arange(1,26).reshape(5,5)[2:, 1] - 10)

print(numpy.arange(1,26).reshape(5,5)[4:])
print(numpy.arange(1,26).reshape(5,5)[4,:])



# Sum of all columns seperately
print(numpy.arange(1,26).reshape(5,5).sum(axis=0))
