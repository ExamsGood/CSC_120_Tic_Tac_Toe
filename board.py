board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def print_board():
    print("    1    2    3")
    count = 1
    for row in board:
        print(count, row)
        count += 1


print_board()
