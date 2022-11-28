# Write a python program to:
	# a. Find the sequences of one uppercase letter followed by lowercase letters
	# b. Match a word containing z
	# c. Match a string containing only uppercase, lowercase letters, numbers and underscores
	# d. To remove leading zeros from an IP address

import re


def sequence_found(text):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, text):
        print("Match Found")
    else:
        print("No Match Found")


def z_found(text1):
    res = re.findall(r'\w*z', text1)
    if (len(res) == 0):
        print("No Match found")
    else:
        print("Match found, word containing z")
        print(res)


def specialchar_found(text1):
    patterns = '^[a-zA-z0-9]*$'
    if re.search(patterns, text1):
        print("Found a Match!!")
    else:
        print("Not Matched!!")


while (1):
    print(
        "1. For some sequences of one uppercase letter followed by lowercase letters"
    )
    print("2. For match word containing z")
    print(
        "3. For strings containing only uppercase, lowercase letters, numbers and underscores"
    )
    print("4. For to remove leading zeros from an IP address")
    print("5. For exit")
    print("Enter your choice:", end=" ")
    choice = int(input())
    if choice == 1:
        st = input("Enter a string: ")
        sequence_found(st)
    elif choice == 2:
        st = input("Enter a string: ")
        z_found(st)
    elif choice == 3:
        st = input("Enter a string: ")
        specialchar_found(st)
    elif choice == 4:
        ip = input("Enter an IP address: ")
        ip = "." + ip
        print(ip)
        ip = re.sub('\.[0]', '.', ip)
        ip = ip[1:]
        print("IP address after removing leading zeros: ", ip)
    elif choice == 5:
        break
    else:
        print("Invalid choice you entered")