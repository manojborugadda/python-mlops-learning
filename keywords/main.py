# This code will raise a SyntaxError because 'if' and 'def' are reserved keywords in Python and cannot be used as variable names.

"""

if = 10
print(if)

def = 20
print(def)

"""

#####################
# The correct way to use variables is to choose names that are not reserved keywords.
a = 5
print(a)

b = 10
print(b)

######################

import keyword
print(keyword.kwlist)  # This will print the list of reserved keywords in Python.

print("total number of keywords : ", len(keyword.kwlist))  # This will print the number of reserved keywords in Python.