#!/usr/bin/python3

"""
    A script that lists all cities in a state from the database hbtn_0e_0_usa
    Username, password and database name and state are given as user args
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""

    cursor.execute(sql, (sys.argv[4],))

    data = cursor.fetchall()

    print(", ".join([city[0] for city in data]))

    cursor.close()
    db.close()
