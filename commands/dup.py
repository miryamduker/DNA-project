from DNAs_data import insert_data
from commands.command import Command
from functions import get_name, get_item, check_function_name


class Dup(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            arg_list = self.args.split()
            new_name = None
            if len(arg_list) > 2:
                raise ValueError
            if len(arg_list) == 2:
                new_name = get_name(arg_list[1])
            dna_item = get_item(arg_list[0])
            if new_name is None:
                dna_name = dna_item.get_name() + '_{}'.format(dna_item.counter)
                while not check_function_name(dna_name):
                    dna_item.counter += 1
                    dna_name = dna_item.get_name() + '_{}'.format(dna_item.counter)
                dna_item.counter += 1
            new_string = dna_item.get_string()
            if insert_data(new_name, new_string):
                return True
            raise ValueError
        except ValueError:
            print("Args not valid")
            return False
