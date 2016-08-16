import webbrowser
import os
import sys
import subprocess 

class CommandManager:
    def __init__(self):
        self.command_actions = {"commands": self.list_commands,
        "pandora": pandora, "gmail": gmail, "drive": drive,
        "chess": chess, "google": google, "setup": setup,
        "python": python, "terminal": terminal}

    def manageCommand(self, commandName):
        self.command_actions[commandName]()
        print("EZ mon$y! What else can I do for you?")

    def list_commands(self):
        commands = [command for command in self.command_actions.keys]
        print(str(commands))


# Internet stuff
def open_website(url):
    protocol = 'http://'
    full_url = protocol + url
    webbrowser.open_new(full_url)

def pandora():
    open_website("pandora.com")

def gmail():
    open_website("mail.google.com")

def drive():
    open_website("drive.google.com")

def chess():
    open_website("chess.com")

def google():
    open_website("google.com")

def setup():
    drive()
    google()
    pandora()


# Programming stuff
def python():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/Google\ Drive/Software/Python'])

def terminal():
    subprocess.Popen(['/bin/sh', '-c', 'open -a terminal ~/'])

