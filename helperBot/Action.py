class Action:
    """A general action that contains the function it calls, helper functions,
    and the aliases which can be called for that function."""

    aliases = []    # List of aliases that can be called for this action

    @staticmethod
    def do_action(self):
        """The main action that will be preformed."""
        pass
