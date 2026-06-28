import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from csv_create import create_csv
from linear_r import *

class RegressionPlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        self.ax_button = plt.axes([0.7, 0.05, 0.2, 0.075])
        self.btn_refresh = Button(self.ax_button, 'Refresh Points')
        self.btn_refresh.on_clicked(self.refresh_plot)

        self.refresh_plot(None)

    def refresh_plot(self, event):
        # Create new random data
        create_csv('data')
        data = pd.read_csv('data.csv')

        print(data.head())

        # Clear the plot
        self.ax.clear()

        # Calculate the slope and y-intercept
        slope, intercept = linear_regression_slope(data['x'], data['y'])
        print(f"Slope: {slope}, Y-Intercept: {intercept}")

        # Plot the data
        self.ax.scatter(data['x'], data['y'], label='Data points')

        # Create regression line
        x_line = np.array([data['x'].min(), data['x'].max()])
        y_line = slope * x_line + intercept
        self.ax.plot(x_line, y_line, color='red', label=f'y = {slope:.2f}x + {intercept:.2f}')

        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title('Linear Regression Example')
        self.ax.legend()

        self.fig.canvas.draw_idle()

def main():
    plotter = RegressionPlotter()
    plt.show()

main()