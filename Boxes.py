#  File: Boxes.py

#  Description: Finds the largest subset of boxes given there length that all nest (fit inside one another)

#  Student Name: Dane Piper

#  Student UT EID: dap3498

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 3/8/2020

#  Date Last Modified: 3/9/2020


# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes(box_list, sub_set, idx, all_box_subsets):
    hi = len(box_list)
    if idx == hi:
        all_box_subsets.append(sub_set)
    else:
        c = sub_set[:]
        sub_set.append(box_list[idx])
        sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
        sub_sets_boxes(box_list, c, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes):
    # created local list to store all the boxes that nest
    all_nested = []
    for i in range(len(all_box_subsets)):
        size = len(all_box_subsets[i])
        fit = True
        for x in range(len(all_box_subsets[i]) - 1):
            if not does_fit(all_box_subsets[i][x], all_box_subsets[i][x + 1]):
                fit = False
                break
        if fit:
            all_nested.append(all_box_subsets[i])
    # Finds the longest list of nested boxes and appends all the lists of that length to all_nesting_boxes
    for y in range(len(all_nested)):
        if len(all_nested[y]) > largest_size and len(all_nested[y]) >= 2:
            largest_size = len(all_nested[y])
    for z in range(len(all_nested)):
        if len(all_nested[z]) == largest_size and largest_size > 1:
            all_nesting_boxes.append(all_nested[z])


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def main():
    # open the file for reading
    in_file = open("./boxes.txt", "r")

    # read the number of boxes
    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # close the file
    in_file.close()

    # print (box_list)
    # print()

    # sort the box list
    box_list.sort()
    # print (box_list)
    # print()

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

    # initialize the size of the largest sub-set of nesting boxes
    largest_size = 0

    # create a list to hold the largest subsets of nesting boxes
    all_nesting_boxes = []

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes)

    # print all the largest subset of boxes
    if len(all_nesting_boxes) == 0:
        print('No Nesting Boxes')
    else:
        print('Largest Subset of Nesting Boxes')
        for x in range(len(all_nesting_boxes)):
            for y in range(len(all_nesting_boxes[x])):
                print(all_nesting_boxes[x][y])
            print()



if __name__ == "__main__":
    main()
