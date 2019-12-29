import atexit

# ------------------------------------------
main()

# ------------------------------------------

# setup for the tool
def setup():
    atexit.register(exit)
    BotStart("Hello")

# Exit function that gets called when the Tool is closed
def exit():
    BotExit("Good Bye")

def BotExit(Nachricht):
    # Beim Bot abmelden

def BotStart(Nachricht):
    # Beim Bot anmelden

# ------------------------------------------


# ------------------------------------------

def main():
    pass

