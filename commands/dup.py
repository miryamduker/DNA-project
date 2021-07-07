from DNAs_data import get_dna_by_id, insert_data


class Dup:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        try:
            arg_list = self.__args.split()
            id = arg_list[0].replace("#", "")
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = arg_list[1].replace("@", "")
            dna_item = get_dna_by_id(int(id))
            if new_name is None:
                new_name = dna_item.get_name()+'_{}'.format(id)
            new_string = dna_item.get_string()
            new_string += new_string
            if insert_data(new_name, new_string):
                return True
            raise ValueError
        except ValueError:
            return False
