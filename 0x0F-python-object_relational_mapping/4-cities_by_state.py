#!/usr/bin/python3
"""Module that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connecting to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # getting a cursor
    cur = db.cursor()

    # executing a query
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON states.id = cities.state_id
                   ORDER BY cities.id ASC""")

    # obtaining query results
    result = cur.fetchall()

    # printing results
    for row in result:
        print(row)

    # close cursor
    cur.close()
    db.close()
