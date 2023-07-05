import json
from mysql.connector import pooling

with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

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

def get_song_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM song LIMIT %s OFFSET %s;"
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_girl_group_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = """SELECT l.gid, l.name, l.debut, r.title FROM girlgroup as l
                JOIN song AS r ON l.hit_song_id = r.sid
                LIMIT %s OFFSET %s;"""
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insert_song(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO song VALUES(default, %s, %s)"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def insert_girl_group(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO girlgroup VALUES(default, %s, %s, %s)"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def song_update(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "UPDATE song SET `title`=%s,lyrics=%s WHERE sid=%s;"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()
    return None

def song_delete(sid):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM song WHERE sid=%s;"
    cur.execute(sql, (sid,))
    conn.commit()
    cur.close()
    conn.close()
    return None