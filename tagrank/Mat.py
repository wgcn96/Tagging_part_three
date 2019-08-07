# -*- coding: utf-8 -*-

"""
Mat.py

The implementation for class Mat

The Mat object represents a movie-tag matrix,
basically, it should have the numpy ndarray, movie number,
tag number and even the corresponding info.
"""

__author__ = 'Wang Chen'
__time__ = '2019/8/6'


from tagrank.static import *


class Mat:
    """
    ndarray:
    shape:
    tag_num:
    movie_num:
    scale:
    """
    def __init__(self, array_path):
        self.ndarray = np.load(array_path)
        self.shape = self.ndarray.shape
        self.tag_num = self.shape[0]
        self.movie_num = self.shape[1]
        self.scale = np.sum(self.ndarray)


if __name__ == '__main__':
    pass