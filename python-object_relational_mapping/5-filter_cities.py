#!/usr/bin/python3
"""
    Module 0-select_states.py
"""
import MySQLdb
import sys


class DataBase:
    """ Create the class DataBase to connect with MySQL """

    def __init__(self, user, passwd, bd, port, host):
        """ The constructor of the class """
        self.user = user
        self.passwd = passwd
        self.bd = bd
        self.port = port
        self.host = host

    def DBConection(self):
        """ Return the conection of the BD"""

        return MySQLdb.connect(
                                host=self.host,
                                port=self.port,
                                user=self.user,
                                passwd=self.passwd,
                                db=self.bd
                              )

    def Cursor(self):
        """ Return the cursor of the db"""

        return self.DBConection().cursor()


if __name__ == '__main__':

    conection_data = sys.argv

    Uname = conection_data[1]
    Upasswd = conection_data[2]
    BDname = conection_data[3]

    input_name = conection_data[4].split(";")

    DataBase_1 = DataBase(Uname, Upasswd, BDname, 3306, "localhost")

    DataBase_1_conection = DataBase_1.DBConection()
    cursor = DataBase_1.Cursor()

    st_1 = "SELECT cities.name FROM states "
    st_2 = "JOIN cities ON cities.state_id = states.id AND "
    st_3 = "states.name = '{}'".format(input_name[0])

    cursor.execute(st_1 + st_2 + st_3)

    states = cursor.fetchall()

    for i in range(0, len(states)):
        if i == len(states) - 1:
            print(states[i][0], end="")
        else:
            print(states[i][0], end=", ")
    print()
