from asyncio import events
import datetime
from distutils.log import error
from tkinter import * 
from tkinter import ttk

from soupsieve import select


import TXT_Vars_Functions
from TXT_Vars_Functions import CategoryList


import TXT_Ms_DataBase_Debug
import TXT_Ms_DataBase_Select
from TXT_Error_Handling import errorMessagebox
from TXT_Error_Handling import attentionMessagebox

#filepath of the database


mainCategory=CategoryList()
subCategory=CategoryList()


#function intiizing some 
def intializingVariables():
    TXT_Vars_Functions.filePath="C:\My_subjects\Data_TxT.accdb"
#--------intializing variables--------
    TXT_Vars_Functions.win=Tk()
    TXT_Vars_Functions.win.title("TXT managment")
# Set the size of the window
    TXT_Vars_Functions.win.geometry("1300x700")

    ###-----------Main category intilizings-------------------
    # ListBox for main_category
    mainCategory.textLabel =Label(TXT_Vars_Functions.win,text="Main category",relief=FLAT)
    mainCategory.textLabel.place(x=50,y=100)

    mainCategory.ListBox = Listbox(TXT_Vars_Functions.win, width=36, height=24,selectmode=EXTENDED)
    mainCategory.ListBox.configure(exportselection=False)
    mainCategory.ListBox.place(x=50,y=120)
    mainCategory.ListBoxCurrentIndex=1

    ##assinging button to a varible buttonAddNewCategory with the name Add New Item
    mainCategory.buttonAddNewCategory=Button(TXT_Vars_Functions.win, text="Add Folder")
    mainCategory.buttonAddNewCategory.place(x=45,y=530)
    mainCategory.buttonAddNewCategory.bind('<ButtonRelease-1>',addNewMainCategoryCallBack)
    

    mainCategory.buttonEditCategory=Button(TXT_Vars_Functions.win, text="Edit Folder")
    mainCategory.buttonEditCategory.place(x=125,y=530)
    mainCategory.buttonEditCategory.bind('<ButtonRelease-1>',editMainCategoryCallBack)

    mainCategory.buttonDeleteCategory=Button(TXT_Vars_Functions.win, text="Delete Folder")
    mainCategory.buttonDeleteCategory.place(x=200,y=530)
    mainCategory.buttonDeleteCategory.bind('<ButtonRelease-1>',deleteMainCategoryCallBack)


    #entary gui and variable entary 
    mainCategory.fromUserText=StringVar()
    mainCategory.fromUserText.set("")
    mainCategory.entaryText= Entry(TXT_Vars_Functions.win, width=15, font=("Arial",18,""),
                 textvariable=mainCategory.fromUserText)
    mainCategory.entaryText.place(x=50,y=560)


    mainCategory.listNames,mainCategory.listIds,errorType=TXT_Ms_DataBase_Select.select_category_list_by_id(TXT_Vars_Functions.filePath,0)
    if errorType!=0:
        errorMessagebox(errorType)

    mainCategoryShowList()

    ###-----------sub category intilizings-------------------
    # ListBox for main_category
    subCategory.textLabel =Label(TXT_Vars_Functions.win,text="Sub category",relief=FLAT)
    subCategory.textLabel.place(x=400,y=50)

    subCategory.ListBox = Listbox(TXT_Vars_Functions.win, width=36, height=24,selectmode=EXTENDED)
    subCategory.ListBox.configure(exportselection=False)
    subCategory.ListBox.place(x=350,y=120)
    subCategory.ListBoxCurrentIndex=1

    ##assinging button to a varible buttonAddNewCategory with the name Add New Item
    subCategory.buttonAddNewCategory=Button(TXT_Vars_Functions.win, text="Add Folder")
    subCategory.buttonAddNewCategory.place(x=350,y=530)
    subCategory.buttonAddNewCategory.bind('<ButtonRelease-1>',addNewSubCategoryCallBack)

    subCategory.buttonEditCategory=Button(TXT_Vars_Functions.win, text="Edit Folder")
    subCategory.buttonEditCategory.place(x=425,y=530)
    subCategory.buttonEditCategory.bind('<ButtonRelease-1>',editSubCategoryCallBack)

    subCategory.buttonDeleteCategory=Button(TXT_Vars_Functions.win, text="Delete Folder")
    subCategory.buttonDeleteCategory.place(x=500,y=530)
    subCategory.buttonDeleteCategory.bind('<ButtonRelease-1>',deleteSubCategoryCallBack)


    TXT_Vars_Functions.backButton=Button(TXT_Vars_Functions.win, text="back")
    TXT_Vars_Functions.backButton.place(x=400,y=75)
    TXT_Vars_Functions.backButton.bind('<ButtonRelease-1>',subCategoryBackButton)
 

    #entary gui and variable entary 
    subCategory.fromUserText=StringVar()
    subCategory.fromUserText.set("")
    subCategory.entaryText= Entry(TXT_Vars_Functions.win, width=15, font=("Arial",18,""),
                 textvariable=subCategory.fromUserText)
    subCategory.entaryText.place(x=365,y=560)


    pass

