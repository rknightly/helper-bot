import commandManager

def run():
        manager = commandManager.CommandManager()
        
        print("Hello, I am HelperBot, your personal helping robot.")
        print("How may I help you?")

        running = True
        while running:
            command = input()

            if command == "q":
                running = False
                break

            manager.manageCommand(command)

