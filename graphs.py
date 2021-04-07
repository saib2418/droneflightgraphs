import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.patches as mpatches

__author__ = "Sai Bharathula"
__copyright__ = "Copyright 2020, Vimaan Robotics"


# key: intervalNum (intervals are 30 seconds apart) value: tuple(successNum, failNum)
def bar_graph():
    """
    def bar_graph() is a function that produces Figure 1
    where a comparison of success(blue color) vs failure (orange color)
    of drone flights are plotted in each 30 second interval.
    """
    result = {}
    # read excel file where all the data related to drone flights are stored
    df = pd.read_excel("inputFiles/Battery_Aging.xlsx")
    # read the column of total flight times
    times = (df["Total flight time(s)"])

    # going through the number of rows that have total flight time in seconds
    for i in range(len(times)):
        # find the interval assignment (interval 1 - 1.5 , 1.5 - 2, 2.5 - 3]
        intervalNum = (int(times[i] / 30)) * 0.5
        if intervalNum < 1:
            continue;

        # if intervalNum not in dictionary
        # Failed flight times are indicated through '0' & success through '1'
        if intervalNum not in result:
            if df['Fail'][i] == 0:
                result[intervalNum] = (0, 1)
            elif df['Fail'][i] == 1:
                result[intervalNum] = (1, 0)
        # store total Failures in 1st index, total Successes in 0 index
        else:
            numFailures = result[intervalNum][1]
            numSuccesses = result[intervalNum][0]
            if df['Fail'][i] == 0:
                result[intervalNum] = (numSuccesses, numFailures + 1)
            elif df['Fail'][i] == 1:
                result[intervalNum] = (numSuccesses + 1, numFailures)
    # created 3 arrays to store flight times, number of success, and number of failures from tuple
    times = []
    successes = []
    failures = []
    minutes = list(result.keys())
    minutes.sort()

    # append values related to eachc category in the array
    for key in minutes:
        times.append(key)
        successes.append(result[key][0])
        failures.append(result[key][1])

    # plot bar graph
    plt.xlabel("Total Flight time(m)")
    plt.ylabel("Total Number of Flights")
    plt.title("Time vs Flight Success")
    plt.xticks(np.arange(1, 10, 0.5))

    f = plt.figure(1)
    barWidth = 0.5
    plt.bar(times, successes, edgecolor="white", width=barWidth)
    plt.bar(times, failures, edgecolor="white", bottom=successes, width=barWidth)

    f.show()

    """"
    created a table correlating to bar graph 
    to quantify the number of successes vs failures 
    for better understanding of why there were more failed flights in certain time intervals
    """
    interval = [" 0 - 1.0 ", " 1.0 - 1.5 ", " 1.5 - 2.0 ", " 2.0 - 2.5 ", " 2.5 - 3.0 ", " 3.0 - 3.5 ", " 3.5 - 4.0 ",
                " 4.0 - 4.5 ", " 4.5 - 5.0 ", " 5.0 - 5.5 ", " 5.5 - 6.0 ", " 6.0 - 6.5 ", " 6.5 - 7.0 ", " 7.0 - 7.5 ",
                " 7.5 - 9.0 "]
    fig = go.Figure(data=[go.Table(header=dict(values=['Interval Time', 'Flight Successes', 'Flight Failures']),
                                   cells=dict(values=[interval, successes, failures]))])
    fig.show()


def scatter_plot():
    """
    def scatter_plot() is a function that produces Figure 2
    where a comparison of success(blue color) vs failure (red color)
    of drone flights are plotted against battery voltage drop variable
    """
    g = plt.figure(2)
    df = pd.read_excel("inputFiles/Battery_Aging.xlsx")
    x = df['Total flight time(s)']
    y = df['Voltage Drop']
    plt.xlabel("Total Flight Time(s)")
    plt.ylabel("Voltage Drop")
    plt.title("Voltage Drop vs Flight Time")
    plt.scatter(x, y, s=7, c=df["Fail"], cmap=plt.cm.RdYlBu)

    # code a legend for scatter plot:
    red_patch = mpatches.Patch(color='red', label='Failed')
    blue_patch = mpatches.Patch(color='blue', label='Success')
    plt.legend(handles=[red_patch, blue_patch], loc="lower left")

    plt.show()


def detailed_scatter_plot():
    """
    def detailed_scatter_plot() is a function that produces Figure 3
    where I zoom in on seconds where the most failed flights occur
    (300 - 475) seconds to further analyze at which
    battery voltage drops and times are the flights failing
    """
    z = plt.figure(3)
    df = pd.read_excel("inputFiles/test.xlsx")
    x = df['Total flight time(s)']
    y = df['Voltage Drop']
    plt.xlabel("Total Flight Time(s)")
    plt.ylabel("Voltage Drop")
    plt.title("Voltage Drop vs Flight Time")
    plt.scatter(x, y, s=7, c=df["Fail"], cmap=plt.cm.RdYlBu)

    # code a legend for scatter plot:
    red_patch = mpatches.Patch(color='red', label='Failed')
    blue_patch = mpatches.Patch(color='blue', label='Success')
    plt.legend(handles=[red_patch, blue_patch], loc="lower left")

    plt.show()


def battery_age_scatterplot():
    """
    def battery_age_scatter_plot() is a function that produces Figure 4
    where a comparison of success(blue color) vs failure (red color)
    of drone flights are plotted against battery age.
    """
    a = plt.figure(4)
    df = pd.read_excel("inputFiles/age.xlsx")
    x = df['Total flight time(s)']
    y = df['Total Flight Time (m)']
    plt.xlabel("Flight Time")
    plt.ylabel("Age in Minutes")
    plt.title("Battery Age vs Time")
    plt.scatter(x, y, s=7, c=df["Fail"], cmap=plt.cm.RdYlBu)
    red_patch = mpatches.Patch(color='red', label='Failed')
    blue_patch = mpatches.Patch(color='blue', label='Success')
    plt.legend(handles=[red_patch, blue_patch], loc="lower left")
    plt.show()


def threedee_plot():
    """
       def three_dee__plot() is a function that produces Figure 5
       where a comparison of success(blue color) vs failure (red color)
       of drone flights are plotted on a 3-D plot to analyze how
       battery age and battery voltage drop affect drone flight time an failures
       """
    b = plt.figure(5)
    ax = plt.axes(projection='3d')
    df = pd.read_excel("inputFiles/threedee.xlsx")
    x = df['Total flight time(s)']
    y = df['Total Flight Time (m)']
    z = df['Voltage Drop']
    plt.xlabel("Flight Time")
    plt.ylabel("Age in Minutes")
    ax.set_zlabel("Voltage Drop")
    plt.title("Battery Age & Time vs Voltage Drop")
    ax.scatter3D(x, y, z, c=df['Fail'], cmap=plt.cm.RdYlBu)
    red_patch = mpatches.Patch(color='red', label='Failed')
    blue_patch = mpatches.Patch(color='blue', label='Success')
    plt.legend(handles=[red_patch, blue_patch], loc="upper left")
    plt.show()



bar_graph()
scatter_plot()
detailed_scatter_plot()
battery_age_scatterplot()
threedee_plot()