#all the time checks if listbox of the mainsubjects is clicks
#and if yes it calls another function
def loop_of_lisning():
    mainCategory.ListBox.bind("<<ListboxSelect>>",mainCategory_print_callback)
    mainCategory.ListBox.bind('<Double-1>', mainCategory_OpenFolder_callback)
    subCategory.ListBox.bind("<<ListboxSelect>>",subCategory_print_callback)
    subCategory.ListBox.bind("<Double-1>",subCategory_OpenFolder_callback)
    pass

#------------Maincategory---------------

###print selected from listbox
def mainCategory_print_selction(listbox):

    selection=listbox.curselection()
    if selection:
        print(f"select item:{listbox.get(selection[0])}")
        mainCategory.listboxSelectedItemName=listbox.get(selection[0])
        selected=mainCategory.listboxSelectedItemName
        mainCategory.fromUserText.set(selected)
    else:
        print("no selected")  
###callback to prient selected from listbox
def mainCategory_print_callback(event):

    mainCategory_print_selction(event.widget)
    pass 

def mainCategory_OpenFolder_callback(event):

    mainCategory_OpenFolder(event.widget)
    pass 

def mainCategory_OpenFolder(listbox):
    selection=listbox.curselection()
    if selection:
        print(f"select item:{listbox.get(selection[0])}")
        mainCategory.listboxSelectedItemName=listbox.get(selection[0])
        selected=mainCategory.listboxSelectedItemName
        mainCategory.fromUserText.set(selected)


        mainCategory.listboxSelectedItemId=getMainSelectionIdByName(selected)
        #print("id:"+str(mainCategory.listboxSelectedItemId))
        subCategory.listNames,subCategory.listIds,errorType=TXT_Ms_DataBase_Select.select_category_list_by_id(TXT_Vars_Functions.filePath,mainCategory.listboxSelectedItemId)
        if errorType!=0:
            errorMessagebox(errorType)
            return
        subCategory.isMainCategory=True    
        subCategoryShowList()
    pass



def addNewMainCategoryCallBack(self):
#    print("func addNewCategoryCallBack")
#    print("Category to add:"+mainCategory.fromUserText.get())
    selected=mainCategory.fromUserText.get()
    mainCategory.addNewCategory(selected,0)
    mainCategory.listNames.append(selected)
    mainCategoryShowList()
    pass

def editMainCategoryCallBack(self):
#    print("func EditCategoryCallBack")
#    print("Category to edit:"+selected)
    text=mainCategory.fromUserText.get()
    selected=mainCategory.listboxSelectedItemName
    if text==selected:
        attentionMessagebox(3)
        return
    
    mainCategory.editCategory(selected,text,0)
    indexforEdit=mainCategory.listNames.index(selected)
    mainCategory.listNames[indexforEdit]=text

    mainCategoryShowList()
    pass

def deleteMainCategoryCallBack(self):
#    print("func DeleteCategoryCallBack")
    selected=mainCategory.listboxSelectedItemName
    errorType=mainCategory.deleteCategory(selected,0)
    if errorType!=0:
        errorMessagebox(errorType)
        return

    mainCategory.listNames.remove(selected)
    mainCategoryShowList()
    pass

def mainCategoryShowList():
    mainCategory.ListBox.delete(0,END)
    mainCategory.ListBoxCurrentIndex=1
    for select in mainCategory.listNames:

      mainCategory.ListBox.insert(mainCategory.ListBoxCurrentIndex, select)
      mainCategory.ListBoxCurrentIndex+=1
    pass


def getMainSelectionIdByName(name):
    indexOfName=0
    for select in mainCategory.listNames:
        if name==select:
            break

        indexOfName+=1

    return mainCategory.listIds[indexOfName]        
    pass


#------------subcategory---------------
def addNewSubCategoryCallBack(self):
    print("func:addNewSubCategoryCallBack")
    selected=subCategory.fromUserText.get()
    if selected=="":
        attentionMessagebox(2)
        return

    if subCategory.isMainCategory==True:
        print("SelectedItemId:"+str(mainCategory.listboxSelectedItemId))
        subCategory.addNewCategory(selected,mainCategory.listboxSelectedItemId)
        
    else:
        print("SelectedItemId:"+str(subCategory.listboxSelectedItemId))
        subCategory.addNewCategory(selected,subCategory.listboxSelectedItemId)
        
    subCategory.listNames.append(selected)
    subCategoryShowList()
    pass

