import numpy as np


example_array = np.array(['Haha', 'why', 'so', 'serous'])
example_array1 = np.array(['ha', 'why', 'you', 'serous'])
print(example_array[0:2], example_array1[:3])
# TODO use pandas and numpy
# negative indexing to move backwards
print(example_array1[-1])
# create a numeric array with 10 items  - list of numbers
numeric_array = np.array(range(1, 101))
print('Array created with 100 numbers: {0}'.format(numeric_array))
print('Picking a specifc number in the array 1/4 of the list = ',numeric_array[24])
last_number = numeric_array[-1]
print('The last element of the list: {0}'.format(last_number))


# TODO WHY USE ARRAYS OVER LIST?
# MULTIDIMENSIONAL ARRAYS
'''
TO GET TO A SINGLE ELEMENT YOU MUST GET DOWN TO A SINGLE ELEMENT.
PROVIDE AN INDEX VALUE FOR EACH DIMENSION
'''
# TWO DIMENSIONAL ARRAY CREATED
# STORES DATA HORIZONTALLY AND VERTICALLY
two_dim_array = np.random.randint(10, size=(2,3))
print('TWO DIMENSIONAL ARRAY CREATED:\n',two_dim_array)
# TODO ACCESSING A TWO DIMENSIONAL ARRAY:
# FIRST VALUE WILL BE FOR THE FIRST ROW
# SECOND VALUE WILL BE FOR ACCESSING COLUMNS
print('SELECTING FROM A TWO DIMENSIONAL ARRAY:')
print('FIRST ROW / THRID COLUMN:',two_dim_array[0,2])
print(two_dim_array[0,2])
# use negative values also
print(two_dim_array[0,-2])
# TODO MUTABILITY TWO DIMENSIONAL ARRAY
numeric_array[3] = 1002
print(numeric_array)
two_dim_array[0,-2] = 403
print(two_dim_array)

# TODO Slicing arrays
# able to grab a group
'''
x[start : stop: step]
start -> starting point
stop  -> stopping point ( grabbing how many elements )
step  -> pull in order 1
      -> pull every other item
if leave blank 
start from beginning
stop at end
'''
# grab items between 3-8
print(numeric_array[3:8])
# grab last 4 items
print(numeric_array[:4])
# grab first 5 items
print(numeric_array[5:])
# grab every 3 item
print(numeric_array[::3])
# grab every 2 items starting from second element
print(numeric_array[1::2])
# TODO slicing negative ( reverse order )
# reverse order of the dataset
print(numeric_array[::-1])
print(numeric_array[::-2])

# TODO SLICING MUTI DIMENSION
# size = (rows,columns)
two_dim_array = np.random.randint(10, size=(5,3))
# print the ne two dimension array
print(two_dim_array)
# grab the first 4 rows and 1 column
print(two_dim_array[:4,:1])

# grab all rows and every column
print(two_dim_array[:, ::2])

# reversing multidimensional arrays
print(two_dim_array[::-1,::-1])

# reverse the rows
print(two_dim_array[::-1])

# reverse the columns
print(two_dim_array[:, ::-1])

# just first row
print(two_dim_array[0])

# return all elements in third column
print(two_dim_array[:,2])
