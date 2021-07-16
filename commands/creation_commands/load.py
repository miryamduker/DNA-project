from commands.command import Command
from commands.command_handler import get_name
from datas.data_handler import insert_data


class Load(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            arg_list = self.args.split()
            file_path = arg_list[0]
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = get_name(arg_list[1])
            file = open(file_path, 'r')
            new_string = file.read()
            file.close()
            if insert_data(new_name, new_string):
                return True
            raise ValueError
        except ValueError:
            print("Args not valid")
            return False
        except:
            print("Error, check file name")
