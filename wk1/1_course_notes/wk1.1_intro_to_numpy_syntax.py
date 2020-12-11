###################
# Week 1.1: Intro #
###################

#############
# Functions #
#############

# variables
x = 1
y = 2
print(x+y)
print(y)


# basic functions 1
def add_numbers(x, y):
    return x + y

print(add_numbers(1, 2))


# incremented functions 2
# with conditionals implemented
def add_numbers(x, y, z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1,2))
print(add_numbers(1,2,3))


# enhanced functions 3
# with optional parameters for testing
def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1,2, flag=True))

# assigning variables using defined functions
def add_numbers(x, y):
    return x+y

a = add_numbers
print(a(1,2))

#######################
# Types and Sequences #
#######################

# returning object type
print(type('This is a string'))

print(type(None))

print(type(1))

print(type(1.0))

print(type(add_numbers))

x = (1, 'a', 2, 'b') # tuples, immutable data structure
print(type(x))

x = [1, 'a', 2, 'b'] # lists, mutable data structure
print(type(x))

# mutation to list
x.append(3.3)
print(x)

# looping through each item in a list
for item in x:
    print(item)

# or, using indexing
i=0
while( i != len(x) ):
    print(x[i])
    i = i + 1

# concatenating lists
print([1,2] + [3,4])

# repeating lists
print([1]*3)

# 'in' checks for belonging criteria
print(1 in [1,2,3])

# string slicing selects substring by position
x = 'This is a string'
print(x[0])
print(x[0:1])
print(x[0:2])

print(x[-1])

print(x[-4:-2])

print(x[:3])

print(x[3:])


# running tests on custom string
# usefule for templates
firstname = 'Dhruv'
lastname = 'Singh'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Dhruv' in firstname)

# string split, into a list
firstname = 'Dhruv Narayan Singh'.split(' ')[0]
lastname = 'Dhruv Narayan Singh'.split(' ')[-1]

print(firstname)
print(lastname)

# objects must be type string for concat
# 'Dhruv' + 2 # causes a type error

print('Dhruv'+str(2))

# dictionary data types: key-value relationship
# dictionaries are a type of a list
x = {'Dhruv Singh': 'dsingh@forsmarshgroup.com', 'Bill Gates': 'billg@microsoft.com'}
print(x['Dhruv Singh']) # Can select value by indexing

# adds a key-value pair to existing dictionary
x['Kevyn Collins-Thompson'] = None
print(x['Kevyn Collins-Thompson'])

# iterating over all keys
for name in x:
    print(x[name])

# iterating over all values
for email in x.values():
    print(email)

# iterating over all items
for name, email in x.items():
    print(name)
    print(email)

# turning to the sequence data type
x = ('Dhruv', 'Singh', 'dsingh@forsmarshgroup.com')

# we can assign multiple element to variables in one line
fname, lname, email = x

print(fname)
print(lname)

###################
# More on Strings #
###################
#print('Dhruv' + 2)
print('Dhruv' + str(2))

# built in method for string formatting
sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Dhruv'}

# can insert variables into strings in the following way
sales_statement = '{} bought {} items(s) at a price of {} each for a total of {}'
    
print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

#################################
# Reading and Writing CSV files #
#################################

import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# prints first 3 rows of key - value pairs
print(mpg[:3])

# csv.Dictreader reads csv as a dictionary
# rather than a dataframe or any other object type
print(len(mpg)) # number of rows

# a nifty way to product column names with a dictionary
print(mpg[0].keys())

# checking column average for 'cty' fuel economy
print(sum(float(d['cty']) for d in mpg) / len(mpg))
# checking column average for 'hwy' fuel economy
print(sum(float(d['hwy']) for d in mpg) / len(mpg))

# with dictionaries: set returns unique values
cylinders = set(d['cyl'] for d in mpg) 
print(cylinders)
# notice that we must always loop over rows to do row calculations


# looping within groups, by cylinder
CtyMpgByCyl = []
for c in cylinders: # iterate over cylinder numbers above
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterating through rows
        if d['cyl'] == c: # group 1 - n, by cylinder
            summpg += float(d['cty']) # totaling 'cty' fuel economy
            cyltypecount += 1 # iterating to count current group
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # group average
                                            # inserted into shell
CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)
# columns are yet unnamed, but can be assigned as shown previously

# checking unique class types for vehicles, using set
vehicleclass = set(d['class'] for d in mpg)
print(vehicleclass)


# looping within groups pt ii., by vehicle class
HwyMpgByClass = []
for t in vehicleclass: # iterate over vehicle class above
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterating through rows, ie, dictionaries
        if d['class'] == t: # group 1 - n, by cylinder
            summpg += float(d['hwy']) # totaling 'hwy' fuel economy
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # group average
                                            # inserted into shell
HwyMpgByClass.sort(key=lambda x: x[1])
print(HwyMpgByClass)
# columns are yet unnamed, but can be assigned as shown previously

###################
# Dates and Times #
###################

import datetime as dt
import time as tm

# time since the epoch, Jan 1st, 1970
print(tm.time())

# convert timestamp to datetime
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)

# extracting date and time elements
print(dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

# creating variable for 100 day difference between two dates
delta = dt.timedelta(days = 100) # create a timedelta of 100 days
print(delta)

# storing todays date
today = dt.date.today()

# date from a 100 days ago
print(today - delta)

# checking boolean b/w two datetimes
print(today > today - delta)

####################
# Object and map() #
####################
# example of a class in python
class Person:
    department = 'Advanced Analytics' # a class variable

    def set_name(self, new_name): # a method
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

person = Person()
person.set_name('Dhruv Singh')
person.set_location('Washington, DC, USA')
print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

# example of mapping function: 'min', between two lists
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2) # map object
print(cheapest)

# iterating through map object
for item in cheapest:
    print(item)

##################################
# Lambda and List Comprehensions #
##################################

# declaring and defining a function using lambda programming
my_function = lambda a, b, c: a + b # sums first two of three arguments
print(my_function(1, 2, 3))

# iterating, to check for even numbers: regular
my_list = []
for number in range(0, 1000):
    if number % 2 == 0: # testing divisible by 2, modulo
        my_list.append(number)
print(my_list)
# here we append to a shell

# iterating, to check for even numbers: list comprehension
my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)
# here we fill list elements dynamically


























