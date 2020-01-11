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

waitingTime = 11
Adress = "http://API:5000"

# --------------------------------------------

while(True):     
   
    try:
         # Collect Data
        Data = DataLoader.CollectData(Adress)
        # send Data to API
        ApiHelper.Senddata(Adress, Data)
    except Exception as e:
        print(e)
    

    # wait & repeat
    time.sleep(waitingTime)
