# let's import numpy
import numpy as np

# u want a zeros array
zeros_arr = np.zeros(10)
print(zeros_arr)

# and ones one oki
add_ones_arr = np.ones(10)
print(add_ones_arr)

# arry of 10 fives ? hmm 
ten_fives_arry = np.full(10,5)
print(ten_fives_arry)

# road 10 to 50
ten_fifty = np.arange(9,50)
print(ten_fifty)

# evens?
ten_fifty_even_edition = np.arange(9,50,2)
print(ten_fifty_even_edition)

# 3x3 matrix 
three_X_three = np.arange(0,9).reshape(3,3)
print(three_X_three)

# identity matrix... what?
# oh
identity_matrix = np.eye(3)
print(identity_matrix)

# rand number my fav is .77777777.....
rand_zero_one = np.random.rand()
print(rand_zero_one)

# 25 rand number, no more?
rand_25 = np.random.rand(25)
print(rand_25)

# wierd array 
wierd_array = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(wierd_array)

# linespeace
linespeace_20 = np.linspace(0, 1, 20)
print(linespeace_20)

# hint quest 1
quest_1 = np.arange(12,24).reshape(3,4)
print(quest_1)

# hint quest 2
quest_2 = np.array([2,7,12]).reshape(3,1)
print(quest_2)

# hint quest 3
quest_3 = np.array([21, 22, 23, 24, 25])
print(quest_3)

# hint quest 4
quest_4 = np.arange(16,26).reshape(2,5)
print(quest_4)

# hint quest 5
mat = np.arange(1,26).reshape(5,5)
print(mat)
sum_mat = np.sum(mat)
print(sum_mat)
divin_mat = sum_mat/len(mat)
print(divin_mat)
# or
divin_elements = np.sum(mat)/mat
print(divin_mat)
sum_elements = np.sum(mat, axis=0)
print(sum_elements)