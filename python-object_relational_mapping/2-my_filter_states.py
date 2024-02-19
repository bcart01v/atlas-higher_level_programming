#!/usr/bin/python3


"""
This module will print only states where the state
begins with N.
"""

import sys as param
import MySQLdb


def main():
    """
    Main function. Prints states that begin with N
    """

    username = param.argv[1]
    password = param.argv[2]
    databasename = param.argv[3]
# Added a condition to display all if search is null
    if len(param.argv) > 4:
        searchvalue = param.argv[4]
    else:
        searchvalue = None

    db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=databasename
)

    cursor = db.cursor()

    if searchvalue is None:
        query_template = "SELECT * FROM states ORDER BY id ASC"
    else:
        query_template = "SELECT * FROM states WHERE name = '{}' " \
            "ORDER BY id ASC"

    dbsearchvalue = query_template.format(searchvalue)


    cursor.execute(dbsearchvalue)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
