from onlineActions import *
from offlineActions import *
from mixedActions import *

class CommandManager:
    def __init__(self):
        general_commands = {"commands": self.list_commands}

        online_commands = {"pandora": pandora, "gmail": gmail, "drive": drive,
                           "chess": chess, "google": google, "setup": setup,
                           "quora": quora, "duolingo": duolingo}

        offline_commands = {"python": python, "terminal": terminal,
                           "same terminal": same_terminal}

        mixed_commands = {"spanish": spanish}

        self.command_actions = {**general_commands, **online_commands,
                         **offline_commands, **mixed_commands}

    def manageCommand(self, command_name):
        if command_name in self.command_actions.keys():
            self.command_actions[command_name]()
            print("EZ mon$y! What else can I do for you?")
        else:
            print("I don't know how to do that yet, sorry. "
                  "Type 'commands' for a list of commands")

    def list_commands(self):
        commands = [command for command in self.command_actions.keys()]
        commands = sorted(commands)
        print(str(commands))
