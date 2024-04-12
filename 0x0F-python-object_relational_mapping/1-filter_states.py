#!/usr/bin/python3
"""a script that lists all states with a 
name starting with N (upper N)"""

if "__name__" == "__main__":
    import MySQLdb
    from sys import argv

    # connecting to MySQL database
    db = MySQLdb.connect(host="localhost",port=3307,user=argv=[1] password=argv[2],database=argv[3])

    #getting a cursor
    cur = db.cursor()

    #executing a query
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC;")

    #obtaining query results
    result = cur.fetchall()

    #printing resuts 
    for row in result:
        print(row)

    #close cursor
    cur.close()
