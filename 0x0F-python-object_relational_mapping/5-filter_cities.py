#!/usr/bin/python3
"""Module that lists all cities of a state from the database hbtn_0e_4_usa"""

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
    cur.execute("""SELECT cities.name
                   FROM cities
                   INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (argv[4],))

    # obtaining query results (cities)
    result = cur.fetchall()

    # printing the cities
    cities = [city[0] for city in result]
    print(", ".join(cities))

    # close cursor and connection
    cur.close()
    db.close()
