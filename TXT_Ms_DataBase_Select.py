import pyodbc

#this function returning all the categorys that has this id
#returning list of names and by ids
def select_category_list_by_id(filePath,categoryId):
#    print("TXT_Ms_DataBase:Select_all_main_category_by_id:")
    error_type=0
    CategorylistNames=[]
    CategorylistIds=[]

    try:
     #file cannot found or cannot connect to the database   
     error_type=1
     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};',DBQ=filePath)
     cursor = conn.cursor()
     
     error_type=2
     sql = 'SELECT CATEGORY_ID,CATEGORTY_NAME FROM Table1 Where PARENT_ID=? ORDER BY CATEGORY_ID DESC'
     #cannot excute sql quarry 
     cursor.execute(sql, (categoryId,))

     #problem of data that is returned from dataBase of how we treat it
     error_type=3
     for id,name in cursor.fetchall():

         CategorylistNames.append(name)
         CategorylistIds.append(id)

     error_type=0
     return CategorylistNames,CategorylistIds,error_type  
    except:
        return CategorylistNames,CategorylistIds,error_type  


def select_category_parent_by_id(filePath,categoryId):
    #    print("TXT_Ms_DataBase:Select_all_main_category_by_id:")
    error_type=0
    Categorylistnames=[]
    CategorylistIds=[]
    CategoryParentId=0

    try:
     #file cannot found or cannot connect to the database   
     error_type=1
     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};',DBQ=filePath)
     cursor = conn.cursor()
     
     error_type=2
     sql = 'SELECT PARENT_ID,CATEGORTY_NAME FROM Table1 Where CATEGORY_ID=?'
     #cannot excute sql quarry 
     cursor.execute(sql, (categoryId,))

     #problem of data that is returned from dataBase of how we treat it
     error_type=3
     for id,name in cursor.fetchall():
         Categorylistnames.append(name)
         CategorylistIds.append(id)

     if len(CategorylistIds)>0:  
        CategoryParentId=CategorylistIds[0]
     else:
        CategoryParentId=None      
     error_type=0
     return CategoryParentId,error_type  
    except:
        return CategoryParentId,error_type  
    pass

