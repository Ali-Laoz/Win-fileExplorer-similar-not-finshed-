import pyodbc

def deleteFromCategory(filePath,categoryName,parent_Id):
    error_type=0
 #   print("DeleteFromCategory")
    try:
        error_type=1
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};',DBQ=filePath)
        cursor = conn.cursor()
    
        error_type=2
        sql = 'DELETE FROM Table1 WHERE CATEGORTY_NAME=? AND PARENT_ID=?'
    
        cursor.execute(sql, (categoryName,parent_Id))
        conn.commit()
        print("Data deleted")

        error_type=0
        return error_type
    except:
        print("Problem")
        return error_type 
    pass