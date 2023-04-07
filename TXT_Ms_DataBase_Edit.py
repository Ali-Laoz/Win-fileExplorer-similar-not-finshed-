import pyodbc

def editCategory(filePath,categoryBefore,categoryAfter,categoryId):
    error_type=0
    try:
        #error_type=file error
        error_type=1

        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};',DBQ=filePath)

        cursor = conn.cursor()
       

        parent_id=categoryId

      

        #error_type=insert error
        error_type=2

        #UPDATE Table1
        #SET CATEGORTY_NAME = 'koi'
        #WHERE PARENT_ID = 0 and CATEGORTY_NAME="koki";
        sql='UPDATE Table1 SET CATEGORTY_NAME=? WHERE CATEGORTY_NAME=? AND PARENT_ID=?'
       # cursor.executemany('UPDATE Table1 SET CATEGORTY_NAME=? WHERE CATEGORTY_NAME=? AND PARENT_ID=?')
        cursor.execute(sql, (categoryAfter,categoryBefore,categoryId))
        conn.commit()
        print("Data updated") 
        

        
        return 0
    except:
          return error_type  

    pass