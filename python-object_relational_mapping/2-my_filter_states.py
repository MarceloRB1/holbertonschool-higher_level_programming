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

    DataBase_1 = DataBase(Uname, Upasswd, BDname, 3306, "localhost")

    DataBase_1_conection = DataBase_1.DBConection()
    cursor = DataBase_1.Cursor()
    consult = "SELECT * from states "
    consult_2 = "WHERE BINARY name='{}'".format(conection_data[4])
    cursor.execute(consult + consult_2 + " ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:

        print(state)
