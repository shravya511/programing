# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
m=1080    #--
w=4680    #  |-- this is done 'cuz 90 years has 1080 month, 4680 weeks and 32850 days
d=32850  #--
#Write your code below this line 👇
a=int(age)
m1=a*12     #---                                                                 remaining_years = 90 - a
w1=a*52     #   |                                                                 d2 = remaining_years * 365
d1=a*365   #   |----this code can be reduced like this -->  w2 = remaining_years * 52
m2=m-m1   #   |                                                                  m2 = remaining_years * 12
w2=w-w1    #   |
d2=d-d1     #---
print(f"You have {d2} days, {w2} weeks, and {m2} months left.")