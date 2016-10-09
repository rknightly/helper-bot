import webbrowser

from Action import Action

class WebAction(Action):
    @staticmethod
    def open_website(url):
        protocol = 'http://'
        full_url = protocol + url
        webbrowser.open_new(full_url)

# Command Actions
class Pandora(WebAction):
    aliases = ["pandora"]

    @staticmethod
    def do_action():
        WebAction.open_website("pandora.com")


class Gmail(WebAction):
    aliases = ["gmail"]

    @staticmethod
    def do_action():
        WebAction.open_website("mail.google.com")

class Drive(WebAction):
    aliases = ["drive"]

    @staticmethod
    def do_action():
        WebAction.open_website("drive.google.com")

class Chess(WebAction):
    aliases = ["chess"]

    @staticmethod
    def do_action():
        WebAction.open_website("chess.com")

class Google():
    aliases = ["google"]

    @staticmethod
    def do_action():
        WebAction.open_website("google.com")

class Quora():
    aliases = ["quora"]

    @staticmethod
    def do_action():
        WebAction.open_website("quora.com")

class Duolingo():
    aliases = ["duolingo"]

    @staticmethod
    def do_action():
        WebAction.open_website("duolingo")

class Setup():
    aliases = ["setup"]

    @staticmethod
    def do_action():
        Drive.do_action()
        Google.do_action()
        Pandora.do_action()

class SpanishtTextbook():
    aliases = ["SpanishtTextbook"]

    @staticmethod
    def do_action():
        WebAction.open_website("pearsonsuccessnet.com")
