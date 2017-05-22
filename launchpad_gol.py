# Game of Life on the Novation Launchpad

import launchpad_py as launchpad
from pygame import time


L_SIZE = 8

color = (0, 64, 64)


def display_grid(grid, lp):
    """
    display the grid on the launchpad
    :param grid: the grid to display
    :param lp: the launchpad object
    :return: void
    """
    for y in range(0, L_SIZE):
        for x in range(0, L_SIZE):
            if grid[y][x] > 0:
                lp.LedCtrlXY(x, y+1, color[0], color[1], color[2])
            else:
                lp.LedCtrlXY(x, y+1, 0, 0, 0)


def check_type(lp):
    """
    check the type of the launchpad
    :param lp: launchpad object
    :return: name of launchpad type
    """
    if lp.Check(0, "pro"):
        print("Launchpad Pro")
        return "Pro"

    elif lp.Check(0, "mk2"):
        print("Launchpad Mk2")
        return "Mk2"

    else:
        print("Launchpad Mk1/S/Mini")
        return "Mk1"


def init_lp():
    """
    initialize the launchpad
    :return: launchpad object
    """
    # create launchpad instance
    lp = launchpad.Launchpad()
    mode = check_type(lp)
    success = False
    # check for the correct launchpad
    if mode == "Pro":
        lp = launchpad.LaunchpadPro()
        if lp.Open(0, "pro"):
            success = True

    elif mode == "Mk2":
        lp = launchpad.LaunchpadMk2()
        if lp.Open(0, "mk2"):
            success = True

    else:
        if lp.Open():
            success = True

    if not success:
        exit(1)
    else:
        return lp


def check_neighbors(x, y, grid):
    """
    check the count of neighbors
    :param x: row of live cell
    :param y: col of live cell
    :param grid: grid at the time
    :return: number of neighbors
    """
    neighbors = 0
    c_y = [-1, -1, -1, 1, 1, 1, 0, 0]
    c_x = [-1, 1, 0, -1, 1, 0, -1, 1]
    for n in range(0, 8):
        if grid[(c_y[n]+y) % 8][(c_x[n]+x) % 8] > 0:
            neighbors += 1
    return neighbors


def life_cycle(grid):
    """
    function to to perform a life cycle
    :param grid: life grid
    :return: new grid
    """
    newg = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    for y in range(0, 8):
        for x in range(0, 8):
            n = check_neighbors(x, y, grid)
            if grid[y][x] > 0:  # if its alive
                if n == 2 or n == 3:
                    newg[y][x] = 1
            else:  # or if it is dead
                if n == 3:
                    newg[y][x] = 1

    return newg


def main():
    cont = 1
    lp = init_lp()
    grid = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0]]

    while cont:
        # lp.LedAllOn(0)
        display_grid(grid, lp)

        grid = life_cycle(grid)

        time.wait(100)

if __name__ == '__main__':
    main()
