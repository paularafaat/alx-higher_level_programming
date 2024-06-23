#!/usr/bin/python3
""" lists all states matches the searched """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    searched_name = sys.argv[4]
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (searched_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
