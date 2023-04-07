import pyodbc
import datetime
import os
import TXT_Ms_DataBase_Delete
import TXT_Ms_DataBase_Insert
import TXT_Ms_DataBase_Edit
import TXT_Ms_DataBase_Select

filePath="C:\My_subjects\Data_TxT.accdb"

def print_all():
    print("we are in function print_all:")
    try:
     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};',DBQ=filePath)
     cursor = conn.cursor()
     cursor.execute('SELECT * FROM Table1')
   
     for row in cursor.fetchall():
         print (row)
    except:
        print("no found")
        return 1      






