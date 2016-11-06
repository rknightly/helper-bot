class Action:
    """A general action that contains the function it calls, helper functions,
    and the aliases which can be called for that function."""

    aliases = []    # List of aliases that can be called for this action

    def set_interface(self, interface):
        self.interface = interface

    def is_alias(self, possible_alias):
        return True if possible_alias in self.aliases else False

    def queue_input(self, prompt):
        self.interface.output_in_line(prompt)
        self.interface.set_command_handler(self.input_handler)

    def input_handler(self, input_phrase):
        self.input_action(input_phrase)
        self.interface.set_to_default_command_handler()

    def input_action(self, input_phrase):
        pass

    def action_finished(self):
        self.interface.output("EZ mon$y! What else can I do for you?")

    def action_sequence(self):
        self.do_action()
        self.action_finished()
        
    @staticmethod
    def do_action(self):
        """The main action that will be preformed."""
        pass
