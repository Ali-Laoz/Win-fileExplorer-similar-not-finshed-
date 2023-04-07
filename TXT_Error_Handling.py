
#errorType name and numbers
from tkinter import messagebox
#types of error handling error
# 1 is error
# 2 is attnetion
# 3 is otions yes , no massage box



def errorMessagebox(errorType):
    errorDiscraption=""
    if errorType==0:
         return

    elif errorType==1:
         errorDiscraption+="Error 1: File cannot found or cannot connect to the database"
    elif errorType==2:
         errorDiscraption+="Error 2: Cannot excute sql quarry"   
    elif errorType==3:
         errorDiscraption+="Error 3: Problem of data that is returned from dataBase"

    else:
         errorDiscraption+="This error Unown"
 
    messagebox.showinfo("Error",errorDiscraption)    
    pass

def attentionMessagebox(attentionType):
     AttentionDiscraption=""
     if attentionType==1:
         AttentionDiscraption+="There is category with this name"
     elif attentionType==2:
         AttentionDiscraption+="Its empty text"
     elif attentionType==3:
         AttentionDiscraption+="Its the same text not updated"         
     else:
         AttentionDiscraption+="This error is Unown"     

     messagebox.showinfo("Attnetion",AttentionDiscraption)     
     pass


def optionMessagebox(optionType):
     pass

