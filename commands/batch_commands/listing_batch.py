from commands.batch_commands.batch import batch


class ListingBatch:
    def __init__(self):
        pass

    def execute(self):
        try:
            print(list(batch.keys()))
        except:
            print("Error")
