import webbrowser

class CommandManager:
    def __init__(self):
        self.command_actions = {"pandora": pandora}

    def manageCommand(self, commandName):
        self.command_actions[commandName]()


def pandora():
    url = "http://pandora.com/"
    webbrowser.open_new(url)
    
