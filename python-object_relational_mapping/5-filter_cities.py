#!/usr/bin/python3


"""
This module shows a list of all states and their cities
"""

import sys
import MySQLdb


def main():
    """
    Main function. Prints all cities and states.
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

    if len(sys.argv) > 4:
        searchvalue = sys.argv[4]
    else:
        searchvalue = None


    db = MySQLdb.connect(host="localhost", port=3306, user=u, passwd=p, db=d)

    cursor = db.cursor()

    if searchvalue:
        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (searchvalue,))
    else:
        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities JOIN states ON cities.state_id = states.id " \
                "ORDER BY cities.id ASC"
        cursor.execute(query)

    results = cursor.fetchall()

    if searchvalue:
        city_names = [row[1] for row in results]
        formatted_output = ", ".join(city_names)
        print(formatted_output)

    else:
        for row in results:
            print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
