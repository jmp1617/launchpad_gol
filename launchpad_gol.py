# Game of Life on the Novation Launchpad

import launchpad_py as launchpad
import random
from pygame import time


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
    pass


if __name__ == '__main__':
    main()
