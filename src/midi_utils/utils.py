import os
import json
import pickle
import ntpath
import fnmatch


def save_obj(obj, name):
    save_name = name.with_suffix('.pkl')
    with open(save_name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    save_name = name.with_suffix('.pkl')
    with open(save_name, 'rb') as f:
        return pickle.load(f)


def find_files_in_subdir(folder, regexp):
    match_files = list(Path(folder).glob(regexp))
    return match_files
