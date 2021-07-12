from commands.command import Command
from datas.data_handler import insert_data
from dnaSequence import DnaSequence
from commands.command_handler import get_id, get_name, get_item


class Slice(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            arg_list = self.args.split()
            if len(arg_list) < 3:
                return False
            dna_item = get_item(arg_list[0])
            s_index = int(arg_list[1])
            e_index = int(arg_list[2])
            new_seq = dna_item.get_string()[s_index:e_index]
            new_dna = DnaSequence()
            if len(arg_list) > 3:
                if arg_list[3] != ":" or len(arg_list) < 5:
                    raise ValueError
                name = get_name(arg_list[4])
                if name == "":
                    dna_item.counter += 1
                    name = dna_item.get_name() + '_s{}'.format(dna_item.counter)
                insert_data(name, new_seq)
            else:
                name = dna_item.get_name()
                new_dna.insert_values(int(get_id(arg_list[0])), name, new_seq)
                print(dna_item.assignment(new_dna))
        except ValueError:
            print("Args not valid")
            return False
