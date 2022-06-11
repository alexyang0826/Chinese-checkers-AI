import numpy as np

NOT_VISITED = 10
VISITED = 20


def build_board():
    """
    initial board, center area = 0, player's home > 0
    :return: board
    """

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

    board[9][21] = 3
    board[10][20] = 3
    board[10][22] = 3
    board[11][19] = 3
    board[11][21] = 3
    board[11][23] = 3
    board[12][18] = 3
    board[12][20] = 3
    board[12][22] = 3
    board[12][24] = 3

    board[13][9] = 4
    board[13][11] = 4
    board[13][13] = 4
    board[13][15] = 4
    board[14][10] = 4
    board[14][12] = 4
    board[14][14] = 4
    board[15][11] = 4
    board[15][13] = 4
    board[16][12] = 4

    board[9][3] = 5
    board[10][2] = 5
    board[10][4] = 5
    board[11][19 - 18] = 5
    board[11][21 - 18] = 5
    board[11][23 - 18] = 5
    board[12][18 - 18] = 5
    board[12][20 - 18] = 5
    board[12][22 - 18] = 5
    board[12][24 - 18] = 5

    board[4][18 - 18] = 6
    board[4][20 - 18] = 6
    board[4][22 - 18] = 6
    board[4][24 - 18] = 6
    board[5][19 - 18] = 6
    board[5][21 - 18] = 6
    board[5][23 - 18] = 6
    board[6][20 - 18] = 6
    board[6][22 - 18] = 6
    board[7][21 - 18] = 6

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


def build_sets():
    """
    build player's home
    :return: player's home
    """

    player1_home = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
    player2_home = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
    player3_home = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]

    return player1_home, player2_home, player3_home


def build_dest_sets():
    """
    build player's destination
    :return: player's destination
    """
    player1_dest = [[16, 12], [15, 11], [15, 13], [14, 10], [14, 14], [14, 12], [13, 9], [13, 15], [13, 13], [13, 11]]
    player2_dest = [[4, 0], [4, 2], [5, 1], [4, 4], [6, 2], [5, 3], [4, 6], [7, 3], [6, 4], [5, 5]]
    player3_dest = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22]]

    return player1_dest, player2_dest, player3_dest


def build_invalid_sets(player1_home, player2_home, player3_home, player1_dest, player2_dest, player3_dest):
    """
    :return:invaild_sets of player
    """
    player1_invalid_sets = player2_home + player3_home + player2_dest + player3_dest
    player2_invalid_sets = player3_home + player1_dest + player3_dest + player1_home
    player3_invalid_sets = player1_dest + player2_dest + player1_home + player2_home

    return player1_invalid_sets, player2_invalid_sets, player3_invalid_sets


def assign_set(player_turn, player1_set, player2_set, player3_set):
    """
    :param player_turn: which player's turn
    :return: player's turn
    """
    player_set = player1_set

    if player_turn == 1:
        player_set = player1_set
    if player_turn == 2:
        player_set = player2_set
    if player_turn == 3:
        player_set = player3_set

    return player_set


def assign_dest_set(player_turn, player1_dest, player2_dest, player3_dest):
    """
    :param player_turn: which player's turn

    :return: player's destination
    """
    dest_set = player1_dest

    if player_turn == 1:
        dest_set = player1_dest
    if player_turn == 2:
        dest_set = player2_dest
    if player_turn == 3:
        dest_set = player3_dest

    return dest_set


def update_player_set(set_pieces, player_turn, player1_set, player2_set, player3_set):
    """
    :param set_pieces: current pieces
    :param player_turn: which player's turn
    :return: updated sets
    """
    if player_turn == 1:
        player1_set = set_pieces
    if player_turn == 2:
        player2_set = set_pieces
    if player_turn == 3:
        player3_set = set_pieces

    return player1_set, player2_set, player3_set


def legal_moves(board, player_pieces, invalid_homes_set):
    """
    find all legal_move
    :param board: game board
    :param player_pieces: current player's pieces
    :param invalid_homes_set: invalid sets
    :return: all legal_moves
    """

    valid_moves = []

    for piece in player_pieces:
        visited_board = np.full(board.shape, NOT_VISITED)
        valid_moves = check_moves(board, visited_board, piece, 0, piece, valid_moves)

    illgal_move = []  # moves that stop at others home

    for valid_move in valid_moves:

        end_move = valid_move[1]

        if end_move in invalid_homes_set:
            illgal_move.append(valid_move)

    new_valid_moves = []
    for move in valid_moves:
        if move not in illgal_move:
            new_valid_moves.append(move)

    return new_valid_moves


