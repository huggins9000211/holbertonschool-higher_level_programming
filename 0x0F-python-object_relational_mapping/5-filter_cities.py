#!/usr/bin/python3
""" sql """
if __name__ == "__main__":
    import MySQLdb
    import sys
    myList = []
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT c.id, c.name, s.name FROM cities c
    INNER JOIN states s ON c.state_id = s.id
    WHERE s.name = %s ORDER BY c.id""", (sys.argv[4],))
    states = c.fetchall()
    for x in states:
        if x[2] == sys.argv[4]:
            myList.append(x[1])
    print(', '.join(myList))
