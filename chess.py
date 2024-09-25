def isPawnMoveCorrect(x1, y1, x2, y2):
    return x2 == x1 and y2 - y1 == 1

def isRookMoveCorrect(x1, y1, x2, y2):
    return x2 == x1 or y2 == y1

def isKnightMoveCorrect(x1, y1, x2, y2):
    return abs(x2 - x1) == 2 and abs(y2 - y1) == 1

def isBishopMoveCorrect(x1, y1, x2, y2):
    return abs(x2 - x1) == abs(y2 - y1)

def isQueenMoveCorrect(x1, y1, x2, y2):
    return isBishopMoveCorrect(x1, y1, x2, y2) or isRookMoveCorrect(x1, y1, x2, y2)

def isKingMoveCorrect(x1, y1, x2, y2):
    return (abs(x2 - x1) == abs(y2 - y1) == 1) or ((x2 == x1 and y2 - y1 == 1) or (y2 == y1 and x2 - x1 == 1))

def convertAChessSquareIntoCoordinates(str):
    return [ord(str[0]) - ord('a'), int(str[1])]

print('введите начальную и конечную клетки')
start = input()
final = input()

coord_start = convertAChessSquareIntoCoordinates(start)
coord_final = convertAChessSquareIntoCoordinates(final)

print('введите фигуру')
chess_piece = input()

functionChess = {'пешка': isPawnMoveCorrect,
                 'ладья': isRookMoveCorrect,
                 'слон': isBishopMoveCorrect,
                 'конь': isKnightMoveCorrect,
                 'королева': isQueenMoveCorrect,
                 'король': isKingMoveCorrect}

ans = functionChess[chess_piece](*coord_start, *coord_final)

if ans:
    print('корректный ход')
else:
    print('некорректный ход')
