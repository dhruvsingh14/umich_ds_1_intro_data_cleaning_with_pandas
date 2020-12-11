###############################
# Week 2.2: Querying a Series #
###############################

#########################################
# Series: Querying by Position and Name #
#########################################
# primary data type in pandas
# can be selected using position or name
# if unnamed explicity - position, is used as name

# iloc: for numeric position querying
# loc: named index querying
import pandas as pd

students_classes = {'Alice': 'Physics',
                  'Jack': 'Chemistry',
                  'Molly': 'English',
                  'Sam': 'History'}
s = pd.Series(students_classes)
print(s)

# grabbing by position
print(s.iloc[3])

# grabbing by name
print(s.loc['Molly'])

# loc and iloc are not methods
# loc and iloc are attributes
# they use square brackets instead of parentheses
# square brackets also known as the indexing operator

# not specifying loc or iloc, pandas can detect based on object type
print(s[3]) # defaults to iloc
print(s['Molly']) # defaults to loc

# being explicit however safeguards against potential errors

# here the index is a set of numbers.
# giving s[n] as query will confuse positional index
# with stated numeric index
class_code = {99: 'Physics',
              100: 'Chemistry',
              101: 'English',
              102: 'History'}

s = pd.Series(class_code)

# thus s[0] produces an error
# therefore it is prudent to use .iloc to be explicit instead

######################
# Series: Operations #
######################
grades = pd.Series([90, 80, 70, 60])

# following loop iterates to sum, then divides by length
total = 0
for grade in grades:
    total+=grade
print(total/len(grades))

# vectorization: using the numpy sum method
import numpy as np

# summing all grades in a series
total= np.sum(grades)
print(total/len(grades)) # printing average

# creating a series of random numbers
numbers = pd.Series(np.random.randint(0,1000,10000))

print(numbers.head())
print(len(numbers))

###########################
# Series: Parallelization #
###########################

# measuring runtime using timeit
import timeit

# a. using looping
mysetup = '''
import pandas as pd
import numpy as np
numbers = pd.Series(np.random.randint(0,1000,10000))
total = 0
'''

mycode = '''
for number in numbers:
    total+=number

total/len(numbers)
'''

print(timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 100))

# b. using vectorization
mysetup = '''
import pandas as pd
import numpy as np
numbers = pd.Series(np.random.randint(0,1000,10000))
total = 0
'''

mycode = '''
total = np.sum(numbers)
total/len(numbers)
'''

print(timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 100))

# function runs far faster
print(numbers.head())

# eg: adding 2 to all numbers in random series
numbers+=2
print(numbers.head())

# iterating through all items always takes longer.
# think twice before doing so

# using iteritems to loop through a series, and return a label+value
for label, value in numbers.iteritems():
    numbers.at[label] = value+2

print(numbers.head())

# more speed comparisons

# a. using iteration
mysetup = '''
import pandas as pd
import numpy as np
s = pd.Series(np.random.randint(0,1000,1000))
'''

mycode = '''
for label, value in s.iteritems():
    s.loc[label] = value+2
'''

print(timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 10))

# b. using broadcasting methods
mysetup = '''
import pandas as pd
import numpy as np
s = pd.Series(np.random.randint(0,1000,1000))
'''

mycode = '''
s+=2
'''

print(timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 10))

# significantly, faster, concise, easier to read

# note: series can have mixed types as indices
# loc, and iloc can be used to assign data values
# assigning values for indices not present, adds a row

# eg: mixed type index
s = pd.Series([1, 2, 3])

# this will lead to mixed indices
s.loc['History'] = 102
print(s)

############################
# Series: Non-Unique Index #
############################

# unique index
students_classes = pd.Series({'Alice': 'Physics',
                    'Jack': 'Chemistry',
                    'Molly': 'English',
                    'Sam': 'History'})
print(students_classes)

# non-unique index
kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'],
                        index=['Kelly', 'Kelly', 'Kelly'])
print(kelly_classes)

# appending the two series
all_students_classes = students_classes.append(kelly_classes)
print(all_students_classes)

# original object is unmodified
print(students_classes)

# querying non-unique index returns a series
print(all_students_classes.loc['Kelly'])




























# plt.show() to display matplotlib plots
