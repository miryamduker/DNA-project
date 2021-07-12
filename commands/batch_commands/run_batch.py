from commands.batch_commands.batch import batch


class RunBatch:
    def __init__(self, name):
        self.name = name

    def execute(self):
        try:
            current_batch = batch.get(self.name)
            for i in range(len(current_batch)):
                current_batch[i].execute()
        except:
            print("Error")