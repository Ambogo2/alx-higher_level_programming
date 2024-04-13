#!/usr/bin/python3
"""module that connects a script to a database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # connecting to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    #getting a cursor
    cur = db.cursor()

    #executing a query
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")

    #obtaining query results
    rows = cur.fetchall()

    #printing resuts 
    for row in rows:
        print(row)

    #close cursor
    cur.close()

    # close all databases
    db.close()
