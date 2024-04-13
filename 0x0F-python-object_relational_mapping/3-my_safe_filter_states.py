#!/usr/bin/python3
"""SQL Injection"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connecting to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    #getting a cursor
    cur = db.cursor()

    #executing a query
    state_name = argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;", (state_name, ))

    #obtaining query results
    result = cur.fetchall()

    #printing resuts 
    for row in result:
        print(row)

    #close cursor
    cur.close()
    