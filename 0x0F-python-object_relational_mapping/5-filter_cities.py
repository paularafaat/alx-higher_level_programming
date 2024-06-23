#!/usr/bin/python3
""" lists all cities """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT cities.name FROM
                cities JOIN states ON states.id = cities.state_id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (state_name,))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))
    cur.close()
    conn.close()
