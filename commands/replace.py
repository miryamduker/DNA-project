from DNAs_data import insert_data
from dnaSequence import DnaSequence
from functions import get_item, get_name, name_or_id


class Replace:
    def __init__(self, args):
        self.__args = args

    def execute(self):
        try:
            arg_list = self.__args.split()
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
                    dna_item.counter += 1
                    name = dna_item.get_name() + '_r{}'.format(dna_item.counter)
                insert_data(name, seq)
            else:
                name = dna_item.get_name()
                new_dna.insert_values(sq_id, name, seq)
                print(dna_item.assignment(new_dna))
        except ValueError:
            print("Args not valid")
            return False
