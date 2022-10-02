import random
print("DAY-5")
print("-----------------------------------------------------------------------------------------------------------")
print("Using for loop")
fruits = ["Apple" , "Peach" , "Pear"]
for fruit in fruits:    # here value of each item in fruits is assigned to fruit.
    print(fruit)

print("Using for sum()")
num=[1,2,3,4,5,6,7,8,9,10]
print(f" num = {num} and its sum is {sum(num)}")

print("Using for max()")
print(f" num = {num} and its max is {max(num)}")

print("Using for min()")
print(f" num = {num} and its min is {min(num)}")

print("Using for range()")
for number in range(10):    # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
    print(number)

for number in range(0,10):  # same as above
    print(number)

for number in range(0,10,4):    # this will step 4 times and print
    print(number)

random.shuffle(num)
print(num)