def check_moves(board, visited_board, start, depth, origin, valid_moves):
    """
    :param board: game board
    :param visited_board: the board that record the visted path.
    :param start: start pos
    :param depth: depth
    :param origin: initial start pos
    :param valid_moves: valid moves
    :return:
    """
    [x_v0, y_v0] = start
    visited_board[x_v0][y_v0] = VISITED

    neighbors_list = find_neighbors(start)

    for x_1, y_1 in neighbors_list:

        if depth == 0 and board[x_1][y_1] == 0:
            valid_moves.append([start, [x_1, y_1]])

        if depth == 0 and board[x_1][y_1] > 0:  # 跳過人
            x_v2, y_v2 = find_jump_between(start, x_1, y_1)
            if board[x_v2][y_v2] == 0:
                valid_moves.append([start, [x_v2, y_v2]])
                valid_moves = check_moves(board, visited_board, [x_v2, y_v2], depth + 1, origin, valid_moves)

        if depth > 0 and board[x_1][y_1] > 0:
            x_v2, y_v2 = find_jump_between(start, x_1, y_1)
            if board[x_v2][y_v2] == 0 and visited_board[x_v2][y_v2] == NOT_VISITED:  # 避免往回跳
                valid_moves.append([origin, [x_v2, y_v2]])
                valid_moves = check_moves(board, visited_board, [x_v2, y_v2], depth + 1, origin, valid_moves)

    return valid_moves


def find_neighbors(pos):  # 周圍6個點
    """
    find neighbors
    :param pos: current position
    :return: all neighbors
    """
    [x, y] = pos

    neighbors_list = []

    neighbor = [x, y + 2]
    if 0 <= neighbor[1] <= 24:
        neighbors_list.append([x, y + 2])

    neighbor = [x, y - 2]
    if 0 <= neighbor[1] <= 24:
        neighbors_list.append([x, y - 2])

    neighbor = [x + 1, y + 1]
    if 0 <= neighbor[0] <= 16 and 0 <= neighbor[1] <= 24:
        neighbors_list.append([x + 1, y + 1])

    neighbor = [x + 1, y - 1]
    if 0 <= neighbor[0] <= 16 and 0 <= neighbor[1] <= 24:
        neighbors_list.append([x + 1, y - 1])

    neighbor = [x - 1, y + 1]
    if 0 <= neighbor[0] <= 16 and 0 <= neighbor[1] <= 24:
        neighbors_list.append([x - 1, y + 1])

    neighbor = [x - 1, y - 1]
    if 0 <= neighbor[0] <= 16 and 0 <= neighbor[1] <= 24:
        neighbors_list.append([x - 1, y - 1])

    return neighbors_list


def find_jump_between(x_0, y_0, x_1, y_1):
    """
    :param x_0: start x pos
    :param y_0: start y pos
    :param x_1: end x pos
    :param y_1: end y pos
    :return:
    """
    x_v2 = x_1 + (x_1 - x_0)
    y_v2 = y_1 + (y_1 - y_0)

    if 0 <= x_v2 <= 16 and 0 <= y_v2 <= 24:
        return x_v2, y_v2
    else:
        return 0, 0


def do_move(board, best_move, pieces_set):
    """
    :param board: game board
    :param best_move: best move
    :param pieces_set: pieces_set
    :return: game board, new_pieces_set
    """
    [start_x, start_y] = best_move[0]
    [end_x, end_y] = best_move[1]

    piece = board[start_x][start_y]
    board[start_x][start_y] = 0
    board[end_x][end_y] = piece

    piece_to_remove = [[start_x, start_y]]
    new_pieces_set = [i for i in pieces_set + piece_to_remove if i not in pieces_set or i not in piece_to_remove]

    # set_pieces.remove([start_x, start_y])
    new_pieces_set.append([end_x, end_y])

    return board, new_pieces_set


def check_win(pieces, dest_set):
    """
    :param pieces: current pieces
    :param dest_set: destination set
    :return: whether game end or not.
    """
    game_end = True

    for piece in pieces:
        if piece not in dest_set:
            game_end = False
            break

    return game_end
