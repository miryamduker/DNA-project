from commands.count import Count
from commands.delete import Delete
from commands.dup import Dup
from commands.find import Find
from commands.find_all import FindAll
from commands.len import Len
from commands.load import Load
from commands.new import New
from commands.replace import Replace
from commands.save import Save
from commands.slice import Slice


class Controller:
    def __init__(self, command, args):
        self.__command = command
        self.__args = args
        self.commands={
            'new':New(self.__args),
            'load': Load(self.__args),
            'dup': Dup(self.__args),
            'slice': Slice(self.__args),
            'replace': Replace(self.__args),
            'save': Save(self.__args),
            'del': Delete(self.__args),
            'find':Find(self.__args),
            'findall': FindAll(self.__args),
            'len': Len(self.__args),
            'count': Count(self.__args)
        }

    def execute_command(self):
        command=self.commands[self.__command]
        if command is not None:
            command.execute()
            return
        else:
            print("Command not found")


