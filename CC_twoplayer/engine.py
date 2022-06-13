import numpy as np
from strat_greedy import greedy
from strat_alphabeta import alphabeta


def build_board():

    board = np.zeros((17, 25))

    board[:][:] = -1

    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9] = 1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

    board[4][18] = 2
    board[4][20] = 2
    board[4][22] = 2
    board[4][24] = 2
    board[5][19] = 2
    board[5][21] = 2
    board[5][23] = 2
    board[6][20] = 2
    board[6][22] = 2
    board[7][21] = 2

    board[9][21] = 0
    board[10][20] = 0
    board[10][22] = 0
    board[11][19] = 0
    board[11][21] = 0
    board[11][23] = 0
    board[12][18] = 0
    board[12][20] = 0
    board[12][22] = 0
    board[12][24] = 0

    board[13][9] = 0
    board[13][11] = 0
    board[13][13] = 0
    board[13][15] = 0
    board[14][10] = 0
    board[14][12] = 0
    board[14][14] = 0
    board[15][11] = 0
    board[15][13] = 0
    board[16][12] = 0

    board[9][21 - 18] = 0
    board[10][20 - 18] = 0
    board[10][22 - 18] = 0
    board[11][19 - 18] = 0
    board[11][21 - 18] = 0
    board[11][23 - 18] = 0
    board[12][18 - 18] = 0
    board[12][20 - 18] = 0
    board[12][22 - 18] = 0
    board[12][24 - 18] = 0

    board[4][18 - 18] = 0
    board[4][20 - 18] = 0
    board[4][22 - 18] = 0
    board[4][24 - 18] = 0
    board[5][19 - 18] = 0
    board[5][21 - 18] = 0
    board[5][23 - 18] = 0
    board[6][20 - 18] = 0
    board[6][22 - 18] = 0
    board[7][21 - 18] = 0

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


def build_invalid_set():

    player1_i_set = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14]]
    player2_i_set = [[9, 3], [10, 2], [10, 4], [11, 3], [11, 5], [12, 4], [12, 6]]

    return player1_i_set, player2_i_set

def assign_invalid_set(player_turn, player1_i_set, player2_i_set):

    invalid_set = player1_i_set

    if player_turn == 1:
        invalid_set = player1_i_set
    if player_turn == 2:
        invalid_set = player2_i_set

    return invalid_set


def find_best_move(board, all_legal_moves, obj_set, player_turn, set_pieces, player1_set, player2_set):

    obj_left = [i for i in obj_set + set_pieces if i not in obj_set or i not in set_pieces]
    if len(obj_left) == 2:
        for move in all_legal_moves:
            start_move = move[0]
            end_move = move[1]
            if start_move == obj_left[1] and end_move == obj_left[0]:
                return move
    try:

        if player_turn == 1:
            depth = 1
            score, best_move = alphabeta(board, depth, player_turn, player_turn, player1_set, player2_set, -1000, 1000)

        elif player_turn == 2:
            # depth = 1
            # score, best_move = minimax(board, depth, player_turn, player_turn, player1_set, player2_set,
            #                            player3_set, player4_set, player5_set, player6_set)
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)

    except Exception:
        return

    return best_move


def check_win(set_pieces, obj_set):

    game_end = True

    for piece in set_pieces:
        if piece not in obj_set:
            game_end = False

    return game_end