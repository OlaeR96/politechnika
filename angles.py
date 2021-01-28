# -*- coding: utf-8 -*-
import math


def deg2grad(deg):
    """
    deg2grad(90.00) --> 100.0
    """

    return deg * 10 / 9


def grad2deg(grad):
    """
    grad2deg(100.00) --> 90.0
    """

    return grad * 9 / 10


def grad2rad(grad):
    """
    grad2rad(100.0) --> 1.5707963267948968
    """

    return grad * (math.pi / 200)


def rad2grad(rad):
    """
    rad2grad(1.5707963267948968) --> 90.0
    """

    return rad * (200 / math.pi)


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    """
    decimal_deg(1.5707963267948968) --> 90.0
    """

    return decimal_deg * (math.pi / 180)


def rad2decimal_deg(rad):
    """
    rad2decimal_deg(1.5707963267948968) --> 90.0
    """

    return rad * (180 / math.pi)


# ======================== for 4

def decimal_deg2dms_deg(decimal_deg):
    """
    decimal_deg2dms_deg(1.0169722222222222) --> (1, 1, 1.1)
    """
    stopnie = int(decimal_deg)
    minuty = (decimal_deg - stopnie) * 60
    sekundy = (minuty - int(minuty)) * 60

    return stopnie, int(minuty), (round(sekundy, 2))


def dms_deg2decimal_deg(dms_deg):
    """
    dms_deg2decimal_deg(1, 1, 1.1) --> (1.0169722222222222)
    """
    stopien = dms_deg[0] + dms_deg[1] / 60 + dms_deg[2] / 3600

    return stopien

# ======================== for 5
