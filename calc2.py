# b
matrix = [['d', '@', '2', '2'],
          ['s', 'f', '3', '2'],
          ['s', '@', '1', '@'],
          ['d', '@', '3', 'v']]


def calculation(matrix):
    el = '@'
    count_el = 0
    for row in matrix:
        for cell in row:

            if cell == el:
                count_el += 1
    return count_el


if __name__ == '__main__':
    print(calculation(matrix))
