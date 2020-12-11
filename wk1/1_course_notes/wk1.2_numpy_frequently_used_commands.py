###################
# Week 1.2: Numpy #
###################

import numpy as np
import math

##################
# Array Creation #
##################

# array is like a superior object type to a list.
# often list inputs can be converted to arrays
# lists of lists can be converted to matrixes

# importantly, arrays are still displayed as lists, or lists of lists

# declaring an array
a = np.array([1, 2, 3])
print(a)
# printing array dimensions, using attribute: ndim
print(a.ndim)

# converting list of lists to multi-dimensional array, ie, a matrix
b = np.array([[1,2,3],[4,5,6]])
print(b)
# printing array dimensions, using attribute: ndim
print(b.ndim)
# printing length of each dimension
print(b.shape)

# listing object data type, using numpy attribute dtype
print(a.dtype)

# listing other data types in an array, such as float
c = np.array([2.2, 5, 1.1])
print(c.dtype.name)

# checking float array's elements
print(c)
# as noted, some of the integers entered, were converted to floats
# to maintain consistency

# declaring empty array, using dimensions as option
# and using 1's and 0's as fillers
d = np.zeros((2,3))
print(d)

e = np.ones((2,3))
print(e)

# can declare an array, of set dimensions, with random numbers
print(np.random.rand(2,3))

# declaring an array using a sequence of integers
# lower bound included, upper bound not included
f = np.arange(10,50,2) # here, argument 3 indicates interval size
print(f)

# declaring an array using a sequence of floats
# both lower bound and upper bound included
print(np.linspace(0,2,15)) # here argument 3 indicates number of intervals

####################
# Array Operations #
####################

# range from elemental arithmetic, addition and subtraction, exponent
# matrix manipulations: transpose, product, inverse

# arithmetic

# declaring test arrays
a = np.array([10,20,30,40])
b = np.array([1,2,3,4])

# subtraction, similar to vector addition
c = a - b
print(c)

# multiplication, akin to vector multiplication
d = a*b
print(d)

# farenheit to celcius value converter
farenheit = np.array([25, 48, 37, 42, 33]) # dc winter temp example

# formula
celcius = (farenheit - 31) * (5/9)
print(celcius)

# boolean for testing greater than condition: greater than 0 degrees celcius
print(celcius > 0)

# boolean for testing modulus or divisibility condition: even number of celcius
print(celcius % 2 == 0)

# matrix manipulations: matrix multiplication
# declaring two matrices
A = np.array([[1,1],[0,1]]) # first list in list of lists, is first row in matrix
B = np.array([[2,0],[3,4]]) # second list in list of lists, is second row of matrix

print(A*B) # dot product, or scalar product, elementwise
print(A@B) # full matrix multiplication

# verifying dimensions for matrix product, as above
print(A.shape)

# upcasting:
# creating an array of integers
array1 = np.array([[1,2,3],[4,5,6]])
print(array1.dtype)

# creating an array of floats
array2 = np.array([[7.1,8.2,9.1],[10.4,11.2,12.3]])
print(array2.dtype)

# adding two arrays: adopts the broader type definition
array3 = array1 + array2
print(array3)
print(array3.dtype)

# aggregating functions, for arrays in numpy
print(array3.sum())
print(array3.max())
print(array3.min())
print(array3.mean())

# can also use aggregator functions by row, or column
b= np.arange(1,16,1).reshape(3,5) # create matrix from single array

# thinking of matrices as one single list of numbers
# is useful for thinking how images are stored in computer memory
from PIL import Image


# opening tiff image
im = Image.open('chris.tiff')
im.show() # here we use im.show
            # as opposed to plt.show for matplotlib
            # .show() seems to be the recurring theme here though

# converting to numpy array
array=np.array(im) # storing image in array object, called array
print(array.shape)
print(array)

# creating an array the same shape
mask=np.full(array.shape,255)
print(mask)

# subtracting from the modified array
modified_array=array-mask

# converting negative values to positive ones
modified_array=modified_array*-1

# lastly, assigning data values type
modified_array=modified_array.astype(np.uint8)
print(modified_array)

# rendering image from array using numpy
im = Image.fromarray(modified_array)
im.show()

# reshaping the array storing image, and rendering
reshaped = np.reshape(modified_array, (100, 400))
print(reshaped.shape)

im = Image.fromarray(reshaped)
im.show()
# numpy arrays are an abstraction we can build on top of data
# such as images

