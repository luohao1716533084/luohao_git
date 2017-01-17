#coding:utf-8

import os

def files_traverse_func(dir_path):
    list_dirs = os.walk(dir_path)
    files_name_list = []
    for root, dirs, files in list_dirs:
        for d in dirs:
            files_name_list.append(os.path.join(root, d))
        for f in files:
            files_name_list.append(os.path.join(root, f))

    return files_name_list
