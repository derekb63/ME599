#!/usr/bin/env python2

import numpy as np

height = 5
radius = 3

def cylinder_volume(height, radius):
    Volume = np.pi*radius**2*height
    return Volume

Volume = cylinder_volume(height, radius)

print Volume
