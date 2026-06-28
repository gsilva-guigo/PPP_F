import pandas as pd
import numpy as np


def find_intercept(x, y, slope):
	x_mean = np.mean(x)
	y_mean = np.mean(y)
	intercept = y_mean - slope * x_mean
	return intercept


def linear_regression_slope(x, y):
	x_mean = np.mean(x)
	y_mean = np.mean(y)

	numerator = np.sum((x - x_mean) * (y - y_mean))
	denominator = np.sum((x - x_mean) ** 2)
	m = numerator / denominator
	b = find_intercept(x, y, m)

	return m, b

