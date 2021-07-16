from commands.command import Command
from commands.command_handler import get_name, get_item, check_dna_name
from datas.data_handler import insert_data


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
                new_name = dna_item.get_name() + '_{}'.format(dna_item.counter)
                while check_dna_name(new_name):
                    dna_item.counter += 1
                    new_name = dna_item.get_name() + '_{}'.format(dna_item.counter)
                dna_item.counter += 1
            new_string = dna_item.get_string()
            if insert_data(new_name, new_string):
                return True
            raise ValueError
        except ValueError:
            print("Args not valid")
            return False
