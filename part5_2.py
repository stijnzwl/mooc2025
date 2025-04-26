def double_items(numbers: list):
    new_list = numbers[:]
    for i in range(len(new_list)):
        new_list[i] = 2 * new_list[i]

    return new_list


numbers = [2, 4, 5, 3, 11, -4]
numbers_doubled = double_items(numbers)
print("original:", numbers)
print("doubled:", numbers_doubled)


def remove_smallest(numbers: list):
    numbers.sort()
    numbers.pop(0)


numbers = [2, 4, 6, 1, 3, 5]
remove_smallest(numbers)
print(numbers)  


def print_sudoku(sudoku: list):
    other_count = 0
    for row in sudoku:
        other_count += 1
        count = 0
        for col in row:
            if col == 0:
                print("_", end=" ")
                count += 1
                if count == 3:
                    print(" ", end=" ")
                    count = 0
            else:
                print(f"{str(col)}", end=" ")
                count +=1
                if count == 3:
                    print(" ", end=" ")
                    count = 0
        if other_count == 3:
            print()
            other_count = 0       
        print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
    return sudoku

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    for row in sudoku:
        new_sudoku.append(row[:])
    new_sudoku[row_no][column_no] = number

    return new_sudoku


sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid_copy = copy_and_add(sudoku, 0, 0, 2)
print("Original:")
print_sudoku(sudoku)
print()
print("Copy:")
print_sudoku(grid_copy)


