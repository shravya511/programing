print("DAY-2")
print("-----------------------------------------------------------------------------------------------------------")
print("hello"[0])
print(type(12))
char_num=str(len(input("Whats your name? ")))
print("Your name has " + char_num + " charecters") 
a=type(123)
print(a)
print(1_234_567_889)    #over here '_' is not considered 
print(2**3)     # here '**' means power operator
print(round(8/3,3))     # here round() is used to round the floating point number. this function takes 2 inputs, one is the operation and another is precision points.
print("using .format() and output the answer of 8/3 ->"+ "{:.2f}".format(8/3))
print(8//3) # '//' this is called flow dividion, used to convert the result to int automatically.
print(f"Using f-string {a} ---- {char_num}")    # f-string is used to automatically concatinate different data types in output screen.