# First thing first import numpy:
import numpy as np

# Part 1 (Creating Numby Arrays) 
''' 
1)Using Built-in Methods: Create the following arrays using NumPy built-in functions:
○ An array of numbers from 0 to 20 with a step of 2.
○ A 3x3 identity matrix.
○ A 4x4 array filled with ones.
○ An array of 10 equally spaced numbers between 5 and 50.
'''

# Any Array from 0 to 20 step by 2:
Any_Array = np.arange(0,21,2)
print(Any_Array)

# A 3x3 identity matrix:
Identity_3x3 = np.eye(3)
print(Identity_3x3)

# A 4x4 ones matrix:
ones_4x4 = np.ones((4,4))
print(ones_4x4)

# speaced by 10 between 5 and 50:
speaced_array = np.linspace(5,50,10)
print(speaced_array)

'''
2)Creating Arrays from Lists
○ Convert a Python list [10, 20, 30, 40, 50] into a NumPy array.
○ Generate a 3x3 matrix of random numbers using rand(), randn(), and randint().
'''

# convert list to array:
my_list = [10, 20, 30, 40, 50]
list_to_Array = np.array(my_list)
print(list_to_Array)

# Generate a 3x3 matrix of random numbers:

rand_matrix = np.random.rand(7, 7)
print(rand_matrix)
randn_matrix = np.random.randn(5, 5)
print(randn_matrix)
randint_matrix = np.random.randint(0, 100, (5, 5))
print(randint_matrix)

'''
3)Array Attributes
○ Print the shape, size, and data type of an array you created in the previous steps.
'''
# change a shape, size and data of an array I created above:

changed_array = np.append(list_to_Array, 60)
changed_shape = changed_array.reshape(2,3)
print(changed_shape)

#change_size_array =  np.resize(changed_shape(2,4))
#print(change_size_array)                          #It doesn't working

change_type = list_to_Array.astype(bool)
print(change_type)

##################################################################################

# Part 2 (Indexing and Selection)

'''
1.Basic Indexing and Selection
○ Create a NumPy array [5, 10, 15, 20, 25, 30]. Select and print:
■ The first element.
■ The last three elements.
■ The elements at index positions 1 to 4.
'''

arr_mine = np.array([5, 10, 15, 20, 25, 30])
first_element = arr_mine[0]
print(first_element)
last_three = arr_mine[-3:]
print(last_three)
middle_elements = arr_mine[1:4]

'''
2. Slicing and Views
○ Create a 3x3 matrix from np.arange(1, 10).reshape(3, 3) and:
■ Select the second row.
■ Select the first two columns.
■ Extract a sub-matrix of shape (2,2).
'''

you_mat = np.arange(1, 10).reshape(3, 3)
print(you_mat)

second_row = you_mat[1, :]
print(second_row)

first_two_cols = you_mat[:, :2]
print(first_two_cols)

sub_matrix_2x2 = you_mat[:2, :2]
print(sub_matrix_2x2)

'''
3. Broadcasting
○ Create a 3x3 matrix and add 10 to every element.
○ Multiply the first column by 2.
'''

my_mat = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("Original Matrix:")
print(my_mat)

mat_plus_10 = my_mat + 10
print(mat_plus_10)

modified_mat = my_mat.copy()
modified_mat[:, 0] = modified_mat[:, 0] * 2
print(modified_mat)

'''
4.Copying Arrays
○ Create a NumPy array and demonstrate the difference between shallow and deep
copies.+
'''

original = np.array([10, 20, 30, 40, 50])
print(original)

shallow = original.view()
shallow[0] = 999
print(original)
print(shallow)

deep = original.copy()
deep[1] = 777  
print(original)
print( deep)

'''
5.Fancy Indexing
○ Given arr = np.arange(10, 101, 10), select elements at index [0, 3, 5].
'''

Array_1 = np.arange(10, 101, 10)
print(Array_1)

selected_elements = Array_1[[0, 3, 5]]
print(selected_elements)

###################################################################################

# Part 3 (NumPy Operations)

'''
1. Mathematical Functions
○ Find the maximum, minimum, index of max, and index of min for the array [3, 7, 2,
9, 12, 5, 10].
'''
Array_2 = np.array([6,7,3,2,5,8,1,9])

max_value = np.max(Array_2)
print(max_value)
min_value = np.min(Array_2)
print(min_value)
index_max = np.argmax(Array_2)
print(index_max)
index_min = np.argmin(Array_2)
print(index_min)

'''
2. Universal Array Functions
○ 1. Given arr = np.array([1, 2, 3, 4, 5]), apply the following functions:
a. Square root (sqrt())
b. Exponential (exp())
c. Sine (sin())
d. Logarithm (log())
'''

sqrt_arr = np.sqrt(Array_2)
print(sqrt_arr)
exp_arr = np.exp(Array_2)
print(exp_arr)
sin_arr = np.sin(Array_2)
print(sin_arr)
log_arr = np.log(Array_2)
print(log_arr)