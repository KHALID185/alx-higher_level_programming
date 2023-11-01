#!/usr/bin/python3
"""solution possible for N board"""

import sys


def init_brd(num):
    """initialize board"""
    brd = []
    [brd.append([]) for h in range(num)]
    [line.append(' ') for h in range(num) for line in brd]
    return (brd)


def cp_brd(brd):
    """a copy of the board n*n"""
    if type(brd) is list:
        return list(map(cp_brd, brd))
    return (brd)


def sol_brd(brd):
    """solution possible for n*n board"""
    s = []
    for hg in range(len(brd)):
        for wt in range(len(brd)):
            if brd[hg][wt] == "Q":
                s.append([hg, wt])
                break
    return (s)


def out_brd(brd, line, coln):
    """solutions already see"""
    for cl in range(coln + 1, len(brd)):
        brd[line][cl] = "x"

    for cl in range(coln - 1, -1, -1):
        brd[line][cl] = "x"

    for ln in range(line + 1, len(brd)):
        brd[ln][coln] = "x"

    for ln in range(line - 1, -1, -1):
        brd[ln][coln] = "x"

    cl = coln + 1
    for ln in range(line + 1, len(brd)):
        if cl >= len(brd):
            break
        brd[ln][cl] = "x"
        cl += 1

    cl = coln - 1
    for ln in range(line - 1, -1, -1):
        if cl < 0:
            break
        brd[ln][cl]
        cl -= 1

    cl = coln + 1
    for ln in range(line - 1, -1, -1):
        if cl >= len(brd):
            break
        brd[ln][cl] = "x"
        cl += 1

    cl = coln - 1
    for ln in range(line + 1, len(brd)):
        if cl < 0:
            break
        brd[ln][cl] = "x"
        cl -= 1


def rec_sol(brd, line, qn, sol):
    """methode of recursion to solve the problem
    args:
        board
        line
        queen
        solution
    returns: the solutions possible
    """
    if qn == len(brd):
        sol.append(sol_brd(brd))
        return (sol)

    for cl in range(len(brd)):
        if brd[line][cl] == " ":
            garage_brd = cp_brd(brd)
            garage_brd[line][cl] = "Q"
            out_brd(garage_brd, line, cl)
            sol = rec_sol(garage_brd, line + 1, qn + 1, sol)

    return (sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = init_brd(int(sys.argv[1]))
    sol = rec_sol(brd, 0, 0, [])
    for sl in sol:
        print(sl)
