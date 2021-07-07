from DNAs_data import insert_data


class Load:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        try:
            arg_list = self.__args.split()
            file_path = arg_list[0]
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = arg_list[1].replace("@", "")
            file = open(file_path,'r')
            new_string = file.read()
            file.close()
            if insert_data(new_name, new_string):
                return True
            raise ValueError
        except ValueError:
            return False
