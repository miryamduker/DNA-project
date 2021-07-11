from DNAs_data import data_with_id_key, data_with_name_key
from commands.command import Command
from functions import get_item


class Delete(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            arg_list = self.args.split()
            if len(arg_list) != 1:
                raise ValueError
            dna_item = get_item(arg_list[0])
            print("Do you really want to delete {}: {}?\nPlease confirm by y/Y or cancel by n/N\n> confirm >>>".format(dna_item.get_name(), dna_item.get_string()), end="")
            confirmation = input()
            while confirmation not in 'yYnN':
                print("You have typed an invalid response. Please confirm with a valid response\n> confirm >>>", end="")
                confirmation = input()
            if confirmation in 'yY':
                data_with_id_key.pop(dna_item.get_id())
                data_with_name_key.pop(dna_item.get_name())
                print("Deleted : [{}] {}: {}".format(dna_item.get_id(), dna_item.get_name(), dna_item.get_string()))
            if confirmation in 'nN':
                return
        except ValueError:
            print("Args not valid")
            return False

