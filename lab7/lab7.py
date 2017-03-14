#! usr/bin/env python

# Derek Bean
# ME 599
# lab 7
# 2/28/2017

from grabber import Webcam
from PIL import ImageChops, Image
import time
import matplotlib.pyplot as plt
from itertools import groupby
import scipy.signal
import numpy as np
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
#     Write a function that detects motion in the image stream that returns
#         the average pixel difference in a function called motion that
#         returns True or False if there is motion in the quad
#     Write a function called event that returns true if there's an event
#         happening in the quad


class ImProcess:
    def __init__(self):
        # Initialize both the image and the data variables
        self.image = Webcam()
        self.data = self.image.grab_image_data()

    def open_file(self, filename):
        # Open an external file as a PIL image file for use in the class
        # Objects created by this class use the fucntions of the PIL toolbox
        return Image.open(filename)

    def show(self):
        self.image.grab_image().show()

    def avg_intensity(self, other=None):
        # If the average intensity of an image that is not self input it as
        # other and the average intensity will be returned provided the
        # other image is a PIL Image object
        if other is None:
            # Average the intensity of each pixel in the image
            pixel_data = list(self.data)
            pixel_mean = [sum(x)/len(x) for x in pixel_data]
            # Average the intensity of all pixels in the image
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
        # Write the most common color and the ratio of said color to a txt file
        ans = open('answers.txt', 'w')
        ans.writelines('{0} is the most common color'.format(common_color) +
                       '\n' +
                       'The ratio of pixels that ' +
                       'are this color is {0}'.format(color_ratio))
        ans.close()
        return (common_color, color_ratio)

    def multi_image(self, num_imgs=99, wait=1, plot=True):
        # Take num_imgs from the webcam with a time delay of wait and return
        # return the average intensity of all the images
        self.intensity_list = []
        times = []
        start = time.time()
        for i in xrange(num_imgs):
            self.__init__()
            self.intensity_list.append(self.avg_intensity())
            times.append(time.time()-start)
            time.sleep(wait)
        # Filter the average intensities based on a 9 point median filter
        self.filtered_intensity_list = scipy.signal.\
                                       medfilt(self.intensity_list, 9)
        if plot is True:
            plt.figure(1)
            plt.plot(times, self.intensity_list)
            plt.plot(times, self.filtered_intensity_list)
            plt.xlabel('Time (s)')
            plt.ylabel('Average Intensity')
            plt.legend(['Raw Intensity', 'Filtered Intensity'], loc=0)
            plt.ylim([40, 120])
            plt.show()
        return self.intensity_list, self.filtered_intensity_list

    def motion(self):
        # Determine if there is motion in the quad based on two images grabbed
        # close together then subtracted from one another. The euclidean
        # distance of the subracted image determines if there is motion based
        # on an observed value for motion
        img1 = self.image.grab_image()
        self.__init__()
        img2 = self.image.grab_image()
        movement = ImageChops.difference(img1, img2)
        if self.euclidean_distance(movement) > 8000:
            return True
        else:
            return False

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
        # Determine if there is an event in the center square of the quad
        cropped = self.cropit()
        # Create a new image that is the same size as the cropped one that is
        # a gray close to the color of the concrete in the quad
        gray_img = Image.new('RGB', cropped.size, (150, 150, 150))
        diff_img = ImageChops.difference(cropped, gray_img)
        # Determine if there is an event based on if the euclidean distance is
        # above the observed threshold
        # (blue, black and orange 'tents' were tested)
        if self.euclidean_distance(diff_img) > 14500:
            return True
        else:
            return False

if __name__ == '__main__':
    test = ImProcess()
    # test.multi_image()
    print 'Average Intensity: ', test.avg_intensity()
    print 'Most Common Color: ', test.most_common_color()[0]
    print 'Ratio of most common color pixels: ', test.most_common_color()[1]
    print 'Is it daytime: ', test.daytime()
    print 'Is there movement: ', test.motion()
    print 'Is there an event: ', test.event()

