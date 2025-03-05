#!/usr/bin/python3
"""
This script lists states who matches the user input
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    state_name = sys.argv[4]

    cur = db.cursor()

    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC".format(state_name)
    )

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
