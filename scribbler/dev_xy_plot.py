import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import random



def create_plot_x_y_arc(blocks,
                        start_min_max = 50,   # Means a range of -50 to 50
                        stop_min_max =  50,   # Means a range of -50 to 50


                        points=[[0, 1, 2, 3], [0, 1, 2, 3]], fieldname='default'):
    # https://stackoverflow.com/questions/52014197/how-to-interpolate-a-2d-curve-in-python
    # The purpose of this function is to provide
    # properly spaced quadratic x y points for the plot type
    # and geometrically expand them to fit the number of sentences
    #TODO need a check to see if the len of points match
    print(start_min_max, stop_min_max)


    if fieldname:
        fieldname = "plot." + fieldname


    # get the highest |n| number from the list
    nums = []
    for i in points[1]:
        nums.append(abs(i))
    max_value = max(nums)
    modifier = start_min_max / max_value


    x = []
    for i in points[0]:
        x.append(i * int(blocks / 100))
    y = []
    for i in points[1]:
        y.append(i * modifier)

    points = [x, y]
    points = np.array(points).T

    # Linear length along the line:
    distance = np.cumsum(np.sqrt(np.sum(np.diff(points, axis=0) ** 2, axis=1)))
    distance = np.insert(distance, 0, 0) / distance[-1]

    # Interpolation for different methods:
    interpolations_methods = ['quadratic']
    alpha = np.linspace(0, 1, blocks)

    return_list = []
    interpolated_points = {}
    for method in interpolations_methods:
        interpolator = interp1d(distance, points, kind=method, axis=0)
        interpolated_points[method] = interpolator(alpha)

    for method_name, curve in interpolated_points.items():
        count = 1
        for i in curve:
            entry = {'block': count, fieldname: int(i[1])}
            return_list.append(entry)
            count = count + 1

    df = pd.DataFrame(return_list)
    print(df)

    return df

basic_plots = {
    'rise':             np.array([[0, 25, 50, 75,100],  [-17, -20, 0, 20, 17]]),
    'fall':             np.array([[0, 25, 50, 75,100],  [17, 20, 0, -20, -17]]),
    'fall_rise':        np.array([[0, 15, 29, 37, 55, 75,85, 100],  [12, 8, 0,  -8, -22, 5, 10, 13]]),
    'rise_fall':        np.array([[0, 25, 50, 75,100],  [-15, -3, 20, -3, -15]]),
    'rise_fall_rise':   np.array([[0, 25, 50, 75,100],  [-15, 15, 0, -14,15]]),
    'fall_rise_fall':   np.array([[0, 25, 50, 75,100],  [15, -15, 0, 14,-15]])
}


stories = range(1,10)
accumulated_plots = []
x = []
y = []
for n in stories:
    key = random.choice(list(basic_plots))
    selected_archetype = basic_plots[key]
    accumulated_plots.append(selected_archetype)
    x.append(selected_archetype[0])
    y.append(selected_archetype[1])

print(x)

print(y)

running_x = [0]
for test_list in x:
    # generate successive difference list using list comprehension
    res = [test_list[i + 1] - test_list[i] for i in range(len(test_list) - 1)]
    for x in res:
        last_num = running_x[-1]
        running_x.append(x+last_num)

print(running_x)
# starting with 0, add the previous number


import sys
sys.exit()




blocks = 1060
points = [[0, 15, 29, 37, 55, 75,85, 100],  [12, 8, 0,  -8, -15, 5, 10, 13]]
coordinates = create_plot_x_y_arc(blocks=blocks, points=points)

plot.plot(coordinates['plot.default'])
plot.show()