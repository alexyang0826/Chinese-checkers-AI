import numpy as np


# from strat_greedy import greedy
# from strat_alphabeta import alphabeta


def find_best_move(board, all_legal_moves, obj_set, player_turn, set_pieces, player1_set, player2_set, player3_set,
                   player4_set, player5_set, player6_set):
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
            score, best_move = alphabeta(board, depth, player_turn, player_turn, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, -1000, 1000)
        elif player_turn == 3:
            depth = 2
            score, best_move = alphabeta(board, depth, player_turn, player_turn, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, -1000, 1000)
        elif player_turn == 5:
            depth = 3
            score, best_move = alphabeta(board, depth, player_turn, player_turn, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, -1000, 1000)
        elif player_turn == 2:
            # depth = 1
            # score, best_move = minimax(board, depth, player_turn, player_turn, player1_set, player2_set,
            #                            player3_set, player4_set, player5_set, player6_set)
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 4:
            # depth = 2
            # score, best_move = minimax(board, depth, player_turn, player_turn, player1_set, player2_set,
            #                            player3_set, player4_set, player5_set, player6_set)
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 6:
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)

    except Exception:
        return

    return best_move


from board import *
import copy

player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = build_sets()
player1_obj, player2_obj, player3_obj, player4_obj, player5_obj, player6_obj = build_obj_sets()
player1_inv_homes, player2_inv_homes, player3_inv_homes, player4_inv_homes, player5_inv_homes, player6_inv_homes = \
    build_invalid_homes_sets(player1_set, player2_set, player3_set, player4_set, player5_set, player6_set, player1_obj,
                             player2_obj, player3_obj, player4_obj, player5_obj, player6_obj)


def alphabeta(board, depth, player, first_player, player1_set, player2_set, player3_set, player4_set, player5_set,
              player6_set, alpha, beta):
    board_copy = board[:][:]

    if depth == 0:
        board_score = calculate_board_score(first_player, player1_set, player2_set, player3_set, player4_set,
                                            player5_set, player6_set)
        return board_score, None

    set_pieces = assign_set(player, player1_set, player2_set, player3_set, player4_set, player5_set, player6_set)

    obj_set = assign_obj_set(player, player1_obj, player2_obj, player3_obj, player4_obj,
                             player5_obj, player6_obj)

    inv_homes_set = assign_invalid_homes_set(player, player1_inv_homes, player2_inv_homes, player3_inv_homes,
                                             player4_inv_homes, player5_inv_homes, player6_inv_homes)

    valid_moves = find_all_legal_moves(board_copy, set_pieces, obj_set, inv_homes_set)

    scores = []
    moves = []

    if player == first_player:

        for move in valid_moves:

            board_copy_again = copy.copy(board_copy)
            new_board, new_set_pieces = do_move(board_copy_again, move, set_pieces)

            player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                update_player_set(new_set_pieces, player, player1_set, player2_set, player3_set, player4_set,
                                  player5_set, player6_set)

            next_player = player + 1
            if next_player == 7:
                next_player = 1

            score, something = alphabeta(new_board, depth - 1, next_player, first_player, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, alpha, beta)

            scores.append(score)
            moves.append(move)
            # print('- player', player, 'depth', depth, '- move', move, 'score', score)
            # print('---- scores:', scores)
            # print('---- moves:', moves)

            alpha = max(score, alpha)
            if beta <= alpha:
                # print('--------------------- node skipped - alpha', alpha, '- beta', beta)
                break

        if len(scores) == 0:
            return
        max_score_index = scores.index(max(scores))
        best_move = moves[max_score_index]
        # print('- player', player, '- best move', best_move, '. score', max(scores), '. at index', max_score_index)
        return scores[max_score_index], best_move

    else:

        for move in valid_moves:

            # print('--- player', player, "set:", set_pieces)
            # print('- player', player, "- move:", move)

            board_copy_again = copy.copy(board_copy)
            new_board, new_set_pieces = do_move(board_copy_again, move, set_pieces)

            player1_set, player2_set, player3_set, player4_set, player5_set, player6_set = \
                update_player_set(new_set_pieces, player, player1_set, player2_set, player3_set, player4_set,
                                  player5_set, player6_set)

            next_player = player + 1
            if next_player == 7:
                next_player = 1

            score, something = alphabeta(new_board, depth - 1, next_player, first_player, player1_set, player2_set,
                                         player3_set, player4_set, player5_set, player6_set, alpha, beta)

            scores.append(score)
            moves.append(move)
            # print('- player', player, 'depth', depth, '- move', move, 'score', score)
            # print('---- scores:', scores)
            # print('---- moves:', moves)

            beta = min(score, beta)
            if beta <= alpha:
                # print('----------------------------- node skipped', alpha, '- beta', beta)
                break

        if len(scores) == 0:
            return
        min_score_index = scores.index(min(scores))
        worst_opponent_move = moves[min_score_index]
        # print('- player', player, '- worst opponent move', worst_opponent_move, '. score', min(scores), '. at index',
        #     min_score_index)

        return scores[min_score_index], worst_opponent_move


