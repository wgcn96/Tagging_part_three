# -*- coding: utf-8 -*-

"""
sample.py

sample a small scale of movies.
basically, three fotrh of the movies are supposed to posses
at least one tag.
"""

__author__ = 'Wang Chen'
__time__ = '2019/8/8'

import sys
sys.path.extend(['/data/wangchen/auto-tagging/Tagging_part_three/', '/data/wangchen/auto-tagging/Tagging_part_three/sample_matrix'])


from sample_matrix.static import *

if_disp = True
num = 10000
np.random.seed(0)


if __name__ == '__main__':

    random_list = np.random.permutation(59334)[:num]

    matrix = np.load(os.path.join(workdir, 'matrix', 'full_matrix.npy'))
    while True:
        part_matrix = matrix[random_list]

        if if_disp: print(part_matrix.shape)

        check_list = np.where(np.sum(part_matrix, axis=1) > 0)
        check = check_list[0].shape[0]/num

        if if_disp: print(check)

        if check >= 0.75:
            break

        random_list = np.random.permutation(59334)[:num]

