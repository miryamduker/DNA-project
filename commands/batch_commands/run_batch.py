from commands.batch_commands.batch import batch
from commands.command_handler import get_name


class RunBatch:
    def __init__(self, name):
        self.name = get_name(name)

    def execute(self):
        try:
            current_batch = batch.get(self.name)
            for i in range(len(current_batch)):
                current_batch[i].execute()
        except:
            print("Error")