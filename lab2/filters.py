#! usr/bin/env python

# Derek Bean
# ME 599
# 1/24/2017

import numpy as np
from sensor import *


def three_point_mean(data):
    output = []
    for idx, val in enumerate(data):
        if idx == 0:
            output.append(np.mean(data[0:2]))
        elif idx == len(data):
            output.append(np.mean(data[-3:-1]))
        else:
            output.append(np.mean(data[idx-1:idx+2]))
    return data, output


def variable_width_mean(data, width):
    output = []
    if width % 2 and width > 0:
        for idx, val in enumerate(data):
            if idx <= width:
                output.append(np.mean(data[0:width]))
            elif idx >= len(data)-width:
                output.append(np.mean(data[-width:-1]))
            else:
                output.append(np.mean(data[idx-width:idx+width+1]))
        return data, output
    else:
        print('Width ' + str(width) + ' is not odd and/or positive')
        return None, None


def variable_width_median(data, width):
    output = []
    if width % 2 and width > 0:
        for idx, val in enumerate(data):
            if idx <= width:
                output.append(np.median(data[0:width]))
            elif idx >= len(data)-width:
                output.append(np.median(data[-width:-1]))
            else:
                output.append(np.median(data[idx-width:idx+width+1]))
        return data, output
    else:
        print('Width ' + str(width) + ' is not odd and/or positive')
        return None, None


if __name__ == '__main__':
    data = generate_sensor_data()
    data1, output1 = three_point_mean(data)
    data2, output2 = variable_width_mean(data, 3)
    data3, output3 = variable_width_mean(data, 4)
    data4, output4 = variable_width_median(data, 3)
    data5, output5 = variable_width_median(data, 4)
    