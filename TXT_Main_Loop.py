#what this program is doing?

#not all needed here but its only Temporary
# Import the required libraries
from asyncio import events
from asyncore import loop
from cProfile import label
import datetime    #import for times and data minupaltions
from distutils import command
from tkinter import * #import for gui and data minupaltions
from tkinter import ttk #import for gui and data minupaltions
from tkinter import messagebox #for notification in order
import winsound #for sound in order 
import time 
#from pyparsing import sys
from winotify import Notification,audio #for notification and sound parallel
import os
import sys


#my files -importing my functions

import TXT_Functions
import TXT_Vars_Functions



TXT_Functions.intializingVariables()

###loop all the time lisning to a event
#its nesserly for 
TXT_Functions.loop_of_lisning()



#TXT_Functions.mainCategoryShowList()


TXT_Vars_Functions.win.mainloop()