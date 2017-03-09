#! usr/bin/env python

# Derek Bean
# ME 599
# lab 7
# 2/28/2017

from grabber import Webcam
from PIL import ImageChops, ImageFilter, Image
import time
import matplotlib.pyplot as plt
from itertools import groupby
import scipy.signal
import numpy as np
import operator
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

    def open_file(self, filename):
        return Image.open(filename)

    def show(self):
        self.image.grab_image().show()

    def avg_intensity(self, other=None):
        if other is None:
            pixel_data = list(self.data)
            pixel_mean = [sum(x)/len(x) for x in pixel_data]
            return sum(pixel_mean) / len(pixel_mean)
        else:
            pixel_data = other.getdata()
            pixel_mean = [float(sum(x))/len(x) for x in pixel_data]
            return float(sum(pixel_mean)) / len(pixel_mean)

    def euclidean_distance(self, img=None):
        if img is None:
            return np.sqrt(np.sum(np.power(np.array(self.data), 2)))
        else:
            return np.sqrt(np.sum(np.power(np.array(img.getdata()), 2)))

    def colors(self):
        return set(self.data)

    def most_common_color(self):
        pixel_count = []
        for color, group_of_colors in groupby(sorted(self.data)):
            pixel_count.append((color, len(list(group_of_colors))))
        pixel_count.sort(key=lambda l: l[1])
        pixel_rel = [(x[0], float(x[1])/len(self.data)) for x in pixel_count]
        common_color = pixel_rel[-1][0]
        color_ratio = pixel_rel[-1][1]
        ans = open('answers.txt', 'w')
        ans.writelines('{0} is the most common color'.format(common_color) +
                       '\n' +
                       'The ratio of pixels that ' +
                       'are this color is {0}'.format(color_ratio))
        ans.close()
        return (common_color, color_ratio)

    def multi_image(self, num_imgs=10, wait=1, plot=True):
        intensity_list = []
        times = []
        start = time.time()
        for i in xrange(num_imgs):
            self.__init__()
            intensity_list.append(self.avg_intensity())
            times.append(time.time()-start)
            time.sleep(wait)
        if plot is True:
            plt.plot(times, intensity_list)
            plt.plot(times, scipy.signal.medfilt(intensity_list, 9))
            plt.xlabel('Time (s)')
            plt.ylabel('Average Intensity')
            plt.legend(['Raw Intensity', 'Filtered Intensity'], loc=0)
            plt.show()
        return intensity_list

    def motion(self):
        img1 = self.image.grab_image()
        self.__init__()
        img2 = self.image.grab_image()
        movement = ImageChops.difference(img1, img2)
#        movement.show()
        return self.euclidean_distance(movement)

    def daytime(self, threshold=70):
        if self.avg_intensity() > threshold:
            return True
        else:
            return False

    def cropit(self, left=234, right=234+296,
               upper=350, lower=350+140):
        img = self.image.grab_image()
        return img.crop((left, upper, right, lower))

    def event(self):
        cropped = self.cropit()
        cropped.show()
#        edges = ImageOps.equalize(edges)
#        edges = edges.convert('1')
#        edges.show()
        refer = self.open_file('black-tent.jpg')
        refer = refer.crop((234, 325, 234+296, 344+140))
#        refer.show()
#        diff_img = ImageChops.screen(cropped, refer)
#        diff_img = ImageChops.difference(cropped, ImageChops.offset(cropped,1))
#        diff_img.show()
#        print self.avg_intensity(diff_img)
        diff_colors = cropped.histogram()
        diff_colors2 = refer.histogram()
#        diff_colors =  list(map(operator.sub, diff_colors, diff_colors2))
#        plt.plot(diff_colors[0:255], 'r')
#        plt.plot(diff_colors[256:511], 'g')
#        plt.plot(diff_colors[511:768], 'b')
#        plt.show()
        plt.plot(diff_colors2[0:255], 'r')
        plt.plot(diff_colors2[256:511], 'g')
        plt.plot(diff_colors2[511:768], 'b')
        plt.show()
        return 

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
    b = test.most_common_color()
    print 'Average Intensity: ', test.avg_intensity()
    print 'Most Common Color: ', test.most_common_color()
    print 'Is it daytime: ', test.daytime()
    moving = test.motion()
    print 'Is there movement: ', moving
#    test.multi_image(num_imgs=10)
    edges = test.event()
