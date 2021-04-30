#  File: Reducible.py

#  Description: Reads a list of words from a file and determines the largest group of reducible words in the list

#  Student's Name: Dane Piper

#  Student's UT EID: dap3498

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created:4/3/2020

#  Date Last Modified:4/3/2020
# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size(s):
    step = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        step = (step * 26 + letter) % 13
    return 13 - step



# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s, hash_table):
    length = len(hash_table)
    index = hash_word(s, length)
    if hash_table[index] != '':
        new_ind = index + step_size(s)
        while hash_table[new_ind] != '':
            new_ind = (new_ind + step_size(s)) % length
        hash_table[new_ind] = s
    else:
        hash_table[index] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    length = len(hash_table)
    index = hash_word(s, length)
    if hash_table[index] == s:
        return True
    if hash_table[index] == '':
        return False
    new_ind = (index + step_size(s)) % length
    while True:
        if hash_table[new_ind] == s:
            return True
        if hash_table[new_ind] == '':
            return False
        new_ind = (new_ind + step_size(s)) % len(hash_table)


# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise

def is_reducible(s, hash_table, hash_memo):
    if (len(s) == 1):
        if s == 'a' or s == 'o' or s == 'i':
            return True
        else:
            return False
    else:
        if find_word(s, hash_memo):
            return True
        if not find_word(s, hash_table) or not ('a' in s or 'i' in s or 'o' in s):
            return False
        for i in range(len(s)):
            a = s[0: i:] + s[i + 1::]
            if is_reducible(a, hash_table, hash_memo):
                insert_word(a, hash_memo)
                return True
        return False


# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words(string_list):
    words = []
    max1 = len(max(string_list, key=len))
    for word in string_list:
        if len(word) == max1:
            words.append(word)
    words.sort()
    return words


def main():
    # create an empty word_list
    word_list = []
    # open the file words.txt
    file = open('words.txt')
    # read words from words.txt and append to word_list
    with open("words.txt", "r") as file:
        for line in file:
            word_list.append(line.strip())
    # close file words.txt
    file.close()
    # find length of word_list
    list_len = len(word_list)


# determine prime number N that is greater than twice
# the length of the word_list
    list_len = 2 * len(word_list)
    while not is_prime(list_len):
        list_len += 1
# create an empty hash_list
    hash_list = []
# populate the hash_list with N blank strings
    for x in range(list_len):
        hash_list.append('')
# hash each word in word_list into hash_list
        # for collisions use double hashing
    for words in word_list:
        insert_word(words, hash_list)
# create an empty hash_memo of size M
# we do not know a priori how many words will be reducible
# let us assume it is 10 percent (fairly safe) of the words
# then M is a prime number that is slightly greater than
# 0.2 * size of word_list
    M = 27011
    hash_memo = []
# populate the hash_memo with M blank strings
    for y in range(M):
        hash_memo.append('')
# create an empty list reducible_words
    reducible_words = []
# for each word in the word_list recursively determine
# if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

# find words of the maximum length in reducible_words
# print the words of maximum length in alphabetical order
    max_words = get_longest_words(reducible_words)
    for words in max_words:
        print(words)
# one word per line


# This line above main is for grading purposes. It will not
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
