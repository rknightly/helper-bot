import webbrowser

from action import Action


class WebAction(Action):
    @staticmethod
    def open_website(url):
        protocol = 'http://'
        full_url = protocol + url
        webbrowser.open_new(full_url)


class Search(WebAction):
    aliases = ["search", "look up", "lookup"]

    def do_action(self):
        self.interface.output("Alright! What would you like me to search?")
        search_phrase = input("Search: ")
        url = "google.com.tr/search?q=" + search_phrase

        WebAction.open_website(url)


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


class Google(WebAction):
    aliases = ["google"]

    @staticmethod
    def do_action():
        WebAction.open_website("google.com")


class Quora(WebAction):
    aliases = ["quora"]

    @staticmethod
    def do_action():
        WebAction.open_website("quora.com")


class Duolingo(WebAction):
    aliases = ["duolingo"]

    @staticmethod
    def do_action():
        WebAction.open_website("duolingo")


class Setup(WebAction):
    aliases = ["setup"]

    @staticmethod
    def do_action():
        Drive.do_action()
        Google.do_action()
        Pandora.do_action()


class SpanishTextbook(WebAction):
    aliases = ["spanish textbook"]

    @staticmethod
    def do_action():
        WebAction.open_website("pearsonsuccessnet.com")