####################################
# Indexing, Slicing, and Iterating #
####################################

############
# Indexing #
############

# declaring array
a = np.array([1,3,5,7])
# array indexing, 1-dimensional
# remember in python, we start at 0
print(a[2])

# declaring multidimensional array
a = np.array([[1,2],[3,4],[5,6]])
print(a)
# array indexing, 2-dimensional
print(a[1,1])

# pulling multiple elements using indexing, method 1
# by declaring an array of pulled elements
np.array([a[0,0], a[1,1], a[2,1]])

# pulling multiple elements using indexing, method 2
# by listing rows of pulled elements, and columns separately
print(a[[0, 1, 2],[0, 1, 1]])

# this is important for subsetting rows in a dataset.
# however this is mostly for elements.

####################
# Boolean Indexing #
####################

# printing out elements based on condition, by position
print(a > 5)

# extracting out elements meeting condition, into array
print(a[a > 5])

###########
# Slicing #
###########

# python lingo for subsetting
# : used for range, lower bound to the left, upper bound to the right
# if nothing input, default signifies first element, and last element
# upper bound not included

# declaring array
a = np.array([0,1,2,3,4,5])
# print slice, first n elements
print(a[:3])
# slice from the middle of an array
print(a[2:4])

# declaring n-dim array
a = np.array([[1,2,3,4],[5,6,7,8],[0,10,11,12]])
print(a)

# indexing with multi-dimensional arrays
# important for subsetting rows

# subsetting rows:

# the following extracts the first two rows, first: 0th, and second: 1th
print(a[:2])

# subsetting rows and columns: first two rows, by order, and
                            # second and third columns from the left
print(a[:2, 1:3])

# subsetting n-dim: arg1=> row, arg2=>column

# slice of array: called 'passing by reference'

# unless we assign a slice separately, slice is still part of
# original whole.

# therefore, changing the slice changes the whole

# modifying slice

# extracting subarray
sub_array = a[:2, 1:3]

# printing original sub array
print("sub array index [0,0] value before change:", sub_array[0,0])
# printing whole array before change
print("original array index [0,1] value before change:", a[0,1])

# reassigning value at [0,0]
sub_array[0,0] = 50

# printing new sub array
print("sub array index [0,0] value after change:", sub_array[0,0])
# printing whole array after change
print("original array index [0,1] value after change:", a[0,1])


#############################
# Using Numpy with Datasets #
#############################

# reading in data using gentext in numpy
wines = np.genfromtxt("data/winequality-red.csv", delimiter=";", skip_header=1)
print(wines)

# selecting column 'fixed acidity' by position

# must input two argument for row and column
# else, will return a 1-dim list

# selecting all rows, and first column
print("one integer 0 for slicing: ", wines[:, 0])

# selecting same elements, keeping them in initial separate rows
print("0 to 1 for slicing: \n", wines[:, 0:1])

# columns:

# likewise selecting all rows, for first three columns, ordered as such
print(wines[:, 0:3])

# selecting all rows, for non-consecutive columns, by position
print(wines[:, [0,2,4]])

# selecting col by position, + summarizing it
print(wines[:, -1].mean())

## dataset #2: GRE scores
graduate_admission = np.genfromtxt('data/Admission_predict.csv',
                                dtype=None, delimiter=',',
                                skip_header=1,
                                names=('Serial No', 'GRE Score',
                                'TOEFL Score', 'University Rating',
                                'SOP', 'LOR', 'CGPA', 'Research',
                                'Chance of Admit'))
print(graduate_admission)

# checking dimensions, standard procedures
print(graduate_admission.shape)

# now, selecting columns using name (preferable)
print(graduate_admission['CGPA'][0:5])

# checking gpa, and scaling to 4
graduate_admission['CGPA'] = graduate_admission['CGPA']/10*4
print(graduate_admission['CGPA'][0:20])

# boolean masking => selecting rows based on conditional
print(len(graduate_admission[graduate_admission['Research'] == 1]))

# comparing avg gre scores based on chance of admission
# subsetting by 'chance of admission' segment, then
# computing gre mean
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['GRE_Score'].mean())

# boolean masking still produces a list of tuples
# below we have all features of 80th percentile candidates for admission
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8])

# likewise, computing mean gpa after subsetting by chance of admission
print(graduate_admission[graduate_admission['Chance_of_Admit'] > 0.8]['CGPA'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit'] < 0.4]['CGPA'].mean())




































# use plt.show() to display your graphs
