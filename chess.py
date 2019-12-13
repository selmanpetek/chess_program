chess_board = [[' ', '1', '2', '3', '4', '5', '6', '7', '8'],
               ['1', 'K', 'A', 'F', 'V', 'S', 'F', 'A', 'K'],
               ['2', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
               ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['4', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['5', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
               ['7', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
               ['8', 'k', 'a', 'f', 'v', 's', 'f', 'a', 'k']]
for i in chess_board:
    for j in i:
        print(j, end=' ')
    print()
print("\n")


def sah(board, a, b, c, d):
    if board[a][b] == "S":
        if ((d == b - 1 or d == b + 1) and a == c) or ((c == a - 1 or c == a + 1) and b == d):
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif ((d == b - 1 or d == b + 1) and (c == a - 1 or c == a + 1)) or\
                ((c == a - 1 or c == a + 1) and (d == b - 1 or d == b + 1)):
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif not ((d == b - 1 or d == b + 1) and a == c) or ((c == a - 1 or c == a + 1) and b == d):
            print("\nSah sadece tek birim ilerler.")
        else:
            print("\nOynadiginiz yerde yemek icin tas yok.")
    else:
        return 0


def piyon(board, a, b, c, d):
    if board[a][b] == "P":
        if c == a + 1 and b == d and board[c][d] == '.':
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif c == a + 1 and (d == b - 1 or d == b + 1) and board[c][d] != '.':
            board[c][d] = board[a][b]
            board[a][b] = '.'
        elif not c == a + 1 and b == d and board[c][d] == '.':
            print("\nPiyon sadece ileriye tek birim ilerler.")
        else:
            print("\nPiyon sadece caprazindaki rakip tasi yiyebilir.")
    else:
        return 0


def kale(board, a, b, c, d):
    count = a
    count2 = b
    if board[a][b] == "K":
        if d != b and a != c:
            print("\nKale capraz gidemez")
        elif count < c and b == d:
            while board[count + 1][d] == '.':
                if count >= c:
                    break
                count += 1
            if count == c:
                board[c][d] = board[a][b]
                board[a][b] = '.'
            elif count + 1 == c and (board[c][d] == 'p' or board[c][d] == 'k' or board[c][d] == 'a' or
                                     board[c][d] == 'f' or board[c][d] == 'v' or board[c][d] == 's'):
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
            elif count2 + 1 == d and (board[c][d] == 'p' or board[c][d] == 'k' or board[c][d] == 'a' or
                                      board[c][d] == 'f' or board[c][d] == 'v' or board[c][d] == 's'):
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
            elif count - 1 == c and (board[c][d] == 'p' or board[c][d] == 'k' or board[c][d] == 'a' or
                                     board[c][d] == 'f' or board[c][d] == 'v' or board[c][d] == 's'):
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
            elif count2 - 1 == d and (board[c][d] == 'p' or board[c][d] == 'k' or board[c][d] == 'a' or
                                      board[c][d] == 'f' or board[c][d] == 'v' or board[c][d] == 's'):
                board[c][d] = board[a][b]
                board[a][b] = '.'

    else:
        return 0


def at(board, a, b, c, d):
    if board[a][b] == 'A':
        if ((d == b - 1 or d == b + 1) and (c == a + 2 or c == a - 2)) or\
                ((d == b - 2 or d == b + 2) and (c == a - 1 or c == a + 1)):
            board[c][d] = board[a][b]
            board[a][b] = '.'
        else:
            print("\nAt sadece L seklinde gidebilir.")
            pass
    else:
        return 0



def move(board, a, b, c, d):
    if board[a][b] == '.':
        print("\nHamle yaptiginiz yerde tas yok! Tekrar deneyiniz.")
    elif board[c][d] == "P" or board[c][d] == "A" or board[c][d] == "V" or\
            board[c][d] == "S" or board[c][d] == "F" or board[c][d] == "K":
        print("\nOynadiginiz yerde zaten tas var.")
        pass
    else:
        if a == c and b == d:
            pass
        else:
            piyon(board, a, b, c, d)
            kale(board, a, b, c, d)
            at(board, a, b, c, d)
            sah(board, a, b, c, d)


while 1:
    ilk, ikinci, ucuncu, dorduncu = map(int, input("Nerden nereye? : "))
    if ilk > 8 or ikinci > 8 or ucuncu > 8 or dorduncu > 8 or\
            ilk < 1 or ikinci < 1 or ucuncu < 1 or dorduncu < 1:
        print("\nGirdiginiz sayi 1-8 arasinda olmali")
        pass
    else:
        move(chess_board, ilk, ikinci, ucuncu, dorduncu)
        for i in chess_board:
            for j in i:
                print(j, end=' ')
            print()
        print("\n")

