import json, pymysql

# pip install mysql-connector-python
from mysql.connector import pooling






with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)
# 추가
pool = pooling.MySQLConnectionPool(pool_name="mypool",pool_size=3,**config)
# 

def get_song_list_by_debut(year):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()

    cur = conn.cursor()
    sql ='''SELECT l.name, l.debut, r.title FROM girlgroup AS l JOIN song AS r ON l.hit_song_id = r.sid
	    WHERE l.debut LIKE %s;'''
    cur.execute(sql, (f"{year}%",))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insert_song(params):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()

    cur = conn.cursor()
    sql ="INSERT INTO song VALUES(DEFAULT, %s, %s);"
    cur.execute(sql,params)
    conn.commit()       
    cur.close()
    conn.close
    return None

def insert_girl_group(params):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()

    cur = conn.cursor()
    sql ="INSERT INTO girlgroup VALUES(DEFAULT, %s, %s, %s);"
    cur.execute(sql,params)
    conn.commit()       
    cur.close()
    conn.close
    return None

def get_song_list(num):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()

    cur = conn.cursor()
    sql ='''SELECT title FROM song limit %s;'''
    cur.execute(sql, (num,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_girl_group_list(num):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()

    cur = conn.cursor()
    sql ='''SELECT l.name, l.debut FROM girlgroup AS l limit %s;'''
    cur.execute(sql, (num,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

