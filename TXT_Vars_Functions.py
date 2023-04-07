#importing systimg and librarys
#import pyodbc

from ftplib import error_temp
from tkinter import messagebox
from turtle import update


#importing my database functions
import TXT_Ms_DataBase_Debug
import TXT_Ms_DataBase_Delete
import TXT_Ms_DataBase_Insert
import TXT_Ms_DataBase_Edit
import TXT_Ms_DataBase_Select

#importing my error_handling functions
from TXT_Error_Handling import errorMessagebox
from TXT_Error_Handling import attentionMessagebox
from TXT_Container_Handling  import IsThisCategoryInList



#defining global Variables
win=None
#buttons


errorType=0

filePath=None


backButton=None


#this class is between the gui and database
class CategoryList:
    isMainCategory=None

    #list of name and ids
    last_list_name=[]
    last_list_Ids=[]
    listNames=[]
    listIds=[]
    #all about Gui
    textLabel=None #top text what category is
    buttonAddNewCategory=None
    buttonDeleteCategory=None
    buttonEditCategory=None
    entaryText=None #entary text gui
    fromUserText=None #user entered text
    
    #all about list box itration/object changes
    ListBox=None
    ListBoxCurrentIndex=0
    listboxSelectedItemName=None
    listboxSelectedItemId=None
    listBoxBack=None

    #---functions----
    addNewCategory=None
    editCategory=None
    deleteCategory=None

    #gets from data base all the main categoryes
    getCategoryList=None
    #show all the main categoryes
    pass

#function for mainCategory to insert new main category to a database
def addNewCategory(self,categoryName,parentId):
    #print("func:mainCategory:addNewCategory")
    # string not in the list
    categoryListFromDataBase=getCategoryList(parentId)

    #if the string categoryName that we get from entary box is empty we
    #trow message and not saving
    if categoryName=="":
        attentionMessagebox(2)
        return

    if categoryName in categoryListFromDataBase:
        attentionMessagebox(1)
        return


    errorType=TXT_Ms_DataBase_Insert.addNewCategory(filePath,categoryName,parentId)
    if (errorType!=0):
        errorMessagebox(errorType)
        return

      
    pass


#function to get all the main categorys
def getCategoryList(parentId):
    category_list_names=[]
    category_list_ids=[] ###not in use
    category_list_names,category_list_ids,errorType=TXT_Ms_DataBase_Select.select_category_list_by_id(filePath,parentId)
    return category_list_names
    pass


def editCategory(self,categoryBefore,categoryAfter,categoryId):
    errorType=TXT_Ms_DataBase_Edit.editCategory(filePath,categoryBefore,categoryAfter,categoryId)
    if errorType!=0:
        errorMessagebox(errorType)
        return
    pass


def deleteCategory(self,categoryName,parentId):
    CategoryList.listNames=getCategoryList(0)

    if CategoryList.listboxSelectedItemName=="":
        attentionMessagebox(2)
        return

    return TXT_Ms_DataBase_Delete.deleteFromCategory(filePath,categoryName,parentId)
    pass



    pass


#assigengs the functions to CategoryList class functions that the way i find it works 
CategoryList.getCategoryList=getCategoryList
CategoryList.addNewCategory=addNewCategory
CategoryList.editCategory=editCategory
CategoryList.deleteCategory=deleteCategory





