from typing import Dict, Any

dict_field = {'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'q', 'e8': 'k', 'f8': 'b', 'g8': 'n', 'h8': 'r',
              'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
              'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
              'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
              'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
              'a3': '.', 'b3': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.', 'g3': '.', 'h3': '.',
              'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
              'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R'}

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'boo']
dict_changes = {}
player_turn = 0
list_of_moves = []
print(f'     Игра началась!\n     |1__Pаунд__1|\n')

def print_board():
    print('    A B C D E F G H' + '\n')
    array_row = list(dict_field.values())
    array = []
    c = 0
    c_of_c = 8
    for el in range(len(array_row)):
        array.append(array_row[el])
        c += 1
        if c == 8:
            print(c_of_c, ' ', *array, ' ', c_of_c)
            c_of_c -= 1
            array = []
            c = 0
    return '\n    A B C D E F G H\n'


print(f'_И Г Р О В О Е  П О Л Е_\n')
print(print_board())


def valid_move(move, player_turn=0, test=0):
    if test == 0:
        dict_changes.clear()
    if len(move) < 2:
        return False
    for key, value in dict_field.items():
        if key == move:  # проверка на базовые ходы пешки
            if dict_field[move[0] + (str(int(move[1]) - 2) if player_turn % 2 == 0 else str(int(move[1]) + 2))] == (
                    'P' if player_turn % 2 == 0 else 'p') and move[1] == ('4' if player_turn % 2 == 0 else '5') and \
                    dict_field[move[0] + (str(int(move[1]) - 1) if player_turn % 2 == 0 else str(int(move[1]) + 1))] == '.':  # проверка первого хода пешки на +2
                if test == 0:
                    dict_changes[move[0] + (str(int(move[1]) - 2) if player_turn % 2 == 0 else str(int(move[1]) + 2))] = '.'
                    dict_changes[key] = ('P' if player_turn % 2 == 0 else 'p')
                    return True
                else:
                    return True
            elif dict_field[move] == '.' and dict_field[
                move[0] + (str(int(move[1]) - 1) if player_turn % 2 == 0 else str(int(move[1]) + 1))] == (
                    'P' if player_turn % 2 == 0 else 'p'):
                if test == 0:
                    dict_changes[move[0] + (str(int(move[1]) - 1) if player_turn % 2 == 0 else str(
                        int(move[1]) + 1))] = '.'  # если не +2 то пешка на +1
                    dict_changes[key] = ('P' if player_turn % 2 == 0 else 'p')
                    return True
                else:
                    return True
        if move[0] in 'abcdefgh' and move[1] == 'x' and move[-2:] in dict_field.keys() and dict_field[
            move[-2:]] in ('rnpbqk' if player_turn % 2 == 0 else 'RNPBQK'):  # пешка ест
            if letters.index(move[0]) - letters.index(move[2]) == -1 and dict_field[move[0] + (str(int(move[-1]) - 1) if player_turn % 2 == 0 else str(int(move[-1]) + 1))] == ('P' if player_turn % 2 == 0 else 'p'):
                if test == 0:  # проверка с какой стороны ест пешка
                    dict_changes[
                        move[0] + (str(int(move[3]) - 1) if player_turn % 2 == 0 else str(int(move[3]) + 1))] = '.'
                    dict_changes[move[2:]] = ('P' if player_turn % 2 == 0 else 'p')
                    return True
                else:
                    return True
            elif letters.index(move[0]) - letters.index(move[2]) == 1 and dict_field[move[0] + (str(int(move[-1]) - 1) if player_turn % 2 == 0 else str(int(move[-1]) + 1))] == ('P' if player_turn % 2 == 0 else 'p'):
                if test == 0:
                    dict_changes[letters[letters.index(move[2]) + 1] + (
                        str(int(move[3]) - 1) if player_turn % 2 == 0 else str(int(move[3]) + 1))] = '.'
                    dict_changes[move[2:]] = ('P' if player_turn % 2 == 0 else 'p')
                    return True
                else:
                    return True
    if move[0] == ('N' if player_turn % 2 == 0 else 'n'):
        if move[-2] in 'abcdefgh' and move[-1] in '12345678':  # обычный ход конём
            for knight in [letters[(letters.index(move[-2]) + 1) if letters.index(move[-2]) + 1 <= 7 else 8] + str(int(move[-1]) + 2),
                           letters[(letters.index(move[-2]) + 2) if letters.index(move[-2]) + 2 <= 7 else 8] + str(int(move[-1]) + 1),
                           letters[(letters.index(move[-2]) + 2) if letters.index(move[-2]) + 2 <= 7 else 8] + str(int(move[-1]) - 1),
                           letters[(letters.index(move[-2]) + 1) if letters.index(move[-2]) + 1 <= 7 else 8] + str(int(move[-1]) - 2),
                           letters[(letters.index(move[-2]) - 1) if letters.index(move[-2]) - 1 <= 7 else 8] + str(int(move[-1]) - 2),
                           letters[(letters.index(move[-2]) - 2) if letters.index(move[-2]) - 2 <= 7 else 8] + str(int(move[-1]) - 1),
                           letters[(letters.index(move[-2]) - 2) if letters.index(move[-2]) - 2 <= 7 else 8] + str(int(move[-1]) + 1),
                           letters[(letters.index(move[-2]) - 1) if letters.index(move[-2]) - 1 <= 7 else 8] + str(int(move[-1]) + 2)]:
                if knight in dict_field.keys() and dict_field[knight] == ('N' if player_turn % 2 == 0 else 'n') and \
                        (len(move) == 3 and 'x' not in move and dict_field[move[-2:]] == '.' or
                         len(move) == 4 and 'x' in move and dict_field[move[2:]] in (
                                 'rnpbqk' if player_turn % 2 == 0 else 'RNPBQK')):
                    if test == 0:
                        dict_changes[knight] = '.'
                        dict_changes[move[-2:]] = ('N' if player_turn % 2 == 0 else 'n')
                        return True
                    else:
                        return True
            if move[0] == ('N' if player_turn % 2 == 0 else 'n') and move[1] in 'abcdefgh' and move[
                                                                                               -2:] in dict_field.keys() and \
                    (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                if move[2] == 'x' and dict_field[move[-2:]] == '.' or 'x' not in move and dict_field[move[-2:]] != '.':
                    return False
                else:
                    for keys, values in dict_field.items():
                        if move[-2] in keys and dict_field[keys] == ('N' if player_turn % 2 == 0 else 'n') \
                                and move[-2:] in dict_field.keys():
                            if test == 0:
                                dict_changes[keys] = '.'
                                dict_changes[move[-2:]] = ('N' if player_turn % 2 == 0 else 'n')
                                return True
                            else:
                                return True
            elif move[0] == ('N' if player_turn % 2 == 0 else 'n') and move[1] in '12345678' and move[
                                                                                                 -2:] in dict_field.keys() and \
                    (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                if move[1] == 'x' and dict_field[move[-2:]] == '.' or 'x' not in move and dict_field[move[-2:]] != '.':
                    return False
                else:
                    for keys, values in dict_field.items():
                        if move[1] in keys and dict_field[keys] == ('N' if player_turn % 2 == 0 else 'n') and move[
                                                                                                              -2:] in dict_field.keys():
                            if test == 0:
                                dict_changes[keys] = '.'
                                dict_changes[move[-2:]] = ('N' if player_turn % 2 == 0 else 'n')
                                return True
                            else:
                                return True
    if move[0] == ('B' if player_turn % 2 == 0 else 'b'):
        if (len(move) == 3 and 'x' not in move and dict_field[move[-2:]] == '.' or len(move) == 4 and move[1] == 'x' and
            move[-2:] in dict_field.keys() and dict_field[move[-2:]] in (
                    'rnbqkp' if player_turn % 2 == 0 else 'RNBQKP')) and move[-2] in 'abcdefgh' and move[
            -1] in '12345678':
            if move[-2] in 'abcdefgh' and move[-1] in '12345678' and (len(move) == 3 or len(move) == 4):
                possible_bishops = []
                for one_move in [letters[letters.index(move[-2]) + 1] + str(int(move[-1]) + 1),
                                 letters[letters.index(move[-2]) + 1] + str(int(move[-1]) - 1),
                                 letters[letters.index(move[-2]) - 1] + str(int(move[-1]) + 1),
                                 letters[letters.index(move[-2]) - 1] + str(int(move[-1]) - 1)]:
                    if one_move in dict_field.items():
                        if dict_field[one_move] == ('B' if player_turn % 2 == 0 else 'b') and 'x' in move and \
                                dict_field[move[-2:]] != '.':
                            if test == 0:

                                dict_changes[one_move] = '.'
                                dict_changes[move[-2:]] = ('B' if player_turn % 2 == 0 else 'b')
                                return True
                            else:
                                return True
                        elif dict_field[one_move] == ('B' if player_turn % 2 == 0 else 'b') and 'x' not in move and \
                                dict_field[
                                    move[-2:]] == '.':
                            # print(2)
                            if test == 0:  # если ход на одну клетку в любую сторону
                                dict_changes[one_move] = '.'
                                dict_changes[move[-2:]] = ('B' if player_turn % 2 == 0 else 'b')
                                return True
                            else:
                                return True

                for shift in range(1, 7):
                    for bishop in [
                        letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                            int(move[-1]) + shift),
                        letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                            int(move[-1]) - shift),
                        letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                            int(move[-1]) + shift),
                        letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                            int(move[-1]) - shift)]:
                        if bishop in dict_field.keys():
                            possible_bishops.append(bishop)
                        else:
                            possible_bishops.append(0)
                for my_bishop in range(len(possible_bishops)):
                    if possible_bishops[my_bishop] != 0:
                        if dict_field[possible_bishops[my_bishop]] == ('B' if player_turn % 2 == 0 else 'b'):
                            if int(move[-1]) > int(possible_bishops[my_bishop][1]):
                                for new_bishop in range(len(possible_bishops)):
                                    if possible_bishops[new_bishop] != 0:
                                        if my_bishop % 4 == new_bishop % 4 and int(move[-1]) >= int(
                                                possible_bishops[new_bishop][1]) > int(possible_bishops[my_bishop][1]):
                                            if dict_field[possible_bishops[new_bishop]] == '.':
                                                continue
                                            else:
                                                return False
                            elif int(move[-1]) < int(possible_bishops[my_bishop][1]):
                                for new_bishop in range(len(possible_bishops)):
                                    if possible_bishops[new_bishop] != 0:
                                        if my_bishop % 4 == new_bishop % 4 and int(move[-1]) <= int(
                                                possible_bishops[new_bishop][1]) < int(possible_bishops[my_bishop][1]):
                                            if dict_field[possible_bishops[new_bishop]] == '.':
                                                continue
                                            else:
                                                return False
                            if test == 0:
                                dict_changes[possible_bishops[my_bishop]] = '.'
                                dict_changes[move[-2:]] = ('B' if player_turn % 2 == 0 else 'b')
                                return True
                            else:
                                return True
    if move[0] == ('R' if player_turn % 2 == 0 else 'r'):
        if 'x' in move and dict_field[move[-2:]] in (
        'prnbqk' if player_turn % 2 == 0 else 'PRNBQK') or 'x' not in move and dict_field[move[-2:]] == '.':
            rooks_num = 0
            possible_rooks = []
            valid = False
            my_rook = ''
            trigger = 0
            for shift in range(1, 8):
                for rook in [
                    letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + move[-1],
                    move[-2] + str(int(move[-1]) + shift),
                    letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + move[-1],
                    move[-2] + str(int(move[-1]) - shift)]:
                    if rook in dict_field.keys():
                        possible_rooks.append(rook)
                    else:
                        possible_rooks.append(0)
            for check_num_of_rooks in range(len(possible_rooks)):
                if possible_rooks[check_num_of_rooks] != 0:
                    if dict_field[possible_rooks[check_num_of_rooks]] == ('R' if player_turn % 2 == 0 else 'r'):
                        valid = True
                        # print(possible_rooks[check_num_of_rooks], 'my possible rook')
                        for valid_rook in range(len(possible_rooks)):
                            if possible_rooks[valid_rook] != 0 and valid_rook % 4 == check_num_of_rooks % 4 and \
                                    valid_rook != check_num_of_rooks:
                                if possible_rooks[valid_rook][1] > possible_rooks[check_num_of_rooks][1] and move[-1] > \
                                        possible_rooks[check_num_of_rooks][1] or \
                                        possible_rooks[valid_rook][1] < possible_rooks[check_num_of_rooks][1] and move[
                                    -1] < \
                                        possible_rooks[check_num_of_rooks][1] or \
                                        possible_rooks[valid_rook][1] == possible_rooks[check_num_of_rooks][1] == move[
                                    -1] and (letters.index(move[-2]) < letters.index(
                                    possible_rooks[valid_rook][0]) < letters.index(
                                    possible_rooks[check_num_of_rooks][0]) or letters.index(move[-2]) > letters.index(
                                    possible_rooks[valid_rook][0]) > letters.index(
                                    possible_rooks[check_num_of_rooks][0])):
                                    if dict_field[possible_rooks[valid_rook]] == '.':
                                        continue
                                    else:
                                        valid = False
                                        break

                        if valid:
                            rooks_num += 1
                if valid:
                    my_rook = possible_rooks[check_num_of_rooks]
                    valid = False
                    trigger += 1
            if my_rook != '' and rooks_num == 1 or my_rook != '' and rooks_num == 1 and trigger == 1:
                if test == 0:
                    dict_changes[my_rook] = '.'
                    dict_changes[move[-2:]] = ('R' if player_turn % 2 == 0 else 'r')
                    return True
                else:
                    return True
            if rooks_num == 2 and len(move) == 4 or rooks_num == 2 and len(move) == 4 and trigger == 1:
                if move[0] == ('R' if player_turn % 2 == 0 else 'r') and move[1] in 'abcdefgh' and move[
                                                                                                   -2:] in dict_field.keys() and \
                        (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                    if move[2] == 'x' and dict_field[move[-2:]] == '.' or 'x' not in move and dict_field[
                        move[-2:]] != '.':
                        return False
                    else:
                        for keys, values in dict_field.items():
                            if move[1] in keys and dict_field[keys] == ('R' if player_turn % 2 == 0 else 'r') and move[
                                                                                                                  -2:] in dict_field.keys():
                                if test == 0:
                                    dict_changes[keys] = '.'
                                    dict_changes[move[-2:]] = ('R' if player_turn % 2 == 0 else 'r')
                                    return True
                                else:
                                    return True
                elif move[0] == ('R' if player_turn % 2 == 0 else 'r') and move[1] in '12345678' and move[
                                                                                                     -2:] in dict_field.keys() and \
                        (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                    if move[2] == 'x' and dict_field[move[-2:]] == '.' or 'x' not in move and dict_field[
                        move[-2:]] != '.':
                        return False
                    else:
                        for keys, values in dict_field.items():
                            if move[1] in keys and dict_field[keys] == ('R' if player_turn % 2 == 0 else 'r') and move[
                                                                                                                  -2:] in dict_field.keys():
                                if test == 0:
                                    dict_changes[keys] = '.'
                                    dict_changes[move[-2:]] = ('R' if player_turn % 2 == 0 else 'r')
                                    return True
                                else:
                                    return True
    if move[0] == ('Q' if player_turn % 2 == 0 else 'q'):
        possible_queens = []
        if (len(move) == 3 and 'x' not in move and dict_field[move[-2:]] == '.' or len(move) == 4 and move[1] == 'x' and
            dict_field[move[-2:]] in ('prnbqk' if player_turn % 2 == 0 else 'PRNBQK')) and \
                move[-2] in 'abcdefgh' and move[-1] in '12345678' and move[-2:] in dict_field.keys():
            for one_move in [letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + move[-1],
                             letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + move[-1],
                             move[-2] + str(int(move[-1]) + 1),
                             move[-2] + str(int(move[-1]) - 1),
                             letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                 int(move[-1]) + 1),
                             letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                 int(move[-1]) - 1),
                             letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                 int(move[-1]) + 1),
                             letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                 int(move[-1]) - 1)]:
                if one_move in dict_field.keys():
                    if dict_field[one_move] == ('Q' if player_turn % 2 == 0 else 'q'):
                        if test == 0:
                            dict_changes[one_move] = '.'
                            dict_changes[move[-2:]] = ('Q' if player_turn % 2 == 0 else 'q')
                            return True
                        else:
                            return True
            for shift in range(1, 8):
                for queen in [
                    letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + move[-1],
                    letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                        int(move[-1]) + shift),
                    move[-2] + str(int(move[-1]) + shift),
                    letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                        int(move[-1]) + shift),
                    letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + move[-1],
                    letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                        int(move[-1]) - shift),
                    move[-2] + str(int(move[-1]) - shift),
                    letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                        int(move[-1]) - shift)]:
                    if queen in dict_field.keys():
                        possible_queens.append(queen)
                    else:
                        possible_queens.append(0)
            for my_queen in range(len(possible_queens)):
                if possible_queens[my_queen] != 0:
                    if dict_field[possible_queens[my_queen]] == ('Q' if player_turn % 2 == 0 else 'q'):
                        valid = True
                        for valid_queen in range(len(possible_queens)):
                            if possible_queens[
                                valid_queen] != 0 and valid_queen % 8 == my_queen % 8 and valid_queen != my_queen:
                                if possible_queens[my_queen][1] > possible_queens[valid_queen][1] > move[-1] or \
                                        possible_queens[my_queen][1] < possible_queens[valid_queen][1] < move[-1] or \
                                        (possible_queens[my_queen][0] > possible_queens[valid_queen][0] > move[-2] or
                                         possible_queens[my_queen][0] < possible_queens[valid_queen][0] < move[-2]) and \
                                        possible_queens[my_queen][1] == possible_queens[valid_queen][1] == move[-1]:
                                    if dict_field[possible_queens[valid_queen]] == '.':
                                        continue
                                    else:
                                        valid = False
                                        break
                        if valid:
                            if test == 0:
                                dict_changes[possible_queens[my_queen]] = '.'
                                dict_changes[move[-2:]] = ('Q' if player_turn % 2 == 0 else 'q')
                                return True
                            else:
                                return True
    if move[0] == ('K' if player_turn % 2 == 0 else 'k'):
        if (len(move) == 3 and move[1] in 'abcdefgh' and move[2] in '12345678' and 'x' not in move and dict_field[move[-2:]] == '.' or len(move) == 4 and move[1] == 'x' and
            dict_field[move[-2:]] in ('prnbqk' if player_turn % 2 == 0 else 'PRNBQK')) and \
                move[-2] in 'abcdefgh' and move[-1] in '12345678' and move[-2:] in dict_field.keys():
            if letters[letters.index(move[-2]) - 1] + str(int(move[-1]) + 1) and letters[
                letters.index(move[-2]) + 1] + str(int(move[-1]) + 1) in dict_field.items():
                if dict_field[letters[letters.index(move[-2]) - 1] + str(int(move[-1]) + 1)] == (
                'p' if player_turn % 2 == 0 else 'P') \
                        or dict_field[letters[letters.index(move[-2]) + 1] + str(int(move[-1]) + 1)] == (
                'p' if player_turn % 2 == 0 else 'P'):
                    return False
            for one_move in [letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + move[-1],
                             letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + move[-1],
                             move[-2] + str(int(move[-1]) + 1),
                             move[-2] + str(int(move[-1]) - 1),
                             letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                 int(move[-1]) + 1),
                             letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                 int(move[-1]) - 1),
                             letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                 int(move[-1]) + 1),
                             letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                 int(move[-1]) - 1)]:
                if one_move in dict_field.keys():
                    if dict_field[one_move] == ('K' if player_turn % 2 == 0 else 'k'):
                        dict_changes[one_move] = '.'
                        dict_changes[move[-2:]] = ('K' if player_turn % 2 == 0 else 'k')
                        return True
    return False


