from DNAs_data import get_dna_by_id, insert_data
from functions import get_name, get_item


class Dup:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        try:
            arg_list = self.__args.split()
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = get_name(arg_list[1])
            dna_item = get_item(arg_list[0])
            if new_name is None:
                dna_item.counter += 1
                new_name = dna_item.get_name() + '_{}'.format(dna_item.counter)
            new_string = dna_item.get_string()
            if insert_data(new_name, new_string):
                return True
            raise ValueError
        except ValueError:
            print("Args not valid")
            return False
