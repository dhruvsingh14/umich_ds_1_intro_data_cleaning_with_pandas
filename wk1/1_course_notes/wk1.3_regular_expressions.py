#################################
# Week 1.3: Regular Expressions #
#################################
import re

# example string
text = "This is a good day."

# match() : used to check pattern at start of string
# search() : used to check pattern anywhere in string

# simply boolean for now
if re.search("good", text):
    print("Wonderful!")
else:
    print("Alas :(")

# tokenizing, used in string searching, is key to nlp

# new string
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."

# splitting on name Amy
print(re.split("Amy", text))
# resulting output is a list of strings

# checking instances of split pattern occurence
print(re.findall("Amy", text))

# using ^ and $ to indicate start and end of a string when matching
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."

print(re.search("^Amy", text))
# returns 'match' type object, value of true if matched,
# and postion of pattern being matched

##########################
# Patterns and Character #
##########################

# checking assignment grades for one course
grades = "ACAAAABCBCBAA"

# checking for number of B grades
print(re.findall("B", grades))

# checking for number of A or B grades
# square bracket or set operator contains multiple patterns
print(re.findall("[AB]", grades))

# placing multiple patterns in double quotes searches for immediacy
# set operators can take ranges
# the following searches for A's followed by B's or C's
print(re.findall("[A][B-C]", grades))

# the above can also be searched using the pipe operator
# to find A followed by B, or A followed by C
print(re.findall("AB|AC", grades))

# caret operator within set operator means 'not'
print(re.findall("[^A]", grades))

# using caret in two separate contexts
# to check begins non-A value
# set operator is for character matching, within or
print(re.findall("^[^A]", grades))

###############
# Quantifiers #
###############

# can be used to match immediacy as well
print(re.findall("A{2,10}", grades))
# where curly braces show min recurrence, to max recurrence

# not using quantifier is same as using default of 1,1
print(re.findall("A{1,1}A{1,1}", grades))

# same result can be achieved using A{2,2}
# however, {2, 2} with a space gives an empty result. caution
print(re.findall("A{2, 2}", grades))

# as before
print(re.findall("AA", grades))

# one argument will be used as both min and max
print(re.findall("A{2}", grades))

# and preference is given to max occurence, working downward from there
print(re.findall("A{1,10}B{1,10}C{1,10}", grades))

# other quantifier values include:
# "*": 0 or more matches
# "?": 1 or more matches
# "+": 1 or more matches

# using scraped wikipedia data
with open("data/ferpa.txt", "r") as file:
    wiki=file.read() #storing raw text data

print(wiki)

# grabbing headers based on pattern matching
# using "any characters, of upto 100 length"
# immediately followed by [edit] {{Pattern idenfied}}
print(re.findall("[a-zA-Z]{1,100}\[edit\]", wiki))

# \w is shorthand for any letters or digits, ie, alphanumeric characters
print(re.findall("[\w]{1,100}\[edit\]", wiki))
# likewise, \s can be used to denote whitespaces

# shortening quantifier, to indicate 0 or more
print(re.findall("[\w]*\[edit\]", wiki))

# adding in a space to phrases preceding [edit]
print(re.findall("[\w ]*\[edit\]", wiki))
# this only searches for single spaces

# now, stripping out the [edit] splitter
for title in re.findall("[\w ]*\[edit\]",wiki):
    print(re.split("[\[]",title)[0])
# stopping search at open square bracket.
# printing only relevant portion before [, not the gunk after

##########
# Groups #
##########

# for multiple pattern matching, use parentheses
# this still follows the sequential rule
print(re.findall("([\w]*)(\[edit\])",wiki))

# recall findall() returns strings, search(), match() return match objects

# to returns a list of match objects, use finditer:
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())

# stating group(number) returns set of matches of interest
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(1))

# labeling groups in regexes being matched
# creating a dictionary key for convenience
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    print(item.groupdict()['title'])

# printing full groups-dictionary of last match
print(item.groupdict())
# other shorthand for string matching,
# "." for single character, \d for single digit

##############################
# Look-ahead and Look-behind #
##############################

# the following returns match type objects
# with the length of the title preceding [edit] displayed
# the pattern preceding displayed
# and the [edit] match discarded
for item in re.finditer("(?P<title>[\w ]*)(?=\[edit\])",wiki):
    print(item)

###################################
# Example: Wikipedia Data: Part 2 #
###################################

# reading in text data
with open("data/buddhist.txt","r", encoding="utf8") as file:
    wiki=file.read()

print(wiki)

# {{Pattern identified}}: " - " "city" "state"
pattern="""
(?P<title>.*)       # university name
(–\ located\ in\ )  # copy pasted from text
(?P<city>\w*)       # city of university
(,\ )               # again copy pasted, \ to show spaces
(?P<state>\w*)      # state the city is in"""

for item in re.finditer(pattern,wiki,re.VERBOSE):
    print(item.groupdict())

########################################
# Example: New York Times and Hashtags #
########################################

# reading in text data of tweets
with open("data/nytimeshealth.txt","r", encoding="utf8") as file:
    health=file.read()

print(health)

# tweets are separated by pipes
# hashtags begin with pound sign/hash mark
pattern= '#[\w\d]*(?=\s)' # * means any occurence of alphanumeric chars
                          # + would mean at least one instane of each

# tweets end in a whitespace.
# so we use a look-ahead to cap off the end of the match

print(re.findall(pattern, health))

# concise code runs optimally



























# use plt.show() to display your graphs
