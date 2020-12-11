#########################
# Assignment 1: Regexes #
#########################

def example_word_count():
    # function used to count words in a string
    example_string = "Amy is 5 years old"
    # storing word units separated by a space
    result = example_string.split(" ")
    # counting results
    return len(result)

##########
# Part A #
##########
import re

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is
                    2 years old.
                    Ruth and Peter, their parents, have 3 kids."""
    # checking instances of split pattern occurence
    return(re.findall("Amy|Mary|Ruth|Peter", simple_string))
    raise NotImplementedError()

assert len(names()) == 4, "There are four names in the simple_striBg"

##########
# Part B #
##########
import re

def grades():
    with open("data/grades.txt", "r") as file:
        grades=file.read() #storing raw text data
    return(re.findall("([\w ]*)(: B)", grades))
    raise NotImplementedError()

assert len(grades()) == 16

##########
# Part c #
##########
import re

def logs():
    with open("data/logdata.txt", "r") as file:
        logdata=file.read() #storing raw text data

    pattern = """
    (?P<host>.*)
    \s-\s
    (?P<user_name>.*)
    \s\[
    (?P<time>.*)
    \]\s\"
    (?P<request>.*)
    \".*
    """
    loglist = []
    for item in re.finditer(pattern,logdata,re.VERBOSE):
        loglist.append(item.groupdict())
    return(loglist)
    raise NotImplementedError()

assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}

assert one_item in logs(), "Sorry, this item should be in the log results, check your formatting"
































# use plt.show() to display plots
