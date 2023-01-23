import sqlite3 as sq
import argon2
from geopy import distance

def main():
    print(distance_finder("50.312,34.3155",1))

def create_user_table():
    con = sq.connect("testdb.db")
    cur = con.cursor()   
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        ID integer PRIMARY KEY,
        name text NOT NULL,
        email text NOT NULL,
        phone text NOT NULL,
        password_hash text NOT NULL
    ) """)
    con.close()

def create_stations_table():
    con = sq.connect("testdb.db")
    cur = con.cursor()   
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stations(
        ID integer PRIMARY KEY,
        name text NOT NULL,
        location text NOT NULL,
        type integer NOT NULL 
    ) """)
    con.close()

def add_new_user(name,email,phone,password):
    con = sq.connect("testdb.db")
    cur = con.cursor()  
    hashed_pswd = hashing(password)
    data = (name,email,phone,hashed_pswd)
    cur.execute("INSERT INTO users (name,email,phone,password_hash) VALUES (?,?,?,?)",data)
    con.commit()
    con.close()

def add_new_station(name,location,type):
    con = sq.connect("testdb.db")
    cur = con.cursor()  
    data = (name,location,type)
    cur.execute("INSERT INTO stations (name,location,type) VALUES (?,?,?)",data)
    con.commit()
    con.close()

def hashing(str_password):
    argon2Hasher = argon2.PasswordHasher(time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
    hash = argon2Hasher.hash(str_password)
    str_password = bytes(str_password, "utf-8")
    return hash

def verify(str_email,str_password): 
    argon2Hasher = argon2.PasswordHasher(time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
    con = sq.connect("testdb.db")
    cur = con.cursor()
    cur.execute(f"SELECT password_hash FROM users WHERE email = '{str_email}'")

    try:
        hashed = cur.fetchone()[0]    
        con.close()
    except TypeError: #eger kayitli emaile ait password yoksa False donduruyor
        return False

    try:
        argon2Hasher.verify(hashed,str_password)
        return True
    except argon2.exceptions.VerifyMismatchError: #passwordu yanlis girdiyse yine false donduruyor
        return False

def distance_finder(user_location,station_id):
    con = sq.connect("testdb.db")
    cur = con.cursor()
    cur.execute(f"SELECT location FROM stations WHERE id = '{station_id}'")

    try:
        location = cur.fetchone()[0]
        con.close()
    except TypeError:
        return False    

    user_location = eval(user_location)
    location = eval(location)

    km_dist =str(distance.distance(location,user_location)).split()
    km_dist = "%.2f"%float(km_dist[0])

    return km_dist


if __name__ == "__main__":
    main()