import random   # random is a pre-build module 
import my_module    # importing user built module
print(my_module.a)
random_int = random.randint(1,10) # this will return a integer between 1 to 10
random_float = random.random()  # this will return a floating point number betweem 0 to 1 but does not include 1.
print(random_float)     
print(random_int)
print(random_float * 5 ) # this will return a floating point number betweem 0 to 5 but does not include 5. 

print("Using LISTS")
states_of_india = ["Karnataka" , "Maharastra" , "Kerala" , "Tamil Nadu"]    # this is a list. lists have -> [ ]
print(states_of_india)
print(states_of_india[1])   
print(states_of_india[-1])  # here -1 means last element in list.
states_of_india.append("Goa")   # append() is used to add elements to the end of the list
print(states_of_india)
states_of_india.extend(["Utter Pradesh" , "Bihar" , "Assam"])   # extend() is used to add a new list to an existing list
print(states_of_india)

print("Using split()")  # used to convert a string into a list by separating out by using some sort of divider
a = "using, split, and, the, separator is a comma"
A = a.split(',')
print(A)

print("Using len()")    # used to returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
print(len(A))

print(random.choice(A))     # used to randomly choose an item from a list or object.