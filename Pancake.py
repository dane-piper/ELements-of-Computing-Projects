#  File: Pancake.py

#  Description: Creates an algorithm that sorts a stack in order from largest to smallest with fewest number of 'flips'

#  Student's Name: Dane Piper

#  Student's UT EID: dap3498

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created:2/21/2020

#  Date Last Modified:2/21/2020

#  Input: pancakes is a list of positive integers
#  Output: a list of the pancake stack each time you
#          have done a flip with the spatula
#          this is a list of lists
#          the last item in this list is the sorted stack


def sort_pancakes(pancakes):
    every_flip = []
    unsorted_size = len(pancakes)
    # loop where the flips happen
    while unsorted_size > 1:
        # creates a sublist for the unsorted portion of the stack
        unsorted = pancakes[0:unsorted_size]
        stack_max = max(unsorted)
        bottom = pancakes.index(stack_max)
        # This if statement flips the highest unsorted number to the top
        if bottom != 0:
            flipped = pancakes[0:bottom + 1]
            flipped.reverse()
            # assigns flipped portion to original stack
            for i in range(bottom + 1):
                pancakes[i] = flipped[i]
            every_flip.append(pancakes[:])
        unsorted = pancakes[0:unsorted_size]
        # This if statement flips the entire unsorted portion of the stack when highest number is on top
        if pancakes.index(max(unsorted)) == 0:
            flipped = pancakes[0: unsorted_size]
            flipped.reverse()
            # assigns flipped portion to original stack
            for i in range(unsorted_size):
                pancakes[i] = flipped[i]
            every_flip.append(pancakes[:])
        unsorted_size -= 1

    return every_flip  # return a list of flipped pancake stacks


def main():
    # open the file pancakes.txt for reading
    in_file = open("./pancakes.txt", "r")

    line = in_file.readline()
    line = line.strip()
    line = line.split()
    print(line)
    pancakes = []
    for item in line:
        pancakes.append(int(item))

    # print content of list before flipping
    print("Initial Order of Pancakes = ", pancakes)

    # call the function to sort the pancakes
    every_flip = sort_pancakes(pancakes)

    # print the contents of the pancake stack after
    # every flip
    for i in range(len(every_flip)):
        print(every_flip[i])

    # print content of list after all the flipping
    print("Final Order of Pancakes = ", every_flip[-1])


if __name__ == "__main__":
    main()
