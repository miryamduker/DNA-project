from controllers.commands import get_command
from controllers.batch_commands import get_batch_command


class Controller:
    def __init__(self, command, args):
        self.command_name = command
        self.args = args

    def execute_command(self):
        """
        sets command to be an object from the type of the command name and executes it
        """
        try:
            command = get_command(self.command_name, self.args)
            if command is not None:
                command.execute()
                return
        except:
            command = get_batch_command(self.command_name, self.args)
            if command is not None:
                command.execute()
                return
            else:
                print("Command not found")

