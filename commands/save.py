from functions import get_item


class Save:
    def __init__(self, seq):
        self.__seq = seq

    def execute(self):
        try:
            arg_list = self.__seq.split()
            dna_item = get_item(arg_list[0])
            file_name = ""
            if len(arg_list) < 2:
                file_name = dna_item.get_name()
            elif len(arg_list) == 2:
                file_name = arg_list[1]
            else:
                raise ValueError
            file_name += '.rawdna'
            f = open(file_name, "w")
            f.write(dna_item.get_string())
            f.close()
        except ValueError:
            print("Args not valid")
            return False
        except:
            print("Error")
