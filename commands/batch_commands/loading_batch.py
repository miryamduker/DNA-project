from commands.command_handler import get_name
from controllers.commands import get_command
from datas.batch_data import str_batch, batch


class LoadBatch:
    def __init__(self, args):
        self.args = args

    def execute(self):
        try:
            arg_list = self.args.split()
            file_name = arg_list[0]
            batch_name = None
            if len(arg_list) == 2:
                batch_name = get_name(arg_list[1])
            elif len(arg_list) == 1:
                batch_name = get_name(arg_list[0]).replace('.dnabatch', "")
            else:
                raise ValueError
            commands = []
            commands_str = []
            print(file_name)
            file = open(file_name, 'r')
            for line in file:
                commands.append(get_command(line[0], line[1:]))
                commands_str.append(line)
            file.close()
            batch[batch_name] = commands
            str_batch[batch_name] = commands_str
        except ValueError:
            print("Args not valid")
            return
        except:
            print("Error")
