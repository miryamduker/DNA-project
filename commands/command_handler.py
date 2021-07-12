from datas.data_handler import get_dna_by_id, get_dna_by_name
from datas.dna_data import data_with_name_key


def get_name(name):
    return name.replace("@", "")


def get_id(id):
    return int(id.replace("#", ""))


def name_or_id(x):
    if x[0] == '#':
        return get_id(x)
    elif x[0] == '@':
        return get_name(x)
    else:
        return False


def get_item(item):
    x = name_or_id(item)
    if type(x) == int:
        return get_dna_by_id(x)
    elif type(x) == str:
        return get_dna_by_name(x)
    else:
        return False


def check_function_name(name):
    for key, item in data_with_name_key.items():
        if name == key:
            return True
    return False
