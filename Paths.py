def count_paths(n, row, col):
    if n == 0:
        return 0
    elif row == n - 1 or col == n - 1:
        return 1
    else:
        return count_paths(n, row + 1, col) + count_paths(n, row, col + 1)


def path_sum(grid, n, row, col):
    if n == 0:
        return 0
    elif row == n - 1 and col == n - 1:
        return grid[row][col]
    elif row == n - 1:
        return grid[row][col] + path_sum(grid, n, row, col + 1)
    elif col == n - 1:
        return grid[row][col] + path_sum(grid, n, row + 1, col)
    else:
        a = grid[row][col] + path_sum(grid, n, row + 1, col)
        b = grid[row][col] + path_sum(grid, n, row, col + 1)
        if a > b:
            return a
        else:
            return b


def main():
    file = open('input.txt')
    n = int(file.readline())
    grid = []
    for lines in range(n):
        a = file.readline()
        a = a.split()
        for i in range(len(a)):
            a[i] = int(a[i])
        grid.append(a)
    for x in range(len(grid)):
        print(grid[x])
    print(path_sum(grid, n, 3, 3))


if __name__ == '__main__':
    main()
