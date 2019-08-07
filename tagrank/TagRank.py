# -*- coding: utf-8 -*-

"""
note something here

"""

__author__ = 'Wang Chen'
__time__ = '2019/8/6'


import sys
sys.path.extend(['/data/wangchen/auto-tagging/Tagging_part_three/', '/data/wangchen/auto-tagging/Tagging_part_three/tagrank'])


from tagrank.Mat import Mat
from tagrank.static import *


def load_mat(matrix_path):
    mat = Mat(matrix_path)
    return mat


def load_similarity_matrix(matrix_path, if_test=False):
    if if_test:
        similarity_matrix = np.eye(59334, dtype=np.int32)
        return similarity_matrix
    else:
        print(datetime.datetime.now(), "begin loading matrix...")
        matrix = np.zeros((59370, 59370), dtype=np.float32)  # Hard code here
        with open(matrix_path) as f:
            index = 0
            while True:
                print(index)
                line = f.readline()
                if not line:
                    break
                temp_list = line.split()
                for i, value in enumerate(temp_list):
                    matrix[index][i] = value
                index += 1

        print(datetime.datetime.now(), "load matrix finish")
        return matrix




if __name__ == '__main__':
    similarity_matrix_path = os.path.join(datadir, 'video redundancy', 'matrix.txt')
    full_matrix_path = os.path.join(matrixdir, 'full_matrix.npy')
    mat = load_mat(full_matrix_path)
    similarity_matrix = load_similarity_matrix(similarity_matrix_path, if_test=True)
