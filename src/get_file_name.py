import sys


def get_file_name(name):
    dir_name = sys.path[0] + "/resources/"
    file = dir_name + name + ".txt"

    return file
