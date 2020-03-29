#!/usr/bin/python3
""" sql """
if __name__ == "__main__":
    import MySQLdb
    import sys
    query = """SELECT id, name FROM states
    WHERE name = '{}' ORDER BY id""".format(sys.argv[4])
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute(query)
    states = c.fetchall()
    for x in states:
        if x[1] == 'Arizona':
            print(x)
