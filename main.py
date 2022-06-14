# import numpy as np
import sys
from pygame.locals import *
import random
# from run1 import *
from board import *
from gui import *
import copy

# times
restart_time = 0
move_time = 0
# rounds to play
ROUND = 1000

NUM_OF_PLAYERS = 2

# depth for alphabeta search
p1_depth = 1
p2_depth = 1
p3_depth = 1
p4_depth = 1
p5_depth = 1
p6_depth = 1
# decide the max players
MAX_PLAYERS = [2]
# decide algorithm to use 0:alphabeta 1:greedy
ALGORITHM = [1,1,1,1,1,1]
# weight of start_dis for greedy
WEIGHT = [0.1,1,1,1,1,1]
def build_sets():
    player1_set = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]  # 1
    player2_set = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22],
                   [12, 24]]  # 2
    player3_set = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]  # 3
    player4_set = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]  # 4
    player5_set = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13],
                   [16, 12]]  # 5
    player6_set = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]  # 6

    return player1_set, player2_set, player3_set, player4_set, player5_set, player6_set


def build_dest_sets():
    player1_dest = [[16, 12], [15, 11], [15, 13], [14, 10], [14, 14], [14, 12], [13, 9], [13, 15], [13, 13],
                    [13, 11]]  # 5
    player2_dest = [[4, 0], [4, 2], [5, 1], [4, 4], [6, 2], [5, 3], [4, 6], [7, 3], [6, 4], [5, 5]]  # 6
    player3_dest = [[4, 24], [5, 23], [4, 22], [6, 22], [4, 20], [5, 21], [7, 21], [4, 18], [5, 19], [6, 20]]  # 4
    player4_dest = [[12, 0], [11, 1], [12, 2], [10, 2], [12, 4], [11, 3], [9, 3], [12, 6], [11, 5], [10, 4]]  # 3
    player5_dest = [[0, 12], [1, 13], [1, 11], [2, 14], [2, 10], [2, 12], [3, 15], [3, 9], [3, 11], [3, 13]]  # 1
    player6_dest = [[12, 24], [12, 22], [11, 23], [12, 20], [10, 22], [11, 21], [12, 18], [9, 21], [10, 20],
                    [11, 19]]  # 2

    return player1_dest, player2_dest, player3_dest, player4_dest, player5_dest, player6_dest


def build_invalid_sets(player1_set, player2_set, player3_set, player4_set, player5_set, player6_set, player1_dest,
                       player2_dest, player3_dest, player4_dest, player5_dest, player6_dest):
    player1_invalid = player2_set + player2_dest + player3_set + player3_dest
    player2_invalid = player1_set + player1_dest + player3_set + player3_dest
    player3_invalid = player1_set + player1_dest + player2_set + player2_dest
    player4_invalid = player1_set + player1_dest + player2_set + player2_dest
    player5_invalid = player2_set + player2_dest + player3_set + player3_dest
    player6_invalid = player1_set + player1_dest + player3_set + player3_dest

    return player1_invalid, player2_invalid, player3_invalid, player4_invalid, player5_invalid, player6_invalid