def editSubCategoryCallBack(self):
    print("func:editSubCategoryCallBack")
    text=subCategory.fromUserText.get()
    if text=="":
        print("text is empty")
        attentionMessagebox(2)
        return
    selected=subCategory.listboxSelectedItemName
    if text==selected:
        attentionMessagebox(3)
        return
    if selected=="":
        print("not selected enthing")
        attentionMessagebox(2)
        return
    
    if subCategory.listboxSelectedItemId==None:
        print("subCategory.listboxSelectedItemId=None")
        return

    print("selceted id:"+str(subCategory.listboxSelectedItemId))    
    
    if subCategory.isMainCategory==True:
        subCategory.editCategory(selected,text,mainCategory.listboxSelectedItemId)
    
    else:
        subCategory.editCategory(selected,text,subCategory.listboxSelectedItemId)


    
    indexforEdit=0
    print("part1")
    try:
        indexforEdit=subCategory.listNames.index(selected)
        subCategory.listNames[indexforEdit]=text 
            
    except:
        print("not worked")
        return

    print("subCategory listNames and listIds")
    print(subCategory.listNames)
    print(subCategory.listIds)
    
        
    subCategoryShowList()
    pass

def deleteSubCategoryCallBack(self):
    print("func:deleteSubCategoryCallBack")
    selected=subCategory.listboxSelectedItemName
    if selected=="" or selected==None:
        attentionMessagebox(2)
        return

    print(selected)   

    errorType=subCategory.deleteCategory(selected,mainCategory.listboxSelectedItemId)
    if errorType!=0:
        errorMessagebox(errorType)
        return

    subCategory.listNames.remove(selected)
    subCategoryShowList()
    pass

def subCategoryShowList():
    print("func:subCategoryShowList")
    subCategory.ListBox.delete(0,END)
    subCategory.ListBoxCurrentIndex=1
    for select in subCategory.listNames:

      subCategory.ListBox.insert(subCategory.ListBoxCurrentIndex, select)
      subCategory.ListBoxCurrentIndex+=1

    pass   
###print selected from listbox
def subCategory_print_selction(listbox):
    print("func:subCategory_print_selction")
    selection=listbox.curselection()
    if selection:
        print(f"select item:{listbox.get(selection[0])}")
        subCategory.listboxSelectedItemName=listbox.get(selection[0])
        selected=subCategory.listboxSelectedItemName
        subCategory.fromUserText.set(selected)

    else:
        print("no selected")  
###callback to prient selected from listbox
def subCategory_print_callback(event):
    subCategory_print_selction(event.widget)
    pass

def subCategory_OpenFolder_callback(event):
    subCategory_OpenFolder(event.widget)
    pass

def subCategory_OpenFolder(listbox):
    print("func:subCategory_OpenFolder")
    selection=listbox.curselection()
    if selection:
        print(f"select item:{listbox.get(selection[0])}")
        subCategory.listboxSelectedItemName=listbox.get(selection[0])
        selected=subCategory.listboxSelectedItemName
        subCategory.fromUserText.set(selected)

        ####from here we are handling what we selcted

        subCategory.listboxSelectedItemId=getSubSelectionIdByName(selected)
        #print("id:"+str(subCategory.listboxSelectedItemId))
        if subCategory.listboxSelectedItemId==None:
            print("empty list subCategory.listboxSelectedItemId")
            return


        listNames,listIds,errorType=TXT_Ms_DataBase_Select.select_category_list_by_id(TXT_Vars_Functions.filePath,subCategory.listboxSelectedItemId)
        if errorType!=0:
            errorMessagebox(errorType)
            return


        subCategory.last_list_name=subCategory.listNames
        subCategory.last_list_Ids=subCategory.listIds
        subCategory.listNames=listNames
        subCategory.listIds=listIds

        

        subCategory.isMainCategory=FALSE    
        subCategoryShowList()

        


    else:
        print("no selected")
    pass

#sercheing name in a list if it is exists and return the index of the name
def getSubSelectionIdByName(name):
  
    print("func:getSubSelectionIdByName")
    indexOfName=0

    if len(subCategory.listNames)==0:
        return
    if len(subCategory.listIds)==0:
        return    

    for select in subCategory.listNames:
        if name==select:
            break

        indexOfName+=1

    if indexOfName>=len(subCategory.listIds):
        return None

    else:
        return subCategory.listIds[indexOfName]        
     
    pass



def subCategoryBackButton(self):
    print("func:subCategoryBackButton")
    if len(subCategory.listIds)==0:
        subCategory.listIds=subCategory.last_list_Ids
        subCategory.listNames=subCategory.last_list_name
        if len(subCategory.listIds)==0:
            return
        id,errorType=(TXT_Ms_DataBase_Select.select_category_parent_by_id(TXT_Vars_Functions.filePath,subCategory.listIds[0]))
        subCategory.listboxSelectedItemId=id
        if subCategory.listboxSelectedItemId==0:
            return
    else:
        id,errorType=(TXT_Ms_DataBase_Select.select_category_parent_by_id(TXT_Vars_Functions.filePath,subCategory.listIds[0]))
        subCategory.listboxSelectedItemId=id
        id,errorType=(TXT_Ms_DataBase_Select.select_category_parent_by_id(TXT_Vars_Functions.filePath,id))
        subCategory.listboxSelectedItemId=id
        if subCategory.listboxSelectedItemId==0:
            return

    subCategory.listNames,subCategory.listIds,errorType=TXT_Ms_DataBase_Select.select_category_list_by_id(TXT_Vars_Functions.filePath,subCategory.listboxSelectedItemId)
    subCategoryShowList()
    pass

