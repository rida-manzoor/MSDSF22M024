import matplotlib.pyplot as plt
import math

#line_plot function will return line plot.
def line_plot(df, x_col, y_col):
    plt.plot(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title('Line Plot')
    plt.show()
#bar_plot function returns bar plot for given values.
def bar_plot(df, x_col, y_col):
    plt.bar(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title('Bar Plot')
    plt.show()
def normal_cdf(x, mean, std):
    """
    Calculates the probability of an event using the cumulative distribution function (CDF)
    of a normal distribution.
    :param x: the value of the event
    :param mean: the mean of the normal distribution
    :param std: the standard deviation of the normal distribution
    :return: probability of the event
    """
    prob = (1.0 + math.erf((x - mean) / (std * math.sqrt(2.0)))) / 2.0
    return prob
def variance(data):
    """
    Calculates the variance of a dataset
    :param data: list of numbers
    :return: variance
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return variance
def median(data):
    """
    Calculates the median of a dataset
    :param data: list of numbers
    :return: median
    """
    n = len(data)
    s = sorted(data)
    if n % 2 == 0:
        median1 = s[n//2]
        median2 = s[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = s[n//2]
    return median
def grouped_median(data):
    """
    Calculates the median of a grouped dataset
    :param data: list of tuples, where each tuple contains the lower and upper bounds of the group and the frequency of the group
    :return: median
    """
    n = sum(x[2] for x in data)
    s = 0
    for x in data:
        if (s + x[2]) >= (n + 1) / 2:
            median = (x[0] + x[1]) / 2
            break
        s += x[2]
    return median
def ungrouped_median(data):
    """
    Calculates the median of an ungrouped dataset
    :param data: list of numbers
    :return: median
    """
    n = len(data)
    s = sorted(data)
    if n % 2 == 0:
        median1 = s[n//2]
        median2 = s[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = s[n//2]
    return median

