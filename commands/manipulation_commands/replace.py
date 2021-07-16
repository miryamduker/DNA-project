from commands.command import Command
from datas.data_handler import insert_data
from dnaSequence import DnaSequence
from commands.command_handler import get_item, get_name, name_or_id, check_dna_name


class Replace(Command):
    def __init__(self, args):
        super().__init__(args)

    def execute(self):
        try:
            arg_list = self.args.split()
            if len(arg_list) < 3:
                return False
            sq_id = name_or_id(arg_list[0])
            index = int(arg_list[1])
            new_letter = arg_list[2]
            dna_item = get_item(arg_list[0])
            seq = dna_item.get_string()
            seq = seq[:index]+new_letter+seq[index+1:]
            new_dna = DnaSequence()
            if len(arg_list) > 3:
                if arg_list[3] != ":" or len(arg_list) < 5:
                    raise ValueError
                name = get_name(arg_list[4])
                if name == "":
                    name = dna_item.get_name() + '_r{}'.format(dna_item.counter)
                    dna_item.counter += 1
                insert_data(name, seq)
            else:
                name = dna_item.get_name()
                new_dna.insert_values(sq_id, name, seq)
                print(dna_item.assignment(new_dna))
        except ValueError:
            print("Args not valid")
            return False