def main():
    # win counters
    p1_win = 0
    p2_win = 0
    p3_win = 0
    p4_win = 0
    p5_win = 0
    p6_win = 0

    # stuck counter
    stuck_counter = 0

    board = build_board()
    player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
    player1_dest, player2_dest, player3_dest, player4_dest, player5_dest, player6_dest = build_dest_sets()
    player1_invalid, player2_invalid, player3_invalid, player4_invalid, player5_invalid, player6_invalid = \
        build_invalid_sets(player1_set, player2_set, player3_set, player4_set,
                           player5_set, player6_set, player1_dest, player2_dest,
                           player3_dest, player4_dest, player5_dest, player6_dest)

    display_surface = init_board()

    # player decision
    player_turn = random.randint(1, NUM_OF_PLAYERS)

    # game start
    game_over = False
    first_turn = True
    first_round = True
    save_first_p = 100

    next_move = USEREVENT + 1
    restart_game = USEREVENT + 2

    event = pg.event.Event(next_move)
    pg.event.post(event)

    i_round = 0
    while i_round < ROUND:

        draw_board(board, display_surface)

        for event in pg.event.get():

            if event.type == QUIT:
                pg.quit()
                sys.exit()

            if event.type == restart_game:
                pg.time.wait(restart_time)
                i_round = i_round + 1

                board = build_board()
                player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
                player1_dest, player2_dest, player3_dest, player4_dest, player5_dest, player6_dest = build_dest_sets()
                player1_invalid, player2_invalid, player3_invalid, player4_invalid, player5_invalid, player6_invalid = \
                    build_invalid_sets(player1_set, player2_set, player3_set, player4_set, player5_set, player6_set,
                                       player1_dest,
                                       player2_dest, player3_dest, player4_dest, player5_dest, player6_dest)
                display_surface = init_board()

                # player decision
                player_turn = random.randint(1, NUM_OF_PLAYERS)

                draw_board(board, display_surface)
                pg.display.update()

                # game restart
                game_over = False
                first_turn = True
                first_round = True
                save_first_p = 100

                event = pg.event.Event(next_move)
                pg.event.post(event)

                break

            if event.type == next_move and not game_over:

                pg.time.wait(move_time)

                # change player turn
                player_turn = player_turn + 1
                if player_turn == NUM_OF_PLAYERS + 1:
                    player_turn = 1

                # randomize first move
                if player_turn == save_first_p:
                    first_round = False
                if first_turn:
                    save_first_p = player_turn
                    first_turn = False

                # print("Player", player_turn)

                # consider the pieces of the player of this turn
                pieces_set = assign_set(player_turn, player1_set, player2_set, player3_set, player4_set,
                                        player5_set, player6_set)

                # identify homes of the player of this turn
                invalid_set = assign_invalid_set(player_turn, player1_invalid,
                                                 player2_invalid, player3_invalid,
                                                 player4_invalid, player5_invalid,
                                                 player6_invalid)

                # assign objective set of positions
                dest_set = assign_dest_set(player_turn, player1_dest, player2_dest, player3_dest, player4_dest,
                                           player5_dest, player6_dest)

                # find all legal moves given a piece set of a player
                all_legal_moves = find_all_legal_moves(board, pieces_set, dest_set, invalid_set)

                # choose the best move
                if first_round:
                    best_move_index = random.randint(0, len(all_legal_moves) - 1)
                    best_move = all_legal_moves[best_move_index]
                else:
                    best_move = find_best_move(board, all_legal_moves, dest_set, player_turn, pieces_set,
                                               player1_set, player2_set, player3_set, player4_set, player5_set,
                                               player6_set)
                # print("player:", player_turn, "best move:", best_move)

                if best_move is None:
                    game_over = True
                    stuck_counter = stuck_counter + 1
                    print('Game stuck counter:', stuck_counter)
                    print('[]------------------[]')

                    event = pg.event.Event(restart_game)
                    pg.event.post(event)

                    break

                # highlight the move chosen
                highlight_best_move(best_move, display_surface)
                pg.display.update()

                # do the best move
                board, pieces_set = do_move(board, best_move, pieces_set)

                # update set
                player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                    update_player_set(pieces_set, player_turn, player1_set, player2_set, player3_set, player4_set,
                                      player5_set, player6_set)

                # update the board

                # check if the player has won
                game_over = check_win(pieces_set, dest_set)

                if game_over:

                    if player_turn == 1:
                        p1_win = p1_win + 1
                    if player_turn == 2:
                        p2_win = p2_win + 1
                    if player_turn == 3:
                        p3_win = p3_win + 1
                    if player_turn == 4:
                        p4_win = p4_win + 1
                    if player_turn == 5:
                        p5_win = p5_win + 1
                    if player_turn == 6:
                        p6_win = p6_win + 1

                    print('Player 1 wins:', p1_win)
                    print('Player 2 wins:', p2_win)
                    print('Player 3 wins:', p3_win)
                    print('Player 4 wins:', p4_win)
                    print('Player 5 wins:', p5_win)
                    print('Player 6 wins:', p6_win)
                    print('[]------------------[]')

                    event = pg.event.Event(restart_game)
                    pg.event.post(event)

                else:

                    event = pg.event.Event(next_move)
                    pg.event.post(event)

                    # pg.display.update()


