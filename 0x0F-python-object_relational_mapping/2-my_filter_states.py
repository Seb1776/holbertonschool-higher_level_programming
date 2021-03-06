#!/usr/bin/python3
'''Filter States by Argv'''

from sys import argv
import MySQLdb

if __name__ == '__main__':
    myUser = argv[1]
    myPswd = argv[2]
    myDb = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=myUser, passwd=myPswd, db=myDb, charset="utf8")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name ='{}' ".format(argv[4]))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
