from commandManager import CommandManager

class Interface:
    def run():
        manager = CommandManager()
        
        print("Hello, I am HelperBot, your personal helping robot.")
        print("How may I help you?")

        while command != "q":
            command = input()
            manager.manageCommand(command)

