from commands.command_handler import get_name
from datas.batch_data import str_batch


class SaveBatch:
    def __init__(self, args):
        self.args = args

    def execute(self):
        try:
            arg_list = self.args.split()
            file_name = None
            if len(arg_list) == 2:
                file_name = arg_list[1] + '.dnabatch'
            elif len(arg_list) == 1:
                file_name = get_name(arg_list[0])+ '.dnabatch'
            else:
                raise ValueError
            print(file_name)
            f = open(file_name, "w")
            for command in str_batch.get(get_name(arg_list[0])):
                f.write(command+'\n')
            f.close()
        except ValueError:
            print("Args not valid")
            return
        except:
            print("Error")
