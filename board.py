import numpy as np
import math
from main import NUM_OF_PLAYERS

VISITED = 20
NOT_VISITED = 15

enable1 = False
enable2 = False
enable3 = False
enable4 = False
enable5 = False
enable6 = False
player_num = NUM_OF_PLAYERS
if player_num > 0:
    enable1 = True
    player_num -= 1
    if player_num > 0:
        enable2 = True
        player_num -= 1
        if player_num > 0:
            enable3 = True
            player_num -= 1
            if player_num > 0:
                enable4 = True
                player_num -= 1
                if player_num > 0:
                    enable5 = True
                    player_num -= 1
                    if player_num > 0:
                        enable6 = True
                        player_num -= 1


def build_board():
    board = np.zeros((17, 25))

    board[:][:] = -1

    if (enable1 == True):
        e1 = 1
    else:
        e1 = 0
    board[0][12] = e1
    board[1][11] = e1
    board[1][13] = e1
    board[2][10] = e1
    board[2][12] = e1
    board[2][14] = e1
    board[3][9] = e1
    board[3][11] = e1
    board[3][13] = e1
    board[3][15] = e1

    if (enable2 == True):
        e2 = 2
    else:
        e2 = 0
    board[9][21] = e2
    board[10][20] = e2
    board[10][22] = e2
    board[11][19] = e2
    board[11][21] = e2
    board[11][23] = e2
    board[12][18] = e2
    board[12][20] = e2
    board[12][22] = e2
    board[12][24] = e2

    if (enable3 == True):
        e3 = 3
    else:
        e3 = 0
    board[9][3] = e3
    board[10][2] = e3
    board[10][4] = e3
    board[11][1] = e3
    board[11][3] = e3
    board[11][5] = e3
    board[12][0] = e3
    board[12][2] = e3
    board[12][4] = e3
    board[12][6] = e3

    if (enable4 == True):
        e4 = 4
    else:
        e4 = 0
    board[4][18] = e4
    board[4][20] = e4
    board[4][22] = e4
    board[4][24] = e4
    board[5][19] = e4
    board[5][21] = e4
    board[5][23] = e4
    board[6][20] = e4
    board[6][22] = e4
    board[7][21] = e4

    if (enable5 == True):
        e5 = 5
    else:
        e5 = 0
    board[13][9] = e5
    board[13][11] = e5
    board[13][13] = e5
    board[13][15] = e5
    board[14][10] = e5
    board[14][12] = e5
    board[14][14] = e5
    board[15][11] = e5
    board[15][13] = e5
    board[16][12] = e5

    if (enable6 == True):
        e6 = 6
    else:
        e6 = 0
    board[4][0] = e6
    board[4][2] = e6
    board[4][4] = e6
    board[4][6] = e6
    board[5][1] = e6
    board[5][3] = e6
    board[5][5] = e6
    board[6][2] = e6
    board[6][4] = e6
    board[7][3] = e6

    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0

    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0

    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0

    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0

    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0

    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

    board[12][8] = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


def assign_set(player_turn, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set):
    set_player = player1_set

    if player_turn == 1:
        set_player = player1_set
    if player_turn == 2:
        set_player = player2_set
    if player_turn == 3:
        set_player = player3_set
    if player_turn == 4:
        set_player = player4_set
    if player_turn == 5:
        set_player = player5_set
    if player_turn == 6:
        set_player = player6_set

    return set_player


def assign_dest_set(player_turn, player1_dest, player2_dest, player3_dest, player4_dest, player5_dest, player6_dest):
    dest_set = player1_dest

    if player_turn == 1:
        dest_set = player1_dest
    if player_turn == 2:
        dest_set = player2_dest
    if player_turn == 3:
        dest_set = player3_dest
    if player_turn == 4:
        dest_set = player4_dest
    if player_turn == 5:
        dest_set = player5_dest
    if player_turn == 6:
        dest_set = player6_dest

    return dest_set


def assign_invalid_set(player_turn, player1_invalid_set, player2_invalid_set, player3_invalid_set,
                       player4_invalid_set, player5_invalid_set, player6_invalid_set):
    invalid_set = player1_invalid_set

    if player_turn == 1:
        invalid_set = player1_invalid_set
    if player_turn == 2:
        invalid_set = player2_invalid_set
    if player_turn == 3:
        invalid_set = player3_invalid_set
    if player_turn == 4:
        invalid_set = player4_invalid_set
    if player_turn == 5:
        invalid_set = player5_invalid_set
    if player_turn == 6:
        invalid_set = player6_invalid_set

    return invalid_set


def update_player_set(pieces_set, player_turn, player1_set, player2_set, player3_set, player4_set, player5_set,
                      player6_set):
    if player_turn == 1:
        player1_set = pieces_set
    if player_turn == 2:
        player2_set = pieces_set
    if player_turn == 3:
        player3_set = pieces_set
    if player_turn == 4:
        player4_set = pieces_set
    if player_turn == 5:
        player5_set = pieces_set
    if player_turn == 6:
        player6_set = pieces_set

    return player1_set, player2_set, player3_set, player4_set, player5_set, player6_set


