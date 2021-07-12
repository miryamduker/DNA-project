from commands.command import Command
from commands.command_handler import get_item


class Len(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            if len(self.arg_list) != 1:
                raise ValueError
            dna = get_item(self.arg_list[0])
            print(len(dna))
        except ValueError:
            print("Args not valid")
            return False
