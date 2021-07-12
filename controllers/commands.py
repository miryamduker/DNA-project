from commands.analysis_commands.count import Count
from commands.management_commands.delete import Delete
from commands.creation_commands.dup import Dup
from commands.analysis_commands.find import Find
from commands.analysis_commands.find_all import FindAll
from commands.analysis_commands.len import Len
from commands.creation_commands.load import Load
from commands.creation_commands.new import New
from commands.manipulation_commands.replace import Replace
from commands.management_commands.save import Save
from commands.manipulation_commands.slice import Slice


def get_command(command, args):
    commands = {
        'new': New(args),
        'load': Load(args),
        'dup': Dup(args),
        'slice': Slice(args),
        'replace': Replace(args),
        'save': Save(args),
        'del': Delete(args),
        'find': Find(args),
        'findall': FindAll(args),
        'len': Len(args),
        'count': Count(args)
    }
    return commands[command]
