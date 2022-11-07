def calcfreq():
    str=input("Enter a string: ")
    allfreq={}
    for i in str:
        if i in allfreq:
            allfreq[i]+=1
        else:
            allfreq[i]=1
    print("Count of characters in a given string is: ",allfreq)
calcfreq()