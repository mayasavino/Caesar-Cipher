'''
File: caesar.py
Authors: Maya Savino and Ariana Garcia
Date: March 24, 2021
'''


def main():

    #create list containing the cipher alphabet
    alphabet_c = {
        "a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i",
        "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o",
        "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u",
        "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a",
        "y": "b", "z": "c" }

    file_name = str(input("Input file's name: "))



    #open("ciphered.txt", "w") as ciphered:
    with open("test_caesar.txt", "r") as file_name, \
         open("ciphered.txt", "w") as ciphered: 

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

        contents = ciphered.write(ciphered_contents)


if __name__ == "__main__":
    main()

