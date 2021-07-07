from commands.dup import Dup
from commands.load import Load
from commands.new import New


class Controller:
    def __init__(self, command, args):
        self.__command = command
        self.__args = args

    def execute_command(self):
        command = None
        if self.__command == 'new':
            command = New(self.__args)
        elif self.__command == 'load':
            command = Load(self.__args)
        elif self.__command == 'dup':
            command = Dup(self.__args)
        if command is not None:
            command.execute()
            return
        else:
            print("Command not found")


