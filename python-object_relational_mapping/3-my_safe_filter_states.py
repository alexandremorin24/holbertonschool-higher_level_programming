#!/usr/bin/python3
"""
This script safely lists states who matches the user input
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    state_name = sys.argv[4]

    cur = conn.cursor()

    query = (
        "SELECT * FROM states WHERE name = %s "
        "ORDER BY id ASC"
    )

    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
