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


def load_similarity_matrix(matrix_path, if_test=False, if_disp=True):
    if if_test:
        similarity_matrix = np.eye(59334, dtype=np.int32)
        return similarity_matrix
    else:
        if if_disp: print(datetime.datetime.now(), "begin loading matrix...")

        # matrix = np.zeros((59334, 59334), dtype=np.float32)  # Hard code here
        # with open(matrix_path) as f:
        #     index = 0
        #     while True:
        #         print(index)
        #         line = f.readline()
        #         if not line:
        #             break
        #         temp_list = line.split()
        #         for i, value in enumerate(temp_list):
        #             matrix[index][i] = value
        #         index += 1

        matrix = np.load(matrix_path)

        if if_disp: print(datetime.datetime.now(), "load matrix finish")
        return matrix


def run_tag_rank(mat, similarity_matrix, round, if_nor=False, if_disp=True):
    """

    :param mat:
    :param similarity_matrix:
    :param round:
    :return:
    """
    if if_disp: print("begin to calculate matrix, ", datetime.datetime.now())

    tmp_matrix = mat.ndarray
    result_matrix_list = []
    for k in range(round):

        if if_disp: print("round {}".format(k))

        # tmp_matrix = np.dot(similarity_matrix, tmp_matrix)
        for j in range(mat.tag_num):
            if if_disp: print("current {} column".format(j))
            tmp_matrix[:, j] = np.dot(similarity_matrix, tmp_matrix[:, j].reshape(-1, 1)).reshape(-1)

        if if_nor:
            norm_matrix = np.linalg.norm(tmp_matrix, axis=0, ord=1, keepdims=True)      #  1范数规范化，按列取归一化值
            for j in range(mat.tag_num):
                tmp_matrix[j, :] = tmp_matrix[j, :] / norm_matrix[j, :]

        result_matrix_list.append(tmp_matrix)

    if if_disp: print(datetime.datetime.now(), "calculate matrix finish")

    return result_matrix_list


if __name__ == '__main__':
    similarity_matrix_path = os.path.join(matrixdir, 'refined_similarity_matrix.npy')
    full_matrix_path = os.path.join(matrixdir, 'full_matrix.npy')
    mat = load_mat(full_matrix_path)
    similarity_matrix = load_similarity_matrix(similarity_matrix_path)
    run_tag_rank(mat, similarity_matrix, 1)
