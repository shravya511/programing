from array import *
x=array("i",[])
n=int(input("How many elements: "))
for i in range(n):
    x.append(int(input("Enter elements: ")))
print(x)
print("Prime numbers in the array are: ")
for i in range(n):
    j=2
    p=1
    if x[i]>2:
        while j<x[i]:
            if (x[i]%j)==0:
                p=0
                break
            j=j+1
        if p==1:
            print(x[i],end=" ")
