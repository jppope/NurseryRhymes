
"""
Thirty days hath September,
April, June, and November;
All the rest have thirty-one,
Excepting February alone,
Which has twenty-eight in line,
Till leap-year gives it twenty-nine.
"""

import sys

# As a list
numDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# written as a dict
daysInMonth = {
    28: ["february"],
    30: ["september", "april", "june", "november"],
    31: ["january", "march", "may", "july", "august", "october", "december"]
}

# basic if/else function to determine how many days are in a month

def howManyDaysInMonth(month):
    # standardize the input
    month = month.lower();
    if (month == "september" or month == "april" or month == "june" or month == "november"):
        return 30
    elif (month == "february"):
        return 28
    else:
        return 31;

#print(howManyDaysInMonth("october"))


# function using the daysInMonth dictionary
def howManyDaysInMonthWithDictionary(month):
    # standardize the input
    month = month.lower();
    days = [31, 30, 28]
    
    for d in days:
        if month in daysInMonth[d]:
            return d
    
    return "Invalid input!"

#print(howManyDaysInMonth("AprIL"))


if __name__ == "__main__":
    """ prints the number of days in the month
    of the first command line argument
    
    ex:
    $python daysInMonth.py september
    30
    """
    print(howManyDaysInMonthWithDictionary(sys.argv[1]))