def find_best_move(board, all_legal_moves, dest_set, player_turn, pieces_set, player1_set, player2_set, player3_set,
                   player4_set, player5_set, player6_set):
    dest_left = []
    for i in dest_set + pieces_set:
        if i not in dest_set or i not in pieces_set:
            dest_left.append(i)

    if len(dest_left) == 2:
        for move in all_legal_moves:
            start_move = move[0]
            end_move = move[1]
            if start_move == dest_left[1] and end_move == dest_left[0]:
                return move
    try:

        if player_turn == 1:
            if ALGORITHM[0] == 0:
                score, best_move = alphabeta(board, p1_depth, player_turn, player_turn, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, -10000, 10000)
            if ALGORITHM[0] == 1:
                best_move = greedy(board, all_legal_moves, dest_set, player_turn, WEIGHT[0])
        elif player_turn == 2:
            if ALGORITHM[1] == 0:
                score, best_move = alphabeta(board, p2_depth, player_turn, player_turn, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, -10000, 10000)
            if ALGORITHM[1] == 1:
                best_move = greedy(board, all_legal_moves, dest_set, player_turn, WEIGHT[1])
        elif player_turn == 3:
            if ALGORITHM[2] == 0:
                score, best_move = alphabeta(board, p3_depth, player_turn, player_turn, player1_set, player2_set,
                                             player3_set, player4_set, player5_set, player6_set, -10000, 10000)
            if ALGORITHM[2] == 1:
                best_move = greedy(board, all_legal_moves, dest_set, player_turn, WEIGHT[2])
        elif player_turn == 4:
            if ALGORITHM[3] == 0:
                score, best_move = alphabeta(board, p4_depth, player_turn, player_turn, player1_set, player2_set,
                                             player3_set, player4_set, player5_set, player6_set, -10000, 10000)
            if ALGORITHM[3] == 1:
                best_move = greedy(board, all_legal_moves, dest_set, player_turn, WEIGHT[3])
        elif player_turn == 5:
            if ALGORITHM[4] == 0:
                score, best_move = alphabeta(board, p5_depth, player_turn, player_turn, player1_set, player2_set,
                                             player3_set, player4_set, player5_set, player6_set, -10000, 10000)
            if ALGORITHM[4] == 1:
                best_move = greedy(board, all_legal_moves, dest_set, player_turn, WEIGHT[4])
        elif player_turn == 6:
            if ALGORITHM[5] == 0:
                score, best_move = alphabeta(board, p6_depth, player_turn, player_turn, player1_set, player2_set,
                                             player3_set, player4_set, player5_set, player6_set, -10000, 10000)
            if ALGORITHM[5] == 1:
                best_move = greedy(board, all_legal_moves, dest_set, player_turn, WEIGHT[5])
    except Exception:
        return

    return best_move


player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
player1_dest, player2_dest, player3_dest, player4_dest, player5_dest, player6_dest = build_dest_sets()
player1_inv, player2_inv, player3_inv, player4_inv, player5_inv, player6_inv = build_invalid_sets(player1_set,
                                                                                                  player2_set,
                                                                                                  player3_set,
                                                                                                  player4_set,
                                                                                                  player5_set,
                                                                                                  player6_set,
                                                                                                  player1_dest,
                                                                                                  player2_dest,
                                                                                                  player3_dest,
                                                                                                  player4_dest,
                                                                                                  player5_dest,
                                                                                                  player6_dest)


def alphabeta(board, depth, player, first_player, player1_set, player2_set, player3_set, player4_set, player5_set,
              player6_set, alpha, beta):
    board_copy = board[:][:]

    if depth == 0:
        board_score = calculate_board_score(first_player, player1_set, player2_set, player3_set, player4_set,
                                            player5_set, player6_set)
        return board_score, None

    pieces_set = assign_set(player, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set)

    dest_set = assign_dest_set(player, player1_dest, player2_dest, player3_dest, player4_dest,
                               player5_dest, player6_dest)

    invalid_set = assign_invalid_set(player, player1_inv, player2_inv, player3_inv,
                                     player4_inv, player5_inv, player6_inv)

    valid_moves = find_all_legal_moves(board_copy, pieces_set, dest_set, invalid_set)

    scores = []
    moves = []

    if player not in MAX_PLAYERS:

        for move in valid_moves:

            board_copy_again = copy.copy(board_copy)
            new_board, new_set_pieces = do_move(board_copy_again, move, pieces_set)

            player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                update_player_set(new_set_pieces, player, player1_set, player2_set, player3_set, player4_set,
                                  player5_set, player6_set)

            next_player = player + 1
            if next_player == NUM_OF_PLAYERS + 1:
                next_player = 1

            score, something = alphabeta(new_board, depth - 1, next_player, first_player, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, alpha, beta)

            scores.append(score)
            moves.append(move)

            alpha = max(score, alpha)
            if beta <= alpha:
                break

        if len(scores) == 0:
            return
        max_score_index = scores.index(max(scores))
        best_move = moves[max_score_index]
        # print('- player', player, '- best move', best_move, '. score', max(scores), '. at index', max_score_index)
        return scores[max_score_index], best_move

    else:

        for move in valid_moves:

            board_copy_again = copy.copy(board_copy)
            new_board, new_set_pieces = do_move(board_copy_again, move, pieces_set)

            player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                update_player_set(new_set_pieces, player, player1_set, player2_set, player3_set, player4_set,
                                  player5_set, player6_set)

            next_player = player + 1
            if next_player == NUM_OF_PLAYERS + 1:
                next_player = 1

            score, something = alphabeta(new_board, depth - 1, next_player, first_player, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, alpha, beta)

            scores.append(score)
            moves.append(move)

            beta = min(score, beta)
            if beta <= alpha:
                break

        if len(scores) == 0:
            return
        min_score_index = scores.index(max(scores))
        worst_opponent_move = moves[min_score_index]

    return scores[min_score_index], worst_opponent_move


