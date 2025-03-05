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

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    city_names = ", ".join(row[0] for row in rows)
    print(city_names)

    cur.close()
    conn.close()
