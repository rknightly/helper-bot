import commandManager
from tkinter import *

class Interface:
    def __init__(self):
        self.manager = commandManager.CommandManager()
        self.manager.set_interface(self)

        self.set_to_default_command_handler()

        self.root = Tk()
        self.root.wm_title('Helper Bot')

        self.text_box = Text(self.root, height=30, width=80)

        self.input_box = Entry(self.root, width=30)

        self.makeGui()

    def set_to_default_command_handler(self):
        self.set_command_handler(self.manager.manage_command)

    def set_command_handler(self, command_handler):
        self.command_handler = command_handler

    def key(self, event):
        if event.char == "\r":
            command = self.input_box.get()
            self.input_box.delete(0, END)

            self.output(command, 'human_text')

            self.command_handler(command)

    def makeGui(self):
        background_color = '#003333'
        inpurt_box_color = '#008888'

        self.root.configure(background=background_color)
        self.root.configure(highlightbackground=background_color)

        self.text_box.configure(state=DISABLED)  # Make it read only
        self.text_box.configure(background=background_color)
        self.text_box.configure(highlightbackground=background_color)
        self.text_box.configure(foreground='#ffffff')
        self.text_box.configure(padx=15, pady=5)

        self.text_box.tag_configure('bot_text', font=('Monaco', 13, 'bold'),
                                    spacing1=5)
        self.text_box.tag_configure('human_text', font=('Monaco', 13,
                                    'italic'), spacing1=5)


        self.text_box.pack()

        self.output("Hello, I am HelperBot, your personal helping robot.")
        self.output("How may I help you?")

        self.input_box.bind("<Key>", self.key)
        self.input_box.config(background=inpurt_box_color)
        self.input_box.configure(highlightbackground=background_color)
        self.input_box.pack(side=BOTTOM)

        mainloop()

    def output_in_line(self, text, tag='bot_text'):
        self.text_box.config(state=NORMAL) # Allow output

        self.text_box.insert(END, text, tag)
        self.text_box.see(END)

        self.text_box.config(state=DISABLED)  # Make it read only

    def output(self, text="", tag='bot_text'):
        self.output_in_line(text + '\n', tag)
