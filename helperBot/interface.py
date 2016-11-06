import commandManager
from tkinter import *

class Interface:
    def __init__(self):
        self.manager = commandManager.CommandManager()
        self.manager.set_interface(self)

        self.root = Tk()
        self.text_box = Text(self.root, height=25, width=80)

        self.input_box = Entry(self.root, width=30)

        self.makeGui()

    def key(self, event):
        if event.char == "\r":
            command = self.input_box.get()
            self.input_box.delete(0, END)

            self.output(command)

            self.manager.manageCommand(command)

    def makeGui(self):
        self.text_box.config(state=DISABLED)  # Make it read only
        self.text_box.pack()

        self.output("Hello, I am HelperBot, your personal helping robot.")
        self.output("How may I help you?")

        self.input_box.bind("<Key>", self.key)
        self.input_box.pack(side=BOTTOM)

        mainloop()

    def output(self, text=""):
        self.text_box.config(state=NORMAL) # Allow output

        self.text_box.insert(END, text + '\n')
        self.text_box.see(END)

        self.text_box.config(state=DISABLED)  # Make it read only
