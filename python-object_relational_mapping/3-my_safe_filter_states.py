#!/usr/bin/python3


"""
This module will print only states where the state
begins with N.
"""

import sys
import MySQLdb


def main():
    """
    Main function. Prints states that begin with N
    """

    if len(sys.argv) > 1:
        u = sys.argv[1]
    else:
        raise ValueError("Missing Username")

    if len(sys.argv) > 2:
        p = sys.argv[2]
    else:
        raise ValueError("Missing Password")

    if len(sys.argv) > 3:
        d = sys.argv[3]
    else:
        raise ValueError("Missing Database")

# Added a condition to display all if search is null
    if len(sys.argv) > 4:
        searchvalue = sys.argv[4]
    else:
        searchvalue = None

    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=p, db=d)

    cursor = db.cursor()

    if searchvalue is None:
        query = "SELECT * FROM states ORDER BY id ASC"
    else:
        query = "SELECT * FROM states WHERE name LIKE %s " \
            "ORDER BY id ASC"
        searchvalue += '%'

    cursor.execute(query, (searchvalue,) if searchvalue else None)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
