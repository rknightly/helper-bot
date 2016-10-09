import offlineActions
import onlineActions
from action import Action

class Spanish(Action):
    aliases = ["spanish", "esp"]

    @staticmethod
    def do_action():
        onlineActions.SpanishTextbook.do_action()

        offlineActions.SpanishPowerpoint.do_action()
        offlineActions.SpanishWarmup.do_action()    # Call last so that it is in the front
