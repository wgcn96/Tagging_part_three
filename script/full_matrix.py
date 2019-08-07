# -*- coding: utf-8 -*-

"""
full_matrix.py

generate the full matrix
"""

__author__ = 'Wang Chen'
__time__ = '2019/8/7'


from script.static import *


def load_list_dict_from_file(file_path, if_disp=False):
    file = open(file_path, encoding='utf-8')
    pos = 0
    result_list = []
    result_dict = {}
    while True:
        line = file.readline().strip()
        if not line:
            break

        content = line.split(" ")[0]
        result_list.append(content)
        result_dict[content] = pos
        pos += 1

    if if_disp: print("total length: ", pos)

    return result_list, result_dict, pos


if __name__ == '__main__':
    if_disp = False
    redundancy_dir = os.path.join(datadir, 'video redundancy')
    movie_id_file_path = os.path.join(redundancy_dir, 'movie_id.txt')
    tag_id_file_path = os.path.join(redundancy_dir, 'tag.txt')

    all_tag_file_path = os.path.join(datadir, 'all_tag_search.json')
    all_tags_content = json.load(open(all_tag_file_path, encoding='utf-8'))
    if if_disp: print("all tagged movies: ", len(all_tags_content))

    movie_id_list, movie_id_dict, movie_num = load_list_dict_from_file(movie_id_file_path, if_disp)
    tag_id_list, tag_id_dict, tag_num = load_list_dict_from_file(tag_id_file_path, if_disp)

    result_matrix = np.zeros((movie_num, tag_num), dtype=np.int32)
    for movie, items in all_tags_content.items():
        cur_movie_pos = movie_id_dict.get(movie, None)
        if not cur_movie_pos:   # movie id not found
            continue
        for item in items:
            cur_tag_pos = tag_id_dict.get(item)
            result_matrix[cur_movie_pos][cur_tag_pos] = 1

    if if_disp: print("total matrix sum: ", np.sum(result_matrix))

    save_path = os.path.join(workdir, 'matrix', 'full_matrix.npy')
    np.save(save_path, result_matrix)
