import commandManager
from tkinter import *

class Interface:
    def __init__(self):
        self.keylog = ""
        self.manager = commandManager.CommandManager()
        self.manager.set_interface(self)

        self.root = Tk()
        self.text_box = Text(self.root, height=25, width=80)

        self.makeGui()

    def key(self, event):
        print("pressed", repr(event.char))
        if event.char != "\r":
            self.keylog += event.char

        else:
            self.output()
            self.manager.manageCommand(self.keylog)
            self.keylog = ""



    def makeGui(self):
        self.text_box.bind("<Key>", self.key)

        self.text_box.pack()
        self.output("Hello, I am HelperBot, your personal helping robot.")
        self.output("How may I help you?")

        mainloop()

    def output(self, text=""):
        self.text_box.insert(END, text + '\n')
