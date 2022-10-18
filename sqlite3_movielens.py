# SELECT * FROM sqlite_master where type='table'; <= sqlite의 db에서 table명들을 확인해준다.

# (1). 우선 db를 만들어줘야 해요. 일종의 정보를 담는 껍떼기라고 생각하면 됩니당.
import sqlite3
from sqlite3 import Error

try:
    con = sqlite3.connect('C:/Users/Daniel Hanjoo Rhee/.spyder-py3/SpyderProjects/sqlite3_db/movielens_db.db')
    print("DB created in memory")
except Error:
    print(Error)
finally:
    con.close()
    
    
# (2). 그 다음에는 db에 담고싶은 csv 파일을 읽어와요.
import pandas as pd

pd.options.display.max_rows = 60
pd.options.display.max_columns = 20

df = pd.read_csv('C:/Users/Daniel Hanjoo Rhee/Desktop/Growth Hackers/RippleAI/data/movie_lens/sample_movies100.csv')

# (3). con이라는 변수로 sqlite3을 (1)에서 만든 껍데기 db와 연결시켜줘요
con = sqlite3.connect('C:/Users/Daniel Hanjoo Rhee/.spyder-py3/SpyderProjects/sqlite3_db/movielens_db.db')

# (4). df.to_sql이라는 함수로 앞에서 읽어온 데이터프레임 변수를 db안에 넣어줘요. 'movies'은 테이블 이름입니당!
df.to_sql('movies',con,if_exists='replace')


# (5). stmt 안에는 sql 명령문을 넣어주고요.
stmt = '''
SELECT * FROM movies;
'''

# (6). 데이터베이스와 sqlite3을 연결해요.
conn = sqlite3.connect('C:/Users/Daniel Hanjoo Rhee/.spyder-py3/SpyderProjects/sqlite3_db/movielens_db.db')

# (7) 그리고 데이터베이스에 들어 있는 테이블의 데이터를 판다스의 데이터프레임으로 가져와요.
try:
    df = pd.read_sql(stmt, conn)
except sqlite3.Error as err:
    print('SQLite ERROR:', err)
else: 
    print(df)
finally:  
    conn.close() 