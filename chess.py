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


class trick_move:
    is_rock = False
    is_king = False


for i in chess_board:
    for j in i:
        print(j, end=' ')
    print()
print("\n")


def king(board, a, b, c, d):
    if ((d == b - 1 or d == b + 1) and a == c) or ((c == a - 1 or c == a + 1) and b == d):
        board[c][d] = board[a][b]
        board[a][b] = '.'
        trick_move.is_king = True
    elif ((d == b - 1 or d == b + 1) and (c == a - 1 or c == a + 1)) or\
            ((c == a - 1 or c == a + 1) and (d == b - 1 or d == b + 1)):
        board[c][d] = board[a][b]
        board[a][b] = '.'
        trick_move.is_king = True
    elif not ((d == b - 1 or d == b + 1) and a == c) or ((c == a - 1 or c == a + 1) and b == d):
        print("\nKing can move only a cell.")
    else:
        print("\nThe way you want to play is empty.")


def pawn(board, a, b, c, d):
    is_pawn = False
    if c == a + 1 and b == d and board[c][d] == '.':
        board[c][d] = board[a][b]
        board[a][b] = '.'
    elif c == a + 1 and (d == b - 1 or d == b + 1) and board[c][d] != '.':
        board[c][d] = board[a][b]
        board[a][b] = '.'
        is_pawn = True
    elif not c == a + 1 and b == d and board[c][d] == '.':
        print("\nPawn can move only a cell to forward.")
    else:
        print("\nPawn can take only the pieces which is located at cross of the pawn.")
    if a == 7 and c == 8 and is_pawn is True:
        while is_pawn is True:
            board[c][d] = input("What would you like to choose for your new piece?(R-N-B-Q) : ")
            for i in pieces:
                if i == board[c][d]:
                    is_pawn = False
            if is_pawn is True:
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
            trick_move.is_rock = True
        elif count + 1 == c and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True
    elif count2 < d and a == c:
        while board[c][count2 + 1] == '.':
            if count2 >= d:
                break
            count2 += 1
        if count2 == d:
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True
        elif count2 + 1 == d and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True
    elif count > c and b == d:
        while board[count - 1][d] == '.':
            if count <= c:
                break
            count -= 1
        if count == c:
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True
        elif count - 1 == c and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True
    elif count2 > d and a == c:
        while board[c][count2 - 1] == '.':
            if count2 <= d:
                break
            count2 -= 1
        if count2 == d:
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True
        elif count2 - 1 == d and (board[c][d] == 'p' or board[c][d] == 'r' or board[c][d] == 'n' or
                                  board[c][d] == 'b' or board[c][d] == 'q' or board[c][d] == 'k'):
            board[c][d] = board[a][b]
            board[a][b] = '.'
            trick_move.is_rock = True


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
        if b < d:
            if a < c:
                a_count = a + 1
                b_count = b + 1
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
                b_count = b + 1
                while board[a_count][b_count] == "." and a_count >= c + 1 and b_count <= d - 1:
                    if board[a_count][b_count] != '.':
                        break
                    else:
                        a_count -= 1
                        b_count += 1
                if board[a_count][b_count] == board[c][d]:
                    board[c][d] = board[a][b]
                    board[a][b] = '.'
                else:
                    print("\nThere is a piece on your way.")
        elif b > d:
            if a < c:
                a_count = a + 1
                b_count = b - 1
                while board[a_count][b_count] == "." and a_count <= c - 1 and b_count >= d + 1:
                    if board[a_count][b_count] != '.':
                        break
                    else:
                        a_count += 1
                        b_count -= 1
                if board[a_count][b_count] == board[c][d]:
                    board[c][d] = board[a][b]
                    board[a][b] = '.'
                else:
                    print("\nThere is a piece on your way.")
            elif a > c:
                a_count = a - 1
                b_count = b - 1
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
        if b < d:
            if a < c:
                a_count = a + 1
                b_count = b + 1
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
                b_count = b + 1
                while board[a_count][b_count] == "." and a_count >= c + 1 and b_count <= d - 1:
                    if board[a_count][b_count] != '.':
                        break
                    else:
                        a_count -= 1
                        b_count += 1
                if board[a_count][b_count] == board[c][d]:
                    board[c][d] = board[a][b]
                    board[a][b] = '.'
                else:
                    print("\nThere is a piece on your way.")
        elif b > d:
            if a < c:
                a_count = a + 1
                b_count = b - 1
                while board[a_count][b_count] == "." and a_count <= c - 1 and b_count >= d + 1:
                    if board[a_count][b_count] != '.':
                        break
                    else:
                        a_count += 1
                        b_count -= 1
                if board[a_count][b_count] == board[c][d]:
                    board[c][d] = board[a][b]
                    board[a][b] = '.'
                else:
                    print("\nThere is a piece on your way.")
            elif a > c:
                a_count = a - 1
                b_count = b - 1
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


def check(board, a, b, c, d):
    if (board[a][b] == 'R' and board[c][d] == 'K') or (board[a][b] == 'K' and board[c][d] == 'R'):
        if b == 1 or (b == 5 and  d == 8):
            count = b + 1
            while board[a][count] == '.':
                count += 1
            if count == d and b == 1:
                board[1][4] = board[a][b]
                board[a][b] = '.'
                board[1][3] = board[c][d]
                board[c][d] = '.'
            elif count == d and b == 5:
                board[1][7] = board[a][b]
                board[a][b] = '.'
                board[1][6] = board[c][d]
                board[c][d] = '.'
            else:
                print("\nThere is already a piece between the rock and the king.")
        elif (b == 5 and d == 1) or b == 8:
            count = b - 1
            while board[a][count] == '.':
                count -= 1
            if count == d and b == 5:
                board[1][3] = board[a][b]
                board[a][b] = '.'
                board[1][4] = board[c][d]
                board[c][d] = '.'
            elif count == d and b == 8:
                board[1][6] = board[a][b]
                board[a][b] = '.'
                board[1][7] = board[c][d]
                board[c][d] = '.'
            else:
                print("\nThere is already a piece between the rock and the king.")


def move(board, a, b, c, d):
    if board[a][b] == '.':
        print("\nInvalid move. Try again!")
    elif board[c][d] == "P" or board[c][d] == "N" or board[c][d] == "Q" or\
            board[c][d] == "K" or board[c][d] == "B" or board[c][d] == "R":
        if board[c][d] == 'K' or board[c][d] == 'R':
            if trick_move.is_rock is False and trick_move.is_king is False:
                check(board, a, b, c, d)
            else:
                print("\nYou have already move the king or the rock.")
        else:
            print("\nThere is already a piece at the cell that you want to play to.")
    else:
        if a == c and b == d:
            pass
        else:
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