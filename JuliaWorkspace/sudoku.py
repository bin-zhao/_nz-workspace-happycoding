#!/usr/bin/env python
# -*- coding: utf-8 -*-

def locate_grid(index):
    # (grid_line, grid_row, table_line, table_row)
    return (index // 27, index % 9 // 3, index // 9, index % 9)

def get_grid_state(index, sudoku):
    result = 0

    grid_line, grid_row, table_line, table_row = locate_grid(index)

    # print(sudoku[table_line * 9 : (table_line + 1) * 9])

    for i in range(9):
        grid_index = grid_line * 27 + grid_row * 3 + i // 3 * 9 + i % 3
        if sudoku[grid_index] != 0:
            result |= 1 << (sudoku[grid_index] - 1)

        line_index = table_line * 9 + i
        if sudoku[line_index] != 0:
            result |= 1 << (sudoku[line_index] - 1)

        row_index = table_row + i * 9
        if sudoku[row_index] != 0:
            result |= 1 << (sudoku[row_index] - 1)
        
        # pass
    
    return 10 + result

def _bits2oct(state):
    return str(oct(state - 10))[2:]

def _bits2nums(state):
    if state < 10:
        return ""

    nums = []
    state = (state - 10) ^ 511
    for i in range(9):
        if state & (1 << i) != 0:
            nums.append(i + 1)

    return nums

def _nums2digit(nums):
    result = 0
    unit = 1
    for n in reversed(nums):
        result += n * unit
        unit *= 10

    return result

def print_sudoku(sudoku):
    print(sudoku)
    for i in range(9):
        # line = "\t\t".join([(str(sudoku[j]) if sudoku[j] < 10 else "[%s]" % _bits2oct(sudoku[j])) for j in range(i * 9, (i + 1) * 9)])
        line = "\t".join([("%-11s" % ("_") if sudoku[j] < 10 else "%-11d" % _nums2digit(_bits2nums(sudoku[j]))) for j in range(i * 9, (i + 1) * 9)])
        print(line)
        if (i + 1) % 3 == 0:
            print()

def main():
    sudoku = [
        0, 0, 9,        8, 0, 0,        0, 0, 0,
        5, 0, 1,        0, 7, 2,        0, 0, 0,
        0, 0, 7,        0, 0, 0,        0, 1, 3,

        0, 9, 0,        0, 0, 0,        0, 0, 2,
        0, 1, 0,        3, 9, 6,        0, 0, 0,
        7, 5, 0,        2, 0, 0,        0, 0, 0,

        9, 6, 2,        4, 0, 0,        3, 7, 8,
        1, 0, 5,        0, 0, 0,        4, 2, 0,
        0, 7, 0,        0, 2, 0,        0, 0, 0
    ]

    # sudoku_state = []
    # for i in range(81):
    #     sudoku_state.append(locate_grid(i))
    # for i in range(9):
    #     print(sudoku_state[i * 9 : (i + 1) * 9])

    # print(oct(get_grid_state(0, sudoku)))

    # line = []
    # grid_line, grid_row, _, _ = locate_grid(79)
    # for j in range(9):
    #     grid_index = grid_line * 27 + grid_row * 3 + j // 3 * 9 + j % 3
    #     line.append(grid_index)
    # print(line)

    # bits = 0o410
    # print(bin(bits))
    # print(_bits2nums(bits + 10))

    # return

    sudoku_state = []
    for i in range(len(sudoku)):
        if sudoku[i] == 0:
            sudoku_state.append(get_grid_state(i, sudoku))
        else:
            sudoku_state.append(sudoku[i])
    
    print_sudoku(sudoku_state)

main()
print("done!")
