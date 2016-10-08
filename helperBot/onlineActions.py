import webbrowser

# Helper functions
def open_website(url):
    protocol = 'http://'
    full_url = protocol + url
    webbrowser.open_new(full_url)

# Command Actions
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

def quora():
    open_website("quora.com")

def duolingo():
    open_website("duolingo")

def setup():
    drive()
    google()
    pandora()
