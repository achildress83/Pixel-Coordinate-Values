import numpy as np
import itertools

class Rectangle():

    def __init__(self, image_dimensions, corner_points):
        self.size = image_dimensions
        self.corner_points = corner_points
        self.rows = image_dimensions[0]
        self.cols = image_dimensions[1]

    # sorts corner_points input to define the rectangle
    def sort_corner_points(self):
        '''input: takes a list of tuples representing the four corners of the rectangle
            output: returns top right and bottom left coordinates'''
        corner_points_sorted = sorted(self.corner_points, key=lambda i: (i[0], i[1]))
        bottom_left = corner_points_sorted[0]
        top_right = corner_points_sorted[-1]
        return bottom_left, top_right

    # gets all equally spaced x and y coordinate values as independent arrays
    def create_coords(self):
        '''input: takes output from sort_corner_points (bottom left and top right coordinates)
            output: returns separate arrays of x and y coordinates
            for all equally spaced points w/in bounds'''
        bottom_left, top_right = self.sort_corner_points()
        x_coords = np.linspace(bottom_left[0], top_right[0], num=self.rows)
        y_coords = np.linspace(bottom_left[1], top_right[1], num=self.cols)
        return x_coords, y_coords

    # gets all combinations of x and y coordinates
    def create_matrix(self):
        '''input: takes output from create_coords (x_coords and y_coords)
        output: returns solution (all equally spaced points in rectangle)'''
        x_coords, y_coords = self.create_coords()
        output = list(itertools.product(x_coords, y_coords))
        output = np.array([list(i) for i in output]).reshape((self.rows, self.cols, 2))
        return output.tolist()
