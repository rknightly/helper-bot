class Action:
    """A general action that contains the function it calls, helper functions,
    and the aliases which can be called for that function."""

    aliases = []    # List of aliases that can be called for this action

    def set_interface(self, interface):
        self.interface = interface

    def is_alias(self, possible_alias):
        return True if possible_alias in self.aliases else False
        
    @staticmethod
    def do_action(self):
        """The main action that will be preformed."""
        pass
