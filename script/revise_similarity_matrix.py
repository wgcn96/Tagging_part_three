# -*- coding: utf-8 -*-

"""
revise_similarity_matrix.py

重构similarity matrix， 删除冗余的行
"""

__author__ = 'Wang Chen'
__time__ = '2019/8/7'

import sys
sys.path.extend(['/data/wangchen/auto-tagging/Tagging_part_three/', '/data/wangchen/auto-tagging/Tagging_part_three/script'])


from script.static import *


if __name__ == '__main__':
    if_disp = True
    if if_disp: print(datetime.datetime.now(), "begin loading matrix...")

    similarity_matrix_path = os.path.join(redundancy_dir, 'matrix.txt')
    matrix = np.zeros((59370, 59370), dtype=np.float32)
    with open(similarity_matrix_path) as f:
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

    if if_disp: print(datetime.datetime.now(), "load matrix finish")

    redundancy_movie_dict = {}
    redundancy_pos_list = []
    pos = 0
    redundancy_id_file_path = os.path.join(redundancy_dir, 'movie_id_duplicate.txt')
    with open(redundancy_id_file_path, encoding='utf-8') as redundancy_id_file:
        while True:
            line = redundancy_id_file.readline().strip()
            if not line:
                break
            check_pos = redundancy_movie_dict.get(line, -1)
            if check_pos != -1:
                redundancy_pos_list.append(pos)
            else:
                # redundancy_movie_list.append(line)
                redundancy_movie_dict[line] = pos
                pos += 1

    refined_matrix = np.delete(matrix, redundancy_pos_list, 0)
    refined_matrix = np.delete(refined_matrix, redundancy_pos_list, 1).astype(np.float32)
    if if_disp: print("refined matrix shape: ", refined_matrix.shape)

    save_path = os.path.join(redundancy_dir, 'refined_similarity_matrix.txt')
    np.savetxt(save_path, refined_matrix)

