from DNAs_data import data_with_id_key, data_with_name_key
from functions import get_item


class Delete:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        try:
            arg_list = self.__args.split()
            if len(arg_list) != 1:
                raise ValueError
            sq = get_item(arg_list[0])
            print("Do you really want to delete {}: {}?\nPlease confirm by y/Y or cancel by n/N\n> confirm >>>".format(sq.get_name(), sq.get_string()), end="")
            confirmation = input()
            while confirmation not in 'yYnN':
                print("You have typed an invalid response. Please confirm with a valid response\n> confirm >>>", end="")
                confirmation = input()
            if confirmation in 'yY':
                data_with_id_key.pop(sq.get_id())
                data_with_name_key.pop(sq.get_name())
                print("Deleted : [{}] {}: {}".format(sq.get_id(), sq.get_name(), sq.get_string()))
            if confirmation in 'nN':
                return
        except ValueError:
            print("Args not valid")
            return False