def check(player_turn):
    for key1, val1 in dict_field.items():
        if val1 == ('K' if player_turn % 2 == 0 else 'k'):
            for key2, val2 in dict_field.items():
                if val2 in ('rnbqk' if player_turn % 2 == 0 else 'RNBQK'):
                    if valid_move(val2 + 'x' + key1, 1 if val2 in 'rnbqk' else 0, 1):
                        return True
                    elif valid_move(key2[0] + 'x' + key1, 1 if val2 in 'rnbqk' else 0, 1):
                        return True
                    else:
                        continue

    return False


def game(player_turn, dict_changes):
    turns = 2
    while True:
        move = (input('ход первого игрока: ') if player_turn % 2 == 0 else input('ход второго игрока: '))
        if move == 'moves':
            continue
        if move == 'save game':
            file = input('file name - ')
            f = open(file, 'w')
            f.writelines("%s\n" % line for line in list_of_moves)
            f.close()
            continue
        if move == 'play game':
            changes = []
            file = input('file name - ')
            f = open(file, 'r')
            print(print_board())
            lines = [line.rstrip() for line in f]
            another_player_turn = 0
            start = input('press "d" for move forward.\npress "a" for move back.\npress enter to start playing.\n')
            aq = []
            for move_el in lines:
                changes.append([move_el])
                # print(move_el, another_player_turn)
                valid_move(move_el, another_player_turn)
                # print(dict_changes)
                # print(f'{list(dict_changes)} = {list(dict_changes.values())}')
                dict_field[list(dict_changes)[0]] = list(dict_changes.values())[0]
                dict_field[list(dict_changes)[1]] = list(dict_changes.values())[1]
                aq.append({list(dict_changes)[0]: list(dict_changes.items())[1][1]})
                aq.append({list(dict_changes)[1]: list(dict_changes.items())[0][1]})
                # print(dict_changes)
                changes[-1].append(list(dict_changes.items())[-1])
                changes[-1].append(list(dict_changes.items())[-2])
                another_player_turn += 1
            # print(aq)
            # print(list(aq[0].items())[0][1])
            for num in range(len(aq)):
                dict_field[list(aq[num].items())[0][0]] = list(aq[num].items())[0][1]
            another_player_turn = 0
            counter = 0
            while True:
                if start == 'd':
                    while start == 'd':
                        valid_move(changes[counter][0], another_player_turn)
                        print(changes)
                        # print(dict_changes)
                        dict_field[changes[counter][1][0]] = changes[counter][1][1]
                        dict_field[changes[counter][2][0]] = changes[counter][2][1]
                        print(counter)
                        counter += 1
                        another_player_turn += 1
                        print(print_board())
                        start = input()
                if start == 'a':
                    print(counter)
                    counter -= 1
                    while start == 'a':
                        dict_field[changes[counter][1][0]] = changes[counter][2][1]
                        dict_field[changes[counter][2][0]] = changes[counter][1][1]
                        counter -= 1
                        player_turn -= 1
                        print(print_board())
                        start = input()
                if start == '':
                    game(another_player_turn, dict_changes)
        if valid_move(move, player_turn):
            print(dict_changes)
            if check(player_turn):
                while check(player_turn):
                    dict_field[list(dict_changes.keys())[0]] = '.'
                    dict_field[list(dict_changes.keys())[1]] = dict_changes[list(dict_changes.keys())[1]]
                    if check(player_turn):
                        dict_field[list(dict_changes.keys())[0]] = dict_changes[list(dict_changes.keys())[1]]
                        dict_field[list(dict_changes.keys())[1]] = '.'
                        print('move is not valid, its check_mate!')
                        print(print_board())
                        move = (input('ход первого игрокa: ') if player_turn % 2 == 0 else input('ход второго игрока: '))
                        dict_changes.clear()
                        valid_move(move, player_turn)
                    else:
                        break
                dict_field[list(dict_changes.keys())[0]] = '.'
                dict_field[list(dict_changes.keys())[1]] = dict_changes[list(dict_changes.keys())[1]]
            else:
                print(dict_changes)
                dict_field[list(dict_changes)[0]] = '.'
                dict_field[list(dict_changes)[1]] = dict_changes[list(dict_changes)[1]]
                if check(player_turn):
                    while check(player_turn):
                        dict_field[list(dict_changes.keys())[0]] = '.'
                        dict_field[list(dict_changes.keys())[1]] = dict_changes[list(dict_changes.keys())[1]]
                        if check(player_turn):
                            dict_field[list(dict_changes.keys())[0]] = dict_changes[list(dict_changes.keys())[1]]
                            dict_field[list(dict_changes.keys())[1]] = '.'
                            print('move is not valid, its check_mate!')
                            print(print_board())
                            move = (input('ход первого игрока: ') if player_turn % 2 == 0 else input(
                                'ход второго игрока: '))
                            dict_changes.clear()
                            valid_move(move, player_turn)
                        else:
                            break
            list_of_moves.append(move)
        else:
            print('move is not valid, try again!')
            player_turn -= 1
        turns += 1
        player_turn += 1
        print(dict_changes)
        dict_changes.clear()
        print(print_board())
        print(f'|{turns // 2}__Pаунд__{turns // 2}|')


print(game(player_turn, dict_changes))