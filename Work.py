#  File: Work.py

#  Description: Linear and Binary search algorithms that search for the number of lines of code a person writes before
#               drinking their first cup of coffee.

#  Student Name:Dane Piper

#  Student UT EID:dap3498

#  Course Name: CS 313E

#  Unique Number:50300

#  Date Created:2/24/2020

#  Date Last Modified:2/24/2020

import time


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    v = 0
    submat = 0
    while submat < n:
        submat = sleep_time(v, k)
        if submat >= n:
            return v
        v += 1

    return v  # placeholder


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search(n: int, k: int) -> int:
    lo = 0
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        if n > sleep_time(mid, k):
            lo = mid + 1
        elif n < sleep_time(mid, k):
            hi = mid - 1
        else:
            return mid
    if lo > hi:
        return lo

    return mid  # placeholder


# Input: v, the number of lines of code that must be written before the first cup of coffee.
#        k, the productivity factor
# Output: The number of lines written before they fall asleep
def sleep_time(v, k):
    submat = 0
    p = 0
    while v // (k ** p) > 1:
        submat += v // (k ** p)
        p += 1
    return submat


# main has been completed for you
# do NOT change anything below this line
def main():
    in_file = open("work.txt", "r")
    num_cases = int((in_file.readline()).strip())

    for i in range(num_cases):
        inp = (in_file.readline()).split()
        n = int(inp[0])
        k = int(inp[1])
        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
