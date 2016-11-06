from action import Action   # For the list commands action below

from onlineActions import *
from offlineActions import *
from mixedActions import *


class CommandManager:
    def __init__(self):
        self.general_actions = [ListCommands]

        self.online_actions = [Search, Pandora, Gmail, Drive, Chess, Google,
                               Quora, Duolingo, Setup, SpanishTextbook]

        self.offline_actions = [Python, Terminal, SameTerminal, SpanishWarmup]

        self.mixed_actions = [Spanish]

        self.actions = self.general_actions + self.online_actions +\
            self.offline_actions + self.mixed_actions

        # Change the list to contain objects instead of classes
        self.actions = [action() for action in self.actions]


    def set_interface(self, interface):
        self.interface = interface
        # Set the interface in all of the actions
        for action in self.actions:
            action.set_interface(self.interface)

    def manageCommand(self, command_name):
        """Run the command if it exists"""
        # Ignore case of input
        command_name = command_name.lower()

        if self.is_command(command_name):
            self.run_command_action(command_name)
            self.interface.output("EZ mon$y! What else can I do for you?")

        else:
            self.interface.output("I don't know how to do that yet, sorry. "
                  "Type 'commands' for a list of commands")

    def is_command(self, command_name):
        """Return true if the given command is an alias for an action, False
        otherwise"""
        command_exists = False
        for action in self.actions:
            if action.is_alias(command_name):
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
        self.interface.output("============ " + header + " ============")

    def list_commands(self):
        self.interface.output('\n\n')   # Create some space to make it look better

        # Find appropriate padding based on action name lengths
        longest_action_name = 0
        for action in self.actions:
            action_name = action.__class__.__name__
            if len(action_name) > longest_action_name:
                longest_action_name = len(action_name)

        padding = int(longest_action_name * 1.5)

        formatting_string = '%-' + str(padding) + 's %-' + str(padding) + 's'

        self.interface.output(formatting_string %
                              ("ACTIONS", "COMMANDS (case insensitive)"))

        self.print_header("Online Actions")
        for action in self.online_actions:
            actions_string = ', '.join('"' + alias + '"'
                                       for alias in action.aliases)
            self.interface.output(formatting_string % (action.__name__,
                                                       actions_string))
        self.interface.output()

        self.print_header("Offline Actions")
        for action in self.offline_actions:
            actions_string = ', '.join('"' + alias + '"'
                                       for alias in action.aliases)
            self.interface.output(formatting_string % (action.__name__,
                                                       actions_string))
        self.interface.output()

        self.print_header("Mixed Actions")
        for action in self.mixed_actions:
            actions_string = ', '.join('"' + alias + '"'
                                       for alias in action.aliases)
            self.interface.output(formatting_string % (action.__name__,
                                                       actions_string))
        self.interface.output()



# Included list commands class because it references CommandManager
class ListCommands(Action):
    aliases = ["commands", "help"]

    def do_action(self):
        manager = CommandManager()
        manager.set_interface(self.interface)
        manager.list_commands()
