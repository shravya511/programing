print("DAY-3")
print("-----------------------------------------------------------------------------------------------------------")
print("Using if statement")
a = input("Value of a is: ")
b = input("Value of b is: ")
if a == b:
    print("A and B are equal")
else:
    print("A and B are not equal")

print("Using nested if statement")
if a == b:
    print("A and B are equal")
else:
    if a > b:
        print("A is greater than B")
    else:
        print("B is greater than A")

print("Using elif statement")
if a == b:
    print("A and B are equal")
elif a > b:
    print("A is greater than B")
elif a < b:
    print("B is greater than A")

print("Using .lower()")
a=input("Enter capital letter: ")
print(a.lower())    # .lower() used to convert capital letters to lower case letters

print("Using .count()")
print(f"Counting number of 'A' in capital letters: {a.count('A')}")     # .count() is used returns the number of elements with the specified value.

print('''    
hey
this 
is
multi 
line
string
''')    # we use ''' <- this to make multi-line string