t1=(1,2,5,7,9,2,4,6,8,10)
print("Tuple t1: ",t1)
t2=(11,13,15)
print("Tuple t2: ",t2)
print("After slicing: ")
n=int(len(t1)/2)
print(t1[:n],"\n",t1[n:])
l1=list()
for i in t1:
    if i%2==0:
        l1.append(i)
even=tuple(l1)
print("Even elements of tuple t1 is: ",even)
print("After concatination of tuple t2 with t1: ")
t1+=t2
print(t1)
print("Maximum: ",max(t1),"\nMinimum: ",min(t1))
