# From https://www.cs.rit.edu/~ncs/color/t_convert.html

import math
def HSVtoRGB(h, s, v):
    if( s == 0 ):
        # achromatic (grey)
        r = g = b = v
    else:
        h *= 6;  # sector 0 to 5
        i = math.floor( h )
        f = h - i    # factorial part of h
        p = v * ( 1 - s )
        q = v * ( 1 - s * f )
        t = v * ( 1 - s * ( 1 - f ) )
        if (i == 0):
            r = v
            g = t
            b = p
        elif (i == 1):
            r = q
            g = v
            b = p
        elif ( i == 2):
            r = p
            g = v
            b = t
        elif (i == 3):
            r = p
            g = q
            b = v
        elif (i == 4):
            r = t
            g = p
            b = v
        elif (i == 5):
            r = v
            g = p
            b = q

    return (r,g,b)


