close_program = False
while not close_program:
    user = input("Type 'encode' to encrypt. \nType 'decode' to decrypt.\n:-").lower()
    message = input("Type your message:\n")
    shift = int(input("Type the shift number (0 ~ 30):\n"))
    encrypted_message = " "
    decrypted_message = " "
# Encoding
    if user == 'encode':
        print("encoding")
        for letter in message:
            ascii_value = ord(letter)
            ascii_symbol_value = ascii_value
        # capital letter encryption
            if ascii_value >= 65 and ascii_value <= 90:
                ascii_value += shift
                while ascii_value > 90:
                    ascii_value -= 26
        # small letter encryption
            elif ascii_value >= 97 and ascii_value <= 122:
                ascii_value += shift
                while ascii_value > 122:
                    ascii_value -= 26
        # symbol encryption    
            elif ascii_value >= 123 and ascii_value <= 126 or ascii_value >= 91 and ascii_value <= 96 or ascii_value >= 58 and ascii_value <= 64 or ascii_value >= 32 and ascii_value <= 47:
                ascii_value += shift
                if ascii_value > 126 and  ascii_symbol_value >= 123 and ascii_symbol_value <= 126:
                    while ascii_value > 126:
                        ascii_value -= 4
                elif ascii_value > 96 and ascii_symbol_value >= 91 and ascii_symbol_value <= 96:
                    while ascii_value > 96:
                        ascii_value -= 6
                elif ascii_value > 64 and ascii_symbol_value >= 58 and ascii_symbol_value <= 64:
                    while ascii_value > 64:
                        ascii_value -= 7
                elif ascii_value > 47 and ascii_symbol_value >= 32 and ascii_symbol_value <= 47:
                    while ascii_value > 47:
                        ascii_value -= 16
        # number encryption
            elif ascii_value >= 48 and ascii_value <= 57:
                ascii_value += shift
                if ascii_value > 57:
                    while ascii_value > 57:
                        ascii_value -= 10
            encrypted_message += chr(ascii_value)
        print(encrypted_message)
    # closing flag
        flag = input("Do you want to close the program? (y/n)\n").lower()
        if flag == 'y':
            close_program = True
            print("Closing Caesar Cipher program.")
# Decoding
    elif user == 'decode':
        print("decoding")
        for letter in message:
            ascii_value = ord(letter)
            ascii_symbol_value = ascii_value
        # capital letter decryption
            if ascii_value >= 65 and ascii_value <= 90:
                ascii_value -= shift
                while ascii_value < 65:
                    ascii_value += 26
        # small letter decryption
            elif ascii_value >= 97 and ascii_value <= 122:
                ascii_value -= shift
                while ascii_value < 97:
                    ascii_value += 26
        # symbol decryption    
            elif ascii_value >= 123 and ascii_value <= 126 or ascii_value >= 91 and ascii_value <= 96 or ascii_value >= 58 and ascii_value <= 64 or ascii_value >= 32 and ascii_value <= 47:
                ascii_value -= shift
                if ascii_value < 32 and ascii_symbol_value >= 32 and ascii_symbol_value <= 47:
                    while ascii_value < 32:
                        ascii_value += 16
                elif ascii_value < 58 and ascii_symbol_value >= 58 and ascii_symbol_value <= 64:
                    while ascii_value < 58:
                        ascii_value += 7
                elif ascii_value < 91 and ascii_symbol_value >= 91 and ascii_symbol_value <= 96:
                    while ascii_value < 91:
                        ascii_value += 6
                elif  ascii_value < 123 and  ascii_symbol_value >= 123 and ascii_symbol_value <= 126:
                    while ascii_value < 123:
                        ascii_value += 4
        # number decryption
            elif ascii_value >= 48 and ascii_value <= 57:
                ascii_value -= shift
                if ascii_value < 48:
                    while ascii_value < 48:
                        ascii_value += 10
            encrypted_message += chr(ascii_value)
        print(encrypted_message)
    # closing flag
        flag = input("Do you want to close the program? (y/n)\n").lower()
        if flag == 'y':
            close_program = True
            print("Closing Caesar Cipher program.")
    else:
        print("Invalid input. \nValid inputs are: \n\t\tEncode\n\t\tDecode.\n")