def calculate_board_score(player_turn, p1_pieces, p2_pieces, p3_pieces, p4_pieces, p5_pieces, p6_pieces):
    p1_avg_distance = find_avg_distance(p1_pieces, player1_obj, 16, 12)
    # print("-- avg distance p1", p1_avg_distance)
    p2_avg_distance = find_avg_distance(p2_pieces, player2_obj, 12, 0)
    # print("-- avg distance p2", p2_avg_distance)
    p3_avg_distance = find_avg_distance(p3_pieces, player3_obj, 4, 0)
    # print("-- avg distance p3", p3_avg_distance)
    p4_avg_distance = find_avg_distance(p4_pieces, player4_obj, 0, 12)
    # print("-- avg distance p4", p4_avg_distance)
    p5_avg_distance = find_avg_distance(p5_pieces, player5_obj, 4, 24)
    # print("-- avg distance p5", p5_avg_distance)
    p6_avg_distance = find_avg_distance(p6_pieces, player6_obj, 12, 24)
    # print("-- avg distance p6", p6_avg_distance)

    score = calculate_score(player_turn, p1_avg_distance, p2_avg_distance, p3_avg_distance, p4_avg_distance,
                            p5_avg_distance, p6_avg_distance)

    return score


def find_avg_distance(p_pieces, p_obj, p_default_x, p_default_y):
    total_distance = 0
    obj_x = p_default_x
    obj_y = p_default_y
    for obj_piece in p_obj:
        if obj_piece not in p_pieces:
            [obj_x, obj_y] = obj_piece
            break

    for piece in p_pieces:
        [x, y] = piece

        square_y = (y * 14.43) / 25
        square_obj_y = (obj_y * 14.43) / 25

        distance_diag = math.sqrt(((obj_x - x) ** 2) + ((square_obj_y - square_y) ** 2))

        total_distance = total_distance + distance_diag

    avg_distance = total_distance / 10

    return avg_distance


def calculate_score(player_turn, p1_avg_distance, p2_avg_distance, p3_avg_distance, p4_avg_distance, p5_avg_distance,
                    p6_avg_distance):
    score = 0

    if player_turn == 1:
        # print("-- loop player 1")
        pturn_avg_distance = p1_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 2:
        # print("-- loop player 2")
        pturn_avg_distance = p2_avg_distance
        score = ((p1_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 3:
        # print("-- loop player 3")
        pturn_avg_distance = p3_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 4:
        # print("-- loop player 4")
        pturn_avg_distance = p4_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 5:
        # print("-- loop player 5")
        pturn_avg_distance = p5_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance) +
                 (p6_avg_distance - pturn_avg_distance)) / 5
    elif player_turn == 6:
        # print("-- loop player 6")
        pturn_avg_distance = p6_avg_distance
        score = ((p2_avg_distance - pturn_avg_distance) +
                 (p3_avg_distance - pturn_avg_distance) +
                 (p4_avg_distance - pturn_avg_distance) +
                 (p5_avg_distance - pturn_avg_distance) +
                 (p1_avg_distance - pturn_avg_distance)) / 5

    return score


import math


def greedy(board, all_legal_moves, obj_set, player_turn):
    obj_available = []

    for pos in obj_set:
        [x, y] = pos
        if board[x][y] != player_turn:
            obj_available.append([x, y])

    max_distance_metric = 0
    move_index = 0
    best_move = 0

    for move in all_legal_moves:

        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]

        for obj in obj_available:

            [obj_x, obj_y] = obj

            # trasform y coord thinking about the board as a square, which it should be
            square_start_y = (start_y * 14.43) / 25
            square_end_y = (end_y * 14.43) / 25
            square_obj_y = (obj_y * 14.43) / 25

            start_diag = math.sqrt(((obj_x - start_x) ** 2) + ((square_obj_y - square_start_y) ** 2))
            end_diag = math.sqrt(((obj_x - end_x) ** 2) + ((square_obj_y - square_end_y) ** 2))

            distance_travel = start_diag - end_diag
            distance_metric = distance_travel + start_diag * 0.5

            if distance_metric > max_distance_metric:
                best_move = move_index
                max_distance_metric = distance_metric

        move_index = move_index + 1

    return all_legal_moves[best_move]
