from controllers.commands import get_command
from datas.batch_data import batch, str_batch


class Batch:
    def __init__(self, name):
        self.name = name

    def get_batch_by_name(self, name):
        return batch.get(name)

    def execute(self):
        if self.name is None:
            print("Missing batch name")
            return
        try:
            print("> batch >>>", end="")
            batch_input = input().split()
            commands = []
            commands_str = []
            while batch_input[0] != "end":
                commands.append(get_command(batch_input[0], ''.join(batch_input[1:])))
                batch[self.name] = commands
                commands_str.append(' '.join(batch_input))
                str_batch[self.name] = commands_str
                print("> batch >>>", end="")
                batch_input = input().split()
        except:
            print("Error")