def calculate_board_score(player_turn, p1_pieces, p2_pieces, p3_pieces, p4_pieces, p5_pieces, p6_pieces):
    p1_avg_distance = find_avg_distance(p1_pieces, player1_dest, 16, 12)
    p2_avg_distance = find_avg_distance(p2_pieces, player2_dest, 4, 0)
    p3_avg_distance = find_avg_distance(p3_pieces, player3_dest, 4, 24)
    p4_avg_distance = find_avg_distance(p4_pieces, player4_dest, 12, 0)
    p5_avg_distance = find_avg_distance(p5_pieces, player5_dest, 0, 12)
    p6_avg_distance = find_avg_distance(p6_pieces, player6_dest, 12, 24)
    score = 0
    if player_turn == 1:
        piece_in_dest = [i for i in p1_pieces if i in player1_dest]
        pturn_avg_distance = p1_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance)
                 ) + len(piece_in_dest) * 100
    elif player_turn == 2:
        piece_in_dest = [i for i in p2_pieces if i in player2_dest]
        pturn_avg_distance = p2_avg_distance
        score = ((p1_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance)
                 ) + len(piece_in_dest) * 100
    elif player_turn == 3:
        piece_in_dest = [i for i in p3_pieces if i in player3_dest]
        pturn_avg_distance = p3_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance)
                 ) + len(piece_in_dest) * 100
    elif player_turn == 4:
        piece_in_dest = [i for i in p4_pieces if i in player4_dest]
        pturn_avg_distance = p4_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) + len(piece_in_dest) * 100
    elif player_turn == 5:
        piece_in_dest = [i for i in p5_pieces if i in player5_dest]
        pturn_avg_distance = p5_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) + len(piece_in_dest) * 100
    elif player_turn == 6:
        piece_in_dest = [i for i in p6_pieces if i in player6_dest]
        pturn_avg_distance = p6_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance)) + len(piece_in_dest) * 100

    return score


def find_avg_distance(p_pieces, p_dest, p_default_x, p_default_y):
    total_distance = 0
    dest_x = p_default_x
    dest_y = p_default_y
    for dest_piece in p_dest:
        if dest_piece not in p_pieces:
            [dest_x, dest_y] = dest_piece
            break

    for piece in p_pieces:
        [x, y] = piece

        transfered_y = y / math.sqrt(2)
        transferd_dest_y = dest_y / math.sqrt(2)

        distance_diag = math.sqrt(((dest_x - x) ** 2) + ((transferd_dest_y - transfered_y) ** 2))

        total_distance = total_distance + distance_diag

    avg_distance = total_distance / 10

    return avg_distance


def greedy(board, all_legal_moves, dest_set, player_turn, weight):
    dest_available = []

    for pos in dest_set:
        [x, y] = pos
        if board[x][y] != player_turn:
            dest_available.append([x, y])

    max_score = float('-inf')
    move_index = 0
    best_move = 0

    for move in all_legal_moves:

        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]


        for dest in dest_available:
            [dest_x, dest_y] = dest

            transfered_x = start_y / math.sqrt(2)
            transfered_y = end_y / math.sqrt(2)
            transfered_dest_y = dest_y / math.sqrt(2)

            start_diag = math.sqrt(((dest_x - start_x) ** 2) + ((transfered_dest_y - transfered_x) ** 2))
            end_diag = math.sqrt(((dest_x - end_x) ** 2) + ((transfered_dest_y - transfered_y) ** 2))


            distance_travel = start_diag - end_diag
            evaluate_score = distance_travel + start_diag * weight


            if evaluate_score > max_score:
                best_move = move_index
                max_score = evaluate_score

        move_index += 1

    return all_legal_moves[best_move]

def calculate_greedy(p_pieces, p_dest, p_default_x, p_default_y):
    total_distance = 0
    dest_x = p_default_x
    dest_y = p_default_y
    for dest_piece in p_dest:
        if dest_piece not in p_pieces:
            [dest_x, dest_y] = dest_piece
            break

    for piece in p_pieces:
        [x, y] = piece

        transfered_y = y / math.sqrt(2)
        transferd_dest_y = dest_y / math.sqrt(2)

        distance_diag = math.sqrt(((dest_x - x) ** 2) + ((transferd_dest_y - transfered_y) ** 2))

        total_distance = total_distance + distance_diag

    avg_distance = total_distance
    return avg_distance
if __name__ == '__main__':
    main()
