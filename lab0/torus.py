#!/usr/bin/env python2

import numpy as np

inner = 3
outer = 4

def torus_volume(major_radius, minor_raduis):
    # For this function the major radius is the distance from the center
    # to the middle of the ring and the minor radius is the distance from
    # the minor radius to the outer edge of the ring, or the radius of
    # the circle resutong from a cross section of the torus through the
    # center radii
    Volume = np.pi*minor_raduis**2*2*np.pi*major_radius
    return Volume

Volume = torus_volume(inner-(outer-inner), outer-inner)

print(Volume)
