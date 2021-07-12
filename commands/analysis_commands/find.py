from commands.command import Command
from commands.command_handler import get_item


class Find(Command):
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
            index = dna.get_string().find(sq)
            if index >= 0:
                print(index)
                return
            print("Couldn't find sequence")
            return
        except ValueError:
            print("Args not valid")
            return
