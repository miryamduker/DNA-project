from commands.batch_commands.batch import str_batch


class ShowingBatch:
    def __init__(self, name):
        self.name = name

    def execute(self):
        try:
            for i in str_batch.get(self.name):
                print(i)
        except:
            print("Error")
