#!/usr/bin/python3

""" 
This module is used to connect to a MySQL database (hbtn_0e_0_usa)
and prints all states sorted by state ID
"""


import MySQLdb
import sys

def main():
    """ 
    Main function that connects to database, and prints.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()