#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
