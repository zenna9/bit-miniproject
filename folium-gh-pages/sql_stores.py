import pandas as pd
import csv
import pymysql
from sqlalchemy import create_engine

db_data = 'mysql+mysqldb://' + 'root' + ':' + 'bit123' + '@' + 'localhost' + ':3306/' \
       + 'free' + '?charset=utf8mb4'
engine = create_engine(db_data)

columns = [
    'idx',
    'area',
    'name',
    'addr1',
    'addr2',
    'zipcode',
    'open_info',
    'close_info',
    'type',
    'target1_code',
    'target1_etc',
    'target2_code',
    'target2_etc',
    'item_code',
    'item_etc',
    'lat',
    'lng',
    'sup_obj',
    'sup_num',
    'sup_item',
    'storeType',
    'img_src'
]

df = pd.read_csv("D:/files/stores_db_04v.csv")
print(df, type(df))

free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')

cursor = free.cursor(pymysql.cursors.DictCursor)

df.to_sql(name="stores",
             con=engine,
             if_exists="append",
             index=False)

sql = "SELECT * FROM `stores`"
cursor.execute(sql)