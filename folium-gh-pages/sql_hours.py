import pandas as pd
import pymysql
from sqlalchemy import create_engine

db_data = 'mysql+mysqldb://' + 'root' + ':' + 'bit123' + '@' + 'localhost' + ':3306/' \
       + 'free' + '?charset=utf8mb4'
engine = create_engine(db_data)

columns = [
    'temp',
    'store_name',
    'open_hour',
    'close_hour',
    'weekday'
]

df = pd.read_csv("D:/files/open_hours3.csv")
print(df, type(df))

free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')

cursor = free.cursor(pymysql.cursors.DictCursor)

df.to_sql(name="gupsik_hours",
             con=engine,
             if_exists="append",
             index=False)

sql = "SELECT * FROM `gupsik_hours`"
cursor.execute(sql)