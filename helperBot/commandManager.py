from Action import Action   # For the list commands action below

from onlineActions import *
from offlineActions import *
from mixedActions import *


class CommandManager:
    def __init__(self):
        self.general_actions = [ListCommands]

        self.online_actions = [Pandora, Gmail, Drive, Chess, Google, Quora, Duolingo,
                          Setup, SpanishtTextbook]

        self.offline_actions = [Python, Terminal, SameTerminal, SpanishWarmup]

        self.mixed_actions = [Spanish]


        self.actions = self.general_actions + self.online_actions +\
                       self.offline_actions + self.mixed_actions

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

    def print_header(self, header):
        print("============ " + header + " ============")

    def list_commands(self):
        print('\n\n')   # Create some space to make it look better

        #Find appropriate padding based on action name lengths
        longest_action_name = 0
        for action in self.actions:
            action_name = action.__name__
            if len(action_name) > longest_action_name:
                longest_action_name = len(action_name)

        padding = int(longest_action_name * 1.5)

        formatting_string = '%-' + str(padding) + 's %-' + str(padding) + 's'


        print(formatting_string % ("ACTIONS", "COMMANDS (case insensitive)"))

        self.print_header("Online Actions")
        for action in self.online_actions:
            actions_string = ', '.join('"' + alias + '"' for alias in action.aliases)
            print(formatting_string % (action.__name__, actions_string))
        print()

        self.print_header("Offline Actions")
        for action in self.offline_actions:
            actions_string = ', '.join('"' + alias + '"' for alias in action.aliases)
            print(formatting_string % (action.__name__, actions_string))
        print()

        self.print_header("Mixed Actions")
        for action in self.mixed_actions:
            actions_string = ', '.join('"' + alias + '"' for alias in action.aliases)
            print(formatting_string % (action.__name__, actions_string))
        print()

# Included list commands class because it references CommandManager
class ListCommands(Action):
    aliases = ["commands", "help"]

    @staticmethod
    def do_action():
        manager = CommandManager()
        manager.list_commands()
