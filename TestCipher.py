#  File: TestCipher.py

#  Description: Encrypts and Decrypts Rail Cypher and Vigenere Cipher

#  Student's Name: Dane Piper

#  Student's UT EID: dap3498

#  Partner's Name: Travis West

#  Partner's UT EID: tmw2785

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created:2/1/2020

#  Date Last Modified:2/7/2020
import string
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    length = len(strng)
    y = key - 2
    lines = []
    z = 0
    # creates a list with key number of rails
    while z < key:
        lines.append(strng[z])
        z += 1
    rail_up = True
    # places characters into rails
    for x in range(key, length):
        if y == 0:
            rail_up = False
            lines[y] += strng[x]
            y += 1
        elif y == key - 1:
            rail_up = True
            lines[y] += strng[x]
            y -= 1
        elif rail_up == True:
            lines[y] += strng[x]
            y -= 1
        elif rail_up == False:
            lines[y] += strng[x]
            y += 1
    encoded_str = ''
    # puts list elements into a string
    for rails in lines:
        encoded_str += rails
    return encoded_str  # returns encoded string
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    length = len(strng)
    decode_arr = [0] * key
    # creates a 2D list with key rows and string length columns
    for i in range(key):
        decode_arr[i] = [0] * length
    y = 0
    rail_up = False
    #creates array with place values for the characters
    for x in range(0, length):
        if y == 0:
            rail_up = False
            decode_arr[y][x] = 1
            y += 1
        elif y == key - 1:
            rail_up = True
            decode_arr[y][x] = 1
            y -= 1
        elif rail_up == True:
            decode_arr[y][x] = 1
            y -= 1
        elif rail_up == False:
            decode_arr[y][x] = 1
            y += 1
    encoded_char = 0
    #places characters into array
    for x in range(0, key):
        for y in range(0, length):
            if decode_arr[x][y] == 1:
                decode_arr[x][y] = strng[encoded_char]
                encoded_char += 1
    decoded_strng = ''
    y = 0
    rail_up = False
    #reads array and places characters into a string
    for x in range(0, length):
        if y == 0:
            rail_up = False
            decoded_strng += decode_arr[y][x]
            y += 1
        elif y == key - 1:
            rail_up = True
            decoded_strng += decode_arr[y][x]
            y -= 1
        elif rail_up == True:
            decoded_strng += decode_arr[y][x]
            y -= 1
        elif rail_up == False:
            decoded_strng += decode_arr[y][x]
            y += 1
    return decoded_strng  # returns decoded string


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    # mades string characters lower case
    strng = strng.lower()

    temp = []
    #removes digits from string
    for x in range(len(strng)):

        if strng[x].isdigit():
            pass
        else:
            temp.append(strng[x])

    strng = ''.join(temp)

    # removes all punctuation marks from string
    temp2 = []
    punctuations = '''!()-[]{};:'"\,<>=+|./?@#$%`^&*_~'''
    for x in range(len(strng)):

        if strng[x] in punctuations:
            pass
        else:
            temp2.append(strng[x])

    strng = ''.join(temp2)

    strng = strng.replace(" ", "")

    return strng  # returns string with only lower case letters


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    #changes plain character into encoded character with pass phrase character p
    encoded = (ord(p) + ord(s) - 194) % 26
    encoded += 97
    encoded = chr(encoded)
    return encoded  # returns encoded character
#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    # takes encoded character and changes it to plain text with pass phrase character p
    decoded = (ord(s) - ord(p) + 26) % 26
    decoded += 97
    decoded = chr(decoded)
    return decoded  # returns decoded character
#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    # creates a string of the pass phrase as long as the string
    str_len = len(strng)
    ph_len = len(phrase)
    y = 0
    phrase1 = ''
    for x in range(0, str_len):
        if y == ph_len - 1:
            phrase1 += phrase[y]
            y = 0
        else:
            phrase1 += phrase[y]
            y += 1
    encoded_phrase = ''
    # coverts characters in string into encrypted characters
    for x in range(0, str_len):
        encoded_phrase += encode_character(phrase1[x], strng[x])
    return encoded_phrase  # returns encoded string
#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    # creates a string of the pass phrase as long as the string
    str_len = len(strng)
    ph_len = len(phrase)
    y = 0
    phrase1 = ''
    for x in range(0, str_len):
        if y == ph_len - 1:
            phrase1 += phrase[y]
            y = 0
        else:
            phrase1 += phrase[y]
            y += 1
    decoded_phrase = ''
    # coverts characters in string into decrypted characters
    for x in range(0, str_len):
        decoded_phrase += decode_character(phrase1[x], strng[x])

    return decoded_phrase  # returns decoded string


def main():
    # prints and prompts input for both Rail fence and Vigenere Cypher
    file = open('geom.txt')
    lines = file.readlines()
    print(lines)
    print("Rail Fence Cipher")

    print('')

    strng = (input("Enter Plain Text to be Encoded: "))

    key = int((input("Enter Key: ")))

    print('Encoded Text:', rail_fence_encode(strng, key))

    print('')

    strng = input("Enter Encoded Text to be Decoded: ")

    key = int((input("Enter Key: ")))

    print('Decoded Plain Text:', rail_fence_decode(strng, key))

    print('')

    # decrypt and print the encoded text using rail fence cipher
    print("Vigenere Cipher")

    print('')

    strng = input("Enter Plain Text to be Encoded: ")

    strng = filter_string(strng)

    phrase = input("Enter Pass Phrase (no spaces allowed): ")

    # encrypt and print the plain text using Vigenere cipher

    print('Encoded Text:', vigenere_encode(strng, phrase))

    print('')

    strng = (input("Enter Encoded Text to be Decoded: "))

    phrase = (input("Enter Pass Phrase (no spaces allowed): "))

    # decrypt and print the encoded text using Vigenere cipher
    print('Decoded Plain Text:',vigenere_decode(strng, phrase))

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()