from datas.data_handler import get_dna_by_id, get_dna_by_name
from datas.dna_data import data_with_name_key


def get_name(name):
    """
    :param name:
    :return: returns name without @
    """
    return name.replace("@", "")


def get_id(id):
    """
    :param id:
    :return: returns id without #
    """
    return int(id.replace("#", ""))


def name_or_id(x):
    """
    :param x:
    :return: name or id, without the first char ( # or @)
    """
    if x[0] == '#':
        return get_id(x)
    elif x[0] == '@':
        return get_name(x)
    else:
        return False


def get_item(item):
    """
    :param item:
    :return: the object the matches the name or id that was sent as item
    """
    x = name_or_id(item)
    if type(x) == int:
        return get_dna_by_id(x)
    elif type(x) == str:
        return get_dna_by_name(x)
    else:
        return False


def check_dna_name(name):
    """
    :param name:
    :return: true if the name exists, false otherwise
    """
    for key, item in data_with_name_key.items():
        if name == key:
            return True
    return False
