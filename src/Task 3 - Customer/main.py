import atexit
from BotHelper import BotHelper
from DataLoader import DataLoader
from ApiHelper import ApiHelper
import time

def setup():
    # melden beim BotFather
    #atexit.register(BotHelper.ConnectToBot("Good Bye"))
    #BotHelper.ConnectToBot("Hello")
    pass

# start
setup()

# --------------------------------------------    
# The Time the Bot waits until next action 

waitingTime = 15
Adress = "http://API:5000"

# --------------------------------------------

while(True):     
    Data = ""
    try:
         # Collect Data
        Data = DataLoader.CollectData(Adress)
    except Exception as e:
        print(e)
    
    # send Data to API
    try:
        # send Data to API
        ApiHelper.Senddata(Adress, Data)
    except Exception as identifier:
        pass

    # wait & repeat
    time.sleep(waitingTime)
