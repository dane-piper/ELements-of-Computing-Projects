#  File: Spiral.py

#  Description: Creates a spiral of natural numbers and prints a portion of it with a given value

#  Student's Name: Dane Piper

#  Student's UT EID: dap3498

#  Course Name: CS 313E

#  Unique Number: 50300

#  Date Created: 2/17/2020

#  Date Last Modified: 2/17/2020


#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged
#          in a spiral
def create_spiral(dim):
    # creates 2-D list with dimension given and assigns the center with value 1
    spiral = [0] * dim
    for x in range(dim):
        spiral[x] = [0] * dim
    center = int((dim - 1) / 2)
    spiral[center][center] = 1
    increase = 1
    # defines variable 'right, down, left, up' corresponding to the direction of spiral
    r_d_l_u = 1
    column = center
    row = center
    count = 1
    spin = 0
    # This exception is for if the index is every out of bounds, returns spiral as is ( for testing)
    try:
        # This is the loop that assigns each element in the 2-D list with numbers in a spiral
        while count < dim * dim - 1:
            if spin % 2 == 0 and spin != 0:
                increase += 1
            if r_d_l_u > 4:
                r_d_l_u = 1
            # This loop determines how many spaces in each direction the spiral moves
            # example: for increase = 2 the spiral moves two to the left
            for x in range(increase):
                if count > dim * dim - 1:
                    break
                else:
                    if r_d_l_u == 1:
                        column += 1
                        spiral[row][column] = count + 1
                        count += 1
                    elif r_d_l_u == 2:
                        row += 1
                        spiral[row][column] = count + 1
                        count += 1
                    elif r_d_l_u == 3:
                        column -= 1
                        spiral[row][column] = count + 1
                        count += 1
                    elif r_d_l_u == 4:
                        row -= 1
                        spiral[row][column] = count + 1
                        count += 1
            spin += 1
            r_d_l_u += 1
    except IndexError:
        return spiral
    return spiral


#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid(grid, val):
    dim = len(grid)
    row = 0
    column = 0
    # finds row and column of the given value
    for x in range(dim):
        for y in range(dim):
            if grid[x][y] == val:
                row = x
                column = y
    # takes row and column and creates a 2-D list with values around the given value
    subgrid = []
    for sub_row in range(row - 1, row + 2):
        row_list = []
        for sub_col in range(column - 1, column + 2):
            if 0 <= sub_row < dim and 0 <= sub_col < dim:
                row_list.append(grid[sub_row][sub_col])
        if len(row_list) != 0:
            subgrid.append(row_list)
    return subgrid


def main():
    # prompt user to enter dimension of grid
    dimension = abs(int(input('Enter dimension: ')))
    if dimension % 2 == 0:
        dimension += 1
    # prompt user to enter value in grid
    number = int(input('Enter number in spiral: '))
    try:
        if number < 1 or number > dimension * dimension:
            raise ValueError
    except ValueError:
        print('Number not in Range')
        exit()
    spiral = create_spiral(dimension)
    # print subgrid surrounding the value
    subgrid = sub_grid(spiral, number)
    rows = len(subgrid)
    columns = len(subgrid[0])
    for x in range(rows):
        line_str = ''
        for y in range(columns):
            line_str += str(subgrid[x][y]) + ' '
        print(line_str)


if __name__ == "__main__":
    main()
