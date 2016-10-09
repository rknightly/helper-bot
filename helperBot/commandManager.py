from onlineActions import *
from offlineActions import *
from mixedActions import *

class CommandManager:
    """
    def __init__(self):
        general_commands = {"commands": self.list_commands}

        online_commands = {Pandora, "gmail": gmail, "drive": drive,
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
    """

    def __init__(self):
        online_actions = [Pandora, Gmail, Drive, Chess, Google, Quora, Duolingo,
                          Setup, SpanishtTextbook]

        offline_actions = [Python, Terminal, SameTerminal, SpanishWarmup]

        mixed_actions = [Spanish]


        self.actions = online_actions + offline_actions + mixed_actions

    def manageCommand(self, command_name):
        """Run the command if it exists"""
        # Ignore case of input
        command_name = command_name.lower()

        if self.is_command(command_name):
            self.run_command_action(command_name)
            print("EZ mon$y! What else can I do for you?")

        else:
            print("I don't know how to do that yet, sorry. "
                  "Type 'commands' for a list of commands")

    def is_command(self, command_name):
        """Return true if the given command is an alias for an action, False
        otherwise"""
        command_exists = False
        for action in self.actions:
            if command_name in action.aliases:
                command_exists = True
                break
        return command_exists

    def run_command_action(self, command_name):
        """Run the action associated with a command"""
        for action in self.actions:
            if command_name in action.aliases:
                action.do_action()
                break
