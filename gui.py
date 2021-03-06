import pygame as pg

# -1 = NOT_VALID_SPACE
BACKGROUND = (0, 0, 0)
# 0 = EMPTY_CELL
EMPTY_CELL = (255, 255, 255)
# 1 = PLAYER 1
PLAYER1_GREEN = (124, 252, 0)
# 2 = PLAYER 2
PLAYER2_YELLOW = (243, 243, 14)
# 3 = PLAYER 3
PLAYER3_ORANGE = (255, 165, 0)
# 4 = PLAYER 4
PLAYER4_RED = (255, 0, 0)
# 5 = PLAYER 5
PLAYER5_PURPLE = (153, 50, 204)
# 6 = PLAYER 6
PLAYER6_BLUE = (0, 0, 255)
# HIGHLIGHT
HIGHLIGHT = (0, 255, 255)

# costants of the board
H_MARGIN_DISTANCE = 20
V_MARGIN_DISTANCE = 20
CIRCLE_RADIUS = 20
CIRCLE_DIAMETER = 2 * CIRCLE_RADIUS
H_SPACING = 8
V_SPACING = 1
WINDOW_WIDTH = (H_MARGIN_DISTANCE * 2) + (CIRCLE_DIAMETER * 13) + (H_SPACING * 12)
WINDOW_HEIGHT = (V_MARGIN_DISTANCE * 2) + (CIRCLE_DIAMETER * 17) + (V_SPACING * 16)


def init_board():
    pg.init()
    display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('Chinese Checkers AI')
    return display_surface


def draw_board(board, display_surface):
    display_surface.fill(BACKGROUND)
    # pg.draw.polygon(display_surface, (0, 0, 0), [(655, 552), (327, 3), (2, 552)])
    pg.draw.polygon(display_surface, (0, 0, 0),
                    [(112, 368), (222, 552), (431, 552), (543, 368), (431, 183), (222, 183)])

    y_coord = V_MARGIN_DISTANCE + CIRCLE_RADIUS

    destinations = [[2, 0], [0, 8], [2, 24], [14, 24], [16, 16], [14, 0]]

    for row in range(0, 17):

        x_coord_long = H_MARGIN_DISTANCE + CIRCLE_RADIUS
        x_coord_short = int(H_MARGIN_DISTANCE + CIRCLE_DIAMETER + (H_SPACING / 2))

        for circle_in_a_row in range(0, 13):
            if row % 2 == 0:

                board_value = board[row][circle_in_a_row * 2]
                color_circle(board_value, display_surface, x_coord_long, y_coord)

                x_coord_long = x_coord_long + CIRCLE_DIAMETER + H_SPACING

            elif row % 2 != 0 and circle_in_a_row != 12:

                board_value = board[row][circle_in_a_row * 2 + 1]
                color_circle(board_value, display_surface, x_coord_short, y_coord)

                x_coord_short = x_coord_short + CIRCLE_DIAMETER + H_SPACING

        y_coord = y_coord + CIRCLE_DIAMETER + V_SPACING


def color_circle(board_value, display_surface, x_coord, y_coord):
    if board_value == -1:
        pg.draw.circle(display_surface, BACKGROUND, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 0:
        pg.draw.circle(display_surface, EMPTY_CELL, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 1:
        pg.draw.circle(display_surface, PLAYER1_GREEN, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 2:
        pg.draw.circle(display_surface, PLAYER2_YELLOW, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 3:
        pg.draw.circle(display_surface, PLAYER3_ORANGE, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 4:
        pg.draw.circle(display_surface, PLAYER4_RED, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 5:
        pg.draw.circle(display_surface, PLAYER5_PURPLE, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 6:
        pg.draw.circle(display_surface, PLAYER6_BLUE, (x_coord, y_coord), CIRCLE_RADIUS, 0)

    pg.draw.polygon(display_surface, PLAYER1_GREEN, [(431, 183), (327, 3), (222, 183)], 5)
    pg.draw.polygon(display_surface, PLAYER5_PURPLE, [(431, 552), (327, 732), (222, 552)], 5)
    pg.draw.polygon(display_surface, PLAYER2_YELLOW, [(655, 552), (543, 368), (431, 552)], 5)
    pg.draw.polygon(display_surface, PLAYER6_BLUE, [(220, 183), (112, 368), (2, 183)], 5)
    pg.draw.polygon(display_surface, PLAYER3_ORANGE, [(222, 552), (112, 368), (2, 552)], 5)
    pg.draw.polygon(display_surface, PLAYER4_RED, [(655, 183), (543, 368), (435, 183)], 5)


def highlight_best_move(best_move, display_surface):
    [start_x, start_y] = best_move[0]
    [end_x, end_y] = best_move[1]

    circle_start_x, circle_start_y = find_circle_from(start_x, start_y)
    pg.draw.ellipse(display_surface, HIGHLIGHT, (circle_start_x - CIRCLE_RADIUS, circle_start_y - CIRCLE_RADIUS,
                                                 CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)

    circle_end_x, circle_end_y = find_circle_from(end_x, end_y)
    pg.draw.ellipse(display_surface, HIGHLIGHT, (circle_end_x - CIRCLE_RADIUS, circle_end_y - CIRCLE_RADIUS,
                                                 CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)


def find_circle_from(x, y):
    if x % 2 == 0:
        circle_x = int(H_MARGIN_DISTANCE + CIRCLE_RADIUS + (CIRCLE_DIAMETER + H_SPACING) * (y / 2))
    else:
        circle_x = int(H_MARGIN_DISTANCE + CIRCLE_DIAMETER + (H_SPACING / 2) + (CIRCLE_DIAMETER + H_SPACING) * ((y - 1)
                                                                                                                / 2))
    circle_y = V_MARGIN_DISTANCE + CIRCLE_RADIUS + (CIRCLE_DIAMETER + V_SPACING) * x

    return circle_x, circle_y
