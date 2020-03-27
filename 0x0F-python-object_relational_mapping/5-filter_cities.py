#!/usr/bin/python3
""" sql """
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT c.id, c.name, s.name FROM cities c 
    INNER JOIN states s ON c.state_id = s.id 
    WHERE s.name = %s ORDER BY c.id""", (sys.argv[4],))
    states = c.fetchall()
    for x in states[:-1]:
        print(x[1], end=', ')
    print(states[-1][1])
