import offlineActions
import onlineActions
from action import Action

class Spanish(Action):
    aliases = ["spanish", "esp"]

    @staticmethod
    def do_action():
        onlineActions.spanish_textbook()

        offlineActions.spanish_powerpoint()
        offlineActions.spanish_warmup()    # Call last so that it is in the front
