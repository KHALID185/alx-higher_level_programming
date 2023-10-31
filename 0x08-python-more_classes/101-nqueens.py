#!/usr/bin/python3
"""find all solution of N"""


def sol_valid_ornot(x, y, board_sz):
    """are the solution valid

    Args:
        x : coordonnes x
        y : coordonnes y
        board_sz : size

    Returns:
        booleens (true or false)
    """
    for items in range(board_sz):
        if board[items][y] == 1 or board[x][items] == 1:
            return False
        dx = x + items
        dy = y + items
        if dx < board_sz and dy < board_sz and board[dx][dy] == 1:
            return False
        dx = x - items
        dy = y - items
        if dx > 0 and dy > 0 and board[dx][dy] == 1:
            return False

        for items_2 in range(board_sz):
            if items + items_2 == x + y and board[items][items_2] == 1:
                return False
            if items - items_2 == x - y and board[items][items_2] == 1:
                return False
    return True

def n_solution_possible(face_q, board_sz, n_debut):
    """all the possible solution

    Args:
        face_q : queen face
        board_sz : size of board
        n_debut : start of the game

    Returns:
        all the solutions
    """
    if face_q == 0:
        return True
    if n_debut[0] >= board_sz or n_debut[1] >= board_sz:
        return False
    x = n_debut[0]
    y = n_debut[1]
    if board[x][y] == 0 and sol_valid_ornot(x, y, board_sz):
        board[x][y] = 1
        if n_solution_possible(face_q - 1, board_sz, (x + 1, 0)):
            return True
        board[x][y] = 0
    return n_solution_possible(face_q, board_sz, (x, y + 1))

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        m = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if m < 4:
        print("N must be at least 4")
        exit(1)

    n_debut = (0, 0)
    while n_debut[1] < m:
        solutions = []
        board = [[0 for items in range(m)] for items_2 in range(m)]
        if n_solution_possible(m, m, n_debut):
            for coord_x in range(m):
                for coord_y in range(m):
                    if board[coord_x][coord_y] == 1:
                        solutions.append([coord_x, coord_y])
            print(solutions)
            sy = solutions[0][1]
        else:
            sy = n_debut[1]
        n_debut = (0, sy + 1)
