from DNAs_data import insert_data
from commands.command import Command
from functions import get_name


class New(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            arg_list = self.args.split()
            new_string = arg_list[0]
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = get_name(arg_list[1])
            if insert_data(new_name, new_string):
                return True
            else:
                raise ValueError
        except ValueError:
            print("Args not valid")
            return False