def find_all_legal_moves(board, pieces_set, dest_set, invalid_set):
    valid_moves = []

    for piece in pieces_set:
        color_board = np.full(board.shape, NOT_VISITED)
        valid_moves = check_moves(board, color_board, piece, 0, piece, valid_moves)

    moves_to_remove = []

    for valid_move in valid_moves:
        start_move = valid_move[0]
        end_move = valid_move[1]

        if start_move in dest_set:
            transfered_start_y = start_move[1] / math.sqrt(2)
            transfered_end_y = end_move[1] / math.sqrt(2)
            central_pos = 12 / math.sqrt(2)

            start_diag = math.sqrt(((8 - start_move[0]) ** 2) + ((central_pos - transfered_start_y) ** 2))
            end_diag = math.sqrt(((8 - end_move[0]) ** 2) + ((central_pos - transfered_end_y) ** 2))

            if start_diag > end_diag:
                moves_to_remove.append(valid_move)

    new_valid_moves = [i for i in valid_moves + moves_to_remove if i not in valid_moves or i not in moves_to_remove]
    moves_to_remove.clear()

    for valid_move in new_valid_moves:

        end_move = valid_move[1]

        if end_move in invalid_set:
            moves_to_remove.append(valid_move)

    valid_moves = [i for i in new_valid_moves + moves_to_remove if i not in valid_moves or i not in moves_to_remove]

    return valid_moves


def check_moves(board, color_board, start, depth, origin, v_moves):
    [x_v0, y_v0] = start
    color_board[x_v0][y_v0] = VISITED

    neighbors_list = find_neighbors_from(start)

    for x_v1, y_v1 in neighbors_list:

        if depth == 0 and board[x_v1][y_v1] == 0:
            v_moves.append([start, [x_v1, y_v1]])
            # print("nodo origine:", origin, "- profondita:", depth, "- end:", x_v1, y_v1)

        if depth == 0 and board[x_v1][y_v1] > 0:
            x_v2, y_v2 = find_jump_between(start, x_v1, y_v1)
            if board[x_v2][y_v2] == 0:
                v_moves.append([start, [x_v2, y_v2]])
                # print("nodo origine:", origin, "- profondita:", depth, "- start:", start, "- destinazione:", x_v2, y_v2)
                v_moves = check_moves(board, color_board, [x_v2, y_v2], depth + 1, origin, v_moves)

        if depth > 0 and board[x_v1][y_v1] > 0:
            x_v2, y_v2 = find_jump_between(start, x_v1, y_v1)
            if board[x_v2][y_v2] == 0 and color_board[x_v2][y_v2] == NOT_VISITED:
                v_moves.append([origin, [x_v2, y_v2]])
                # print("nodo origine:", origin, "- profondita:", depth, "- start:", start, "- destinazione:", x_v2,
                #       y_v2)
                v_moves = check_moves(board, color_board, [x_v2, y_v2], depth + 1, origin, v_moves)

    return v_moves


def find_neighbors_from(node):
    [x, y] = node

    neighbors_list = []

    nb = [x, y + 2]
    if 0 <= nb[1] <= 24:
        neighbors_list.append([x, y + 2])

    nb = [x, y - 2]
    if 0 <= nb[1] <= 24:
        neighbors_list.append([x, y - 2])

    nb = [x + 1, y + 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x + 1, y + 1])

    nb = [x + 1, y - 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x + 1, y - 1])

    nb = [x - 1, y + 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x - 1, y + 1])

    nb = [x - 1, y - 1]
    if 0 <= nb[0] <= 16 and 0 <= nb[1] <= 24:
        neighbors_list.append([x - 1, y - 1])

    return neighbors_list


def find_jump_between(start, x_v1, y_v1):
    [start_x, start_y] = start

    x_v2 = x_v1 + (x_v1 - start_x)
    y_v2 = y_v1 + (y_v1 - start_y)

    if 0 <= x_v2 <= 16 and 0 <= y_v2 <= 24:
        return x_v2, y_v2
    else:
        return 0, 0


def do_move(board, best_move, pieces_set):
    [start_x, start_y] = best_move[0]
    [end_x, end_y] = best_move[1]

    piece = board[start_x][start_y]
    board[start_x][start_y] = 0
    board[end_x][end_y] = piece

    piece_to_remove = [[start_x, start_y]]
    new_set_pieces = [i for i in pieces_set + piece_to_remove if i not in pieces_set or i not in piece_to_remove]

    new_set_pieces.append([end_x, end_y])

    return board, new_set_pieces


def check_win(pieces_set, dest_set):
    game_end = True

    for piece in pieces_set:
        if piece not in dest_set:
            game_end = False

    return game_end
