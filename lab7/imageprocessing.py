#! usr/bin/env python

# Derek Bean
# ME 599
# lab 7
# 2/28/2017

from grabber import Webcam
from PIL import Image, ImageChops
import os

# To save an image from grabber use the syntax
# <variable name> = Webcam()
# <variable name>.save_image(<filename>)

# Tasks of the lab
#     Calculate the average intensity of an image
#     Plot the average intestity over time
#     Write a code that returns the filtered average intensity
#     write a function daytime that returns True and False
#     write a function that grabs an image and calculates the most common
#         color in it. what is the color, how many pixels have this color
#     Write a function that detects mothion in the image stream that returns
#         the average pixel difference in a function called motion that
#         returns True or False if there is motion in the quad
#     Write a function called event that returns true if there's an event
#         happening in the quad

# https://docs.python.org/3/library/sched.html
# https://docs.python.org/2/library/os.html#os.listdir


class ImProcess:
    def __init__(self,image_file):
        self.image= Image.open(image_file)

    def show(self):
        return self.image.show()

    def avg_intensity(self):
        pixel_data = list(self.image.getdata())
        pixel_mean = [sum(x)/len(x) for x in pixel_data]
	return  sum(pixel_mean) / len(pixel_mean)


class GetImage:
    def __init__(self, number_of_images, folder='images'):
        for x in xrange(number_of_images):
            image = Webcam()
            try:
                image.save_image(folder+'/'+'image{0}'.format(x))
            except:
                os.makedirs(folder)
                image.save_image(folder+'/'+'image{0}'.format(x))

if __name__ == '__main__':
    test = ImProcess('image0')
    test.show()
    print test.avg_intensity()



