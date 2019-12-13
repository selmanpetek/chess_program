chess_board = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
               ['1', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
               ['2', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
               ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['4', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['5', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['7', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
               ['8', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pieces = ['R', 'N', 'B', 'Q']
for i in chess_board:
    for j in i:
        print(j, end=' ')
    print()
print("\n")


def king(board, a, b, c, d):
    if ((d == b - 1 or d == b + 1) and a == c) or ((c == a - 1 or c == a + 1) and b == d):
        board[c][d] = board[a][b]
        board[a][b] = '.'
    elif ((d == b - 1 or d == b + 1) and (c == a - 1 or c == a + 1)) or\
            ((c == a - 1 or c == a + 1) and (d == b - 1 or d == b + 1)):
        board[c][d] = board[a][b]
        board[a][b] = '.'
    elif not ((d == b - 1 or d == b + 1) and a == c) or ((c == a - 1 or c == a + 1) and b == d):
        print("\nKing can move only a cell.")
    else:
        print("\nThe way you want to play is empty.")


def pawn(board, a, b, c, d):
    is_Pawn = False
    if c == a + 1 and b == d and board[c][d] == '.':
        board[c][d] = board[a][b]
        board[a][b] = '.'
    elif c == a + 1 and (d == b - 1 or d == b + 1) and board[c][d] != '.':
        board[c][d] = board[a][b]
        board[a][b] = '.'
        is_Pawn = True
    elif not c == a + 1 and b == d and board[c][d] == '.':
        print("\nPawn can move only a cell to forward.")
    else:
        print("\nPawn can take only the pieces which is located at cross of the pawn.")
    if a == 7 and c == 8 and is_Pawn is True:
        while is_Pawn is True:
            board[c][d] = input("What would you like to choose for your new piece?(R-N-B-Q) : ")
            for i in pieces:
                if i == board[c][d]:
                    is_Pawn = False
            if is_Pawn is True:
                print("Your character has to be one of (R-N-B-Q).")


def rock(board, a, b, c, d):
    count = a
    count2 = b
    if d != b and a != c:
        print("\nRock can move only straight.")
    elif count < c and b == d:
        while board[count + 1][d] == '.':
            if count >= c:
                break
            count += 1
        if count == c:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count + 1 == c and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif count2 < d and a == c:
        while board[c][count2 + 1] == '.':
            if count2 >= d:
                break
            count2 += 1
        if count2 == d:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count2 + 1 == d and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif count > c and b == d:
        while board[count - 1][d] == '.':
            if count <= c:
                break
            count -= 1
        if count == c:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count - 1 == c and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif count2 > d and a == c:
        while board[c][count2 - 1] == '.':
            if count2 <= d:
                break
            count2 -= 1
        if count2 == d:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count2 - 1 == d and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'


def knight(board, a, b, c, d):
    if ((d == b - 1 or d == b + 1) and (c == a + 2 or c == a - 2)) or\
            ((d == b - 2 or d == b + 2) and (c == a - 1 or c == a + 1)):
        board[c][d] = board[a][b]
        board[a][b] = '.'
    else:
        print("\nKnight can move only type of L.")
        pass


def queen(board, a, b, c, d):
    count = a
    count2 = b
    if count < c and b == d:
        while board[count + 1][d] == '.':
            if count >= c:
                break
            count += 1
        if count == c:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count + 1 == c and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                 board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif count2 < d and a == c:
        while board[c][count2 + 1] == '.':
            if count2 >= d:
                break
            count2 += 1
        if count2 == d:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count2 + 1 == d and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif count > c and b == d:
        while board[count - 1][d] == '.':
            if count <= c:
                break
            count -= 1
        if count == c:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count - 1 == c and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                 board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif count2 > d and a == c:
        while board[c][count2 - 1] == '.':
            if count2 <= d:
                break
            count2 -= 1
        if count2 == d:
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif count2 - 1 == d and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
    elif abs(b - d) == abs(a - c):
        if a < c:
            a_count = a + 1
            b_count = b + 1
            count = abs(a - c)
            while board[a_count][b_count] == "." and a_count <= c - 1 and b_count <= d - 1:
                if board[a_count][b_count] != '.':
                    break
                else:
                    a_count += 1
                    b_count += 1
            if board[a_count][b_count] == board[c][d]:
                board[c][d] = board[a][b]
                board[a][b] = '.'
            else:
                print("\nThere is a piece on your way.")
        elif a > c:
            a_count = a - 1
            b_count = b - 1
            count = abs(a - c)
            while board[a_count][b_count] == "." and a_count >= c + 1 and b_count >= d + 1:
                if board[a_count][b_count] != '.':
                    break
                else:
                    a_count -= 1
                    b_count -= 1
            if board[a_count][b_count] == board[c][d]:
                board[c][d] = board[a][b]
                board[a][b] = '.'
            else:
                print("\nThere is a piece on your way.")


def bishop(board, a, b, c, d):
    if abs(b - d) == abs(a - c):
        if a < c:
            a_count = a + 1
            b_count = b + 1
            count = abs(a - c)
            while board[a_count][b_count] == "." and a_count <= c - 1 and b_count <= d - 1:
                if board[a_count][b_count] != '.':
                    break
                else:
                    a_count += 1
                    b_count += 1
            if board[a_count][b_count] == board[c][d]:
                board[c][d] = board[a][b]
                board[a][b] = '.'
            else:
                print("\nThere is a piece on your way.")
        elif a > c:
            a_count = a - 1
            b_count = b - 1
            count = abs(a - c)
            while board[a_count][b_count] == "." and a_count >= c + 1 and b_count >= d + 1:
                if board[a_count][b_count] != '.':
                    break
                else:
                    a_count -= 1
                    b_count -= 1
            if board[a_count][b_count] == board[c][d]:
                board[c][d] = board[a][b]
                board[a][b] = '.'
            else:
                print("\nThere is a piece on your way.")
    else:
        print("\nBishop can move only cross way.")


def move(board, a, b, c, d):
    if board[a][b] == '.':
        print("\nInvalid move. Try again!")
    elif board[c][d] == "P" or board[c][d] == "N" or board[c][d] == "Q" or\
            board[c][d] == "K" or board[c][d] == "B" or board[c][d] == "R":
        print("\nThere is already a piece at the cell that you want to play to.")
        pass
    else:
        if a == c and b == d:
            pass
        else:
            is_r = False
            is_k = False
            if board[a][b] == 'P':
                pawn(board, a, b, c, d)
            elif board[a][b] == 'R':
                rock(board, a, b, c, d)
            elif board[a][b] == 'N':
                knight(board, a, b, c, d)
            elif board[a][b] == 'B':
                bishop(board, a, b, c, d)
            elif board[a][b] == 'K':
                king(board, a, b, c, d)
            elif board[a][b] == 'Q':
                queen(board, a, b, c, d)


while 1:
    try:
        second, first, forth, third = map(str, input("From where to where? : ").upper())
        first = int(first)
        third = int(third)
    except:
        print("\nYou have to put 4 characters.")
        continue
    if first > 8 or third > 8 or\
            first < 1 or third < 1:
        print("\nThe numbers have to be between 1-8.")
        pass
    elif second and forth:
        is_i = False
        is_j = False
        for i in column:
            if i == second:
                second = column.index(i) + 1
                is_i = True
        for j in column:
            if j == forth:
                forth = column.index(j) + 1
                is_j = True

        if is_i == False or is_j == False:
            print("\nColumn has to be between A-H.")
        else:
            
            move(chess_board, first, second, third, forth)
            for i in chess_board:
                for j in i:
                    print(j, end=' ')
                print()
            print("\n")