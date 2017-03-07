#! usr/bin/env python

# Derek Bean
# ME 599
# lab 7
# 2/28/2017

from grabber import Webcam
from PIL import Image, ImageChops
import os
import time
import matplotlib.pyplot as plt
from itertools import groupby
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
    def __init__(self):
        self.image = Webcam()
        self.data = self.image.grab_image_data()

    def show(self):
        return self.image.grab_image()

    def avg_intensity(self):
        pixel_data = list(self.data)
        pixel_mean = [sum(x)/len(x) for x in pixel_data]
        return sum(pixel_mean) / len(pixel_mean)

    def colors(self):
        return set(self.data)

    def most_common_color(self):
        pixel_count = []
        for color, group_of_colors in groupby(sorted(self.data)):
            pixel_count.append((color, len(list(group_of_colors))))
        pixel_count.sort(key=lambda l: l[1])
        return pixel_count[-1]

    def multi_image(self, num_imgs=10, wait=1, plot=True):
        intensity_list = []
        times = []
        start = time.time()
        for i in xrange(num_imgs):
            self.__init__()
            self.show()
            intensity_list.append(self.avg_intensity())
            times.append(time.time()-start)
            time.sleep(wait)
        if plot is True:
            plt.plot(times, intensity_list)
            plt.xlabel('Time (s)')
            plt.ylabel('Average Intensity')
            plt.show()
        return intensity_list


# class GetImage:
#    def __init__(self, number_of_images=1, folder='images', wait=0):
#        file_number = 0
#        for x in xrange(number_of_images):
#            self.path = folder+'/'+'image{0}'.format(file_number)
#            image = Webcam()
#            try:
#                while os.path.exists(self.path):
#                    file_number += 1
#                    self.path = folder+'/'+'image{0}'.format(file_number)
#                image.save_image(self.path)
#            except:
#                while os.path.exists(self.path):
#                    file_number += 1
#                    self.path = folder+'/'+'image{0}'.format(file_number)
#                os.makedirs(folder)
#                image.save_image(self.path)
#            time.sleep(wait)


if __name__ == '__main__':

    test = ImProcess()
    print test.avg_intensity()
    test.show()
    print test.most_common_color()
    i = test.multi_image()
