def main():
    choice = input("Please select operation(encrypt/decrypt): ")
    choice = choice.lower()

    if (choice == "encrypt"):
        encrypt()
    elif (choice == "decrypt"):
        decrypt()
    else:
        print("Invalid input. Enter encrypt or decrypt.") 
        main()


def encrypt():

    #create list containing the cipher alphabet
    alphabet_c = {
        "a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g",
        "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m",
        "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s",
        "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y",
        "y": "z", "z": "a" }

    file_name = str(input("Input file's name: "))



    #open("ciphered.txt", "w") as ciphered:
    with open("test_sub.txt", "r") as file_name, \
         open("ciphered_substiution.txt", "w") as ciphered_substitution: 

        lines = file_name.readlines()
        counti = 0
        ciphered_master = []

        while (counti < len(lines)): # reading each line in the file
            letters = list(lines[counti]) # letters is a list with characters in lines
            print("letters: ", letters) #
            print("counti: ", counti)
            #replacement = alphabet_c.get(letters[???])
            #print("replacement: ", replacement)
            ciphered_lst = []

            countl = 0
            while (countl < len(letters)):
                print(ciphered_lst)
                # convert the character in countl position to the cipher character
                if letters[countl] in alphabet_c:
                    replacement = alphabet_c.get(letters[countl])
                else:
                    replacement = letters[countl]
                ciphered_lst.append(replacement)
                print(ciphered_lst)
                countl += 1

            ciphered_str = "".join(map(str, ciphered_lst))
            ciphered_master.append(ciphered_str)
            print(ciphered_master)

            counti += 1 #
            

        ciphered_contents = "".join(map(str, ciphered_master)) 
        print(ciphered_contents)

        contents = ciphered_substitution.write(ciphered_contents)

def decrypt():

#create list containing the cipher alphabet
    alphabet_c = {
        "a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g",
        "g": "h", "h": "i", "i": "j", "j": "k", "k": "l", "l": "m",
        "m": "n", "n": "o", "o": "p", "p": "q", "q": "r", "r": "s",
        "s": "t", "t": "u", "u": "v", "v": "w", "w": "x", "x": "y",
        "y": "z", "z": "a" }

#reverse the alphabet to get the decryption alphabet
    alphabet_c = {v:k for k, v in alphabet_c.items()}

    file_name = str(input("Input file's name: "))



    #open("ciphered.txt", "w") as ciphered:
    with open("test_sub.txt", "r") as file_name, \
         open("ciphered_substiution.txt", "w") as ciphered_substitution: 

        lines = file_name.readlines()
        counti = 0
        ciphered_master = []

        while (counti < len(lines)): # reading each line in the file
            letters = list(lines[counti]) # letters is a list with characters in lines
            print("letters: ", letters) #
            print("counti: ", counti)
            #replacement = alphabet_c.get(letters[???])
            #print("replacement: ", replacement)
            ciphered_lst = []

            countl = 0
            while (countl < len(letters)):
                print(ciphered_lst)
                # convert the character in countl position to the cipher character
                if letters[countl] in alphabet_c:
                    replacement = alphabet_c.get(letters[countl])
                else:
                    replacement = letters[countl]
                ciphered_lst.append(replacement)
                print(ciphered_lst)
                countl += 1

            ciphered_str = "".join(map(str, ciphered_lst))
            ciphered_master.append(ciphered_str)
            print(ciphered_master)

            counti += 1 #
            

        ciphered_contents = "".join(map(str, ciphered_master)) 
        print(ciphered_contents)

        contents = ciphered_substitution.write(ciphered_contents)

if __name__ == "__main__":
    main()


