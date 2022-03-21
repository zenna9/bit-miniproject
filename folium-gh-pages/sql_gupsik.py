import pandas as pd
import pymysql
from sqlalchemy import create_engine

db_data = 'mysql+mysqldb://' + 'root' + ':' + 'bit123' + '@' + 'localhost' + ':3306/' \
       + 'free' + '?charset=utf8mb4'
engine = create_engine(db_data)

columns = [
    'temp',
    'store_name',
    'phone',
    'ppl',
    'open_hours',
    'open_days',
    'latitude',
    'longitude',
    'addr',
    'extra_info',
    'siteurl'
]

# stores = open("open_hours3.csv", encoding="utf-8")
df = pd.read_csv("D:/files/seoul_sql.csv")
print(df, type(df))

free = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bit123', db='free', charset='utf8')

cursor = free.cursor(pymysql.cursors.DictCursor)

df.to_sql(name="gupsik",
             con=engine,
             if_exists="append",
             index=False)

sql = "SELECT * FROM `gupsik`"
cursor.execute(sql)