####################
# Week 2.1: Pandas #
####################
import pandas as pd

##########
# Series #
##########
# object type: cross bw list and dictionary

# 1: easily created by converting list to series

# list of strings:
students = ['Alice', 'Jack', 'Molly']
# series: creates an indexed Series
# object type
print(pd.Series(students))

# list of integers:
numbers = [1, 2, 3]
# series: creates an indexed series
# int64 type
print(pd.Series(numbers))

# list of strings with missing data:
students = ['Alice', 'Jack', None]
# missing value carries over as a none in series
print(pd.Series(students))

# list of integers:
numbers = [1, 2, None]
# missing value converted to nan, floating point, not a number
# whenever there's missing data, pandas converts all nums to float data type
print(pd.Series(numbers))

# important to note, NaN and None are not equivalent
# nan refers to missing numeric values, none refers to strings missing
import numpy as np

# testing, using numpy's nan-generator
print(np.nan == None)

# likewise, testing for nan, cannot be reflexive
print(np.nan == np.nan)

# but can use the numpy function is nan
print(np.isnan(np.nan))

# 2: converting dictionaries into series
students_scores = {'Alice': 'Physics',
                    'Jack': 'Chemistry',
                    'Molly': 'English'}
s = pd.Series(students_scores)
print(s)
# here, while still object type
# keys are set to index

#####################
# way to grab index
print(s.index)
#####################

# 3: converting list of tuples to series
students = [("Alice", "Brown"), ("Jack", "white"), ("Molly", "Green")]
print(pd.Series(students))
# here the tuple type is preserved and has numeric indexing

# 2: casting dictionaries to series using indexing
student_scores = {'Alice': 'Physics',
                  'Jack': 'Chemistry',
                  'Molly': 'English'}

s = pd.Series(students_scores, index=['Alice', 'Molly', 'Sam'])
print(s)
# calling Sam in the index for Series creation doesn't result in error
# even though Sam isn't in original dictionary
# but it does result in missing value for that key.













# plt.show() to display matplotlib plots
