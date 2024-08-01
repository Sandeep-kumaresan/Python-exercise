import pandas as pd
import sql_connection as sql
exceldata=pd.read_csv('data.csv',index_col=False,delimiter=',')
#print(exceldata.head())
#sql.create_db()
#sql.create_table(exceldata)
sql.select()