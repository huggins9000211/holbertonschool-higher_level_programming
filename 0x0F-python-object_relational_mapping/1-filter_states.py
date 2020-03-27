#!/usr/bin/python3
""" sql """
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT id, name FROM states 
    WHERE name REGEXP '^[n]' ORDER BY id""")
    states = c.fetchall()
    for x in states:
        print(x)
