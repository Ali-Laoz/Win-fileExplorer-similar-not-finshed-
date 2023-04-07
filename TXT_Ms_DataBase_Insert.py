import pyodbc

def addNewCategory(filePath,category,categoryId):
    error_type=0
    try:
        #error_type=file error
        error_type=1

        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};',DBQ=filePath)

        cursor = conn.cursor()
       

        parent_id=categoryId

        data_to_insert=(
            (parent_id,category),
        )

        #error_type=insert error
        error_type=2

        cursor.executemany('INSERT INTO Table1 (PARENT_ID,CATEGORTY_NAME) VALUES(?,?)',data_to_insert)
        conn.commit()
        print("Data Inserted") 
        

        
        return 0
    except:
      return error_type  

    pass