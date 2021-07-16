from commands.batch_commands.batch import Batch
from commands.batch_commands.listing_batch import ListingBatch
from commands.batch_commands.loading_batch import LoadBatch
from commands.batch_commands.run_batch import RunBatch
from commands.batch_commands.saving_batch import SaveBatch
from commands.batch_commands.showing_batch import ShowingBatch


def get_batch_command(command, args):
    """
    :param command: name of command
    :param args: of the command
    :return: an object from the type of the command name
    """
    batch_commands = {
        "batch": Batch(args),
        "run": RunBatch(args),
        "batchlist": ListingBatch(),
        "batchshow": ShowingBatch(args),
        "batchsave": SaveBatch(args),
        "batchload": LoadBatch(args)
    }
    return batch_commands[command]