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
    for row in range(0, L_SIZE):
        for col in range(0, L_SIZE):
            if grid[row][col] > 0:
                lp.LedCtrlXY(col, row+1, color[0], color[1], color[2])
            else:
                lp.LedCtrlXY(col, row+1, 0, 0, 0)


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


def main():
    lp = init_lp()
    grid = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    display_grid(grid, lp)

    time.wait(1000)

    lp.LedAllOn(0)

if __name__ == '__main__':
    main()
