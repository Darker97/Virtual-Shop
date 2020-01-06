import atexit
import BotHelper
import DataLoader
import ApiHelper
import time

def setup():
    # melden beim BotFather
    atexit.register(BotHelper.ConnectToBot("Good Bye"))
    BotHelper.ConnectToBot("Hello")


# --------------------------------------------    
# The Time the Bot waits until next action
waitingTime = 60
Adress = ""

# --------------------------------------------
# start
setup()

while(True):     
    # Collect Data
    Data = DataLoader.CollectData()

    # send Data to API
    ApiHelper.Senddata(Adress, Data)

    # wait & repeat
    time.sleep(waitingTime)
