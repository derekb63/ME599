#!/usr/bin/env/python

import math

def cylinder_volume(radius, height):
    if radius <= 0 or height <=0:
	return
    else:
        return math.pi*radius**2*height


def torus_volume(major_radius, minor_radius):
    if major_radius <= 0 or minor_radius <= 0:
        return
    else:
	return (math.pi*minor_radius**2)*(2*math.pi*major_radius)


