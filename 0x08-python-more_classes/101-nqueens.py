#!/usr/bin/python3
"""solves N queen problem """


from sys import argv

if __name__ == "__main__":
    l_n_q = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    nrd = int(argv[1])
    if nrd < 4:
        print("N must be at least 4")
        exit(1)

    for items in range(nrd):
        l_n_q.append([items, None])

    def nrd_deja_existé(coord_y):
        """check if the nord already exist or not"""
        for items in range(nrd):
            if coord_y == l_n_q[items][1]:
                return True
        return False

    def ref_sol(coord_x, coord_y):
        """reject the solution if it is already exist"""
        if (nrd_deja_existé(coord_y)):
            return False
        items = 0
        while(items < coord_x):
            if abs(l_n_q[items][1] - coord_y) == abs(items - coord_x):
                return False
            items += 1
        return True

    def all_reset(coord_x):
        """if the failaire exist clear all"""
        for items_1 in range(coord_x, nrd):
            l_n_q[items_1][1] = None

    def nqueens(coord_x):
        """find the solution with backtraking method"""
        for items_y in range(nrd):
            all_reset(coord_x)
            if ref_sol(coord_x, items_y):
                l_n_q[coord_x][1] = items_y
                if (coord_x == nrd - 1):
                    print(l_n_q)
                else:
                    nqueens(coord_x + 1)
# debut de recursive is 0
    nqueens(0)
