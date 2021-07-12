import re

from commands.command import Command
from commands.command_handler import get_item


class Count(Command):
    def __init__(self, args):
        super().__init__(args)
    def execute(self):
        try:
            if len(self.arg_list) != 2:
                raise ValueError
            dna = get_item(self.arg_list[0])
            sq = self.arg_list[1]
            if sq[0] == '#' or sq[0] == '@':
                sq = get_item(self.arg_list[1]).get_string()
            dna_sq = dna.get_string()
            all_indexes = [m.start() for m in re.finditer(sq, dna_sq)]
            if not all_indexes:
                print("Couldn't find sequence")
                return
            print(len(all_indexes))
        except ValueError:
            print("Args not valid")
            return