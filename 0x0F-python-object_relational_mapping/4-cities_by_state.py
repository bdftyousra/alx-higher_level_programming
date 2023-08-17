#!/usr/bin/python3

"""
    A script that lists all cities from the database hbtn_0e_0_usa
    Username, password and database names are given as user args
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

    sql = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""

    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
