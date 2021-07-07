from DNAs_data import data, insert_data


class New:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        try:
            arg_list = self.__args.split()
            new_string = arg_list[0]
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = arg_list[1].replace("@", "")
            if insert_data(new_name, new_string):
                return True
            else:
                raise ValueError
        except ValueError:
            return False
