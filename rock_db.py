#!/usr/bin/env python3

import sqlite3
from datetime import datetime


def get_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute("""CREATE TABLE page(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    level INTEGER NOT NULL,
    created_at TEXT NOT NULL)""")

cur.execute("""CREATE TABLE item(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    child INTEGER NULL,
    parent INTEGER NULL,
    created_at TEXT NOT NULL)""")

cur.execute(f"""INSERT INTO page 
    VALUES 
        (NULL, 'main', 0, '{get_now()}'),
        (NULL, 'hotspot', 1, '{get_now()}'),
        (NULL, 'patches', 1, '{get_now()}')""")

cur.execute(f"""INSERT INTO item 
    VALUES
        (NULL, 'hotspot', 2, NULL, '{get_now()}'),
        (NULL, 'patches', 3, NULL, '{get_now()}') 
        """)

con.commit()
con.close()
