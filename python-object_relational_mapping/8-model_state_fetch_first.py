#!/usr/bin/python3
""" Create a script that list all State objects
    from database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Conection():

    def __init__(self, user, passwd, db):
        """ Consturctor of the class """
        self.user = user
        self.passwd = passwd
        self.db_name = db
        self.conection = None
        self.session = None

    def New_conection(self):
        """ Define a method called conenction
            that return a db conection
        """
        args = ["mysql+mysqldb://{}:{}@localhost/{}",
                self.user,
                self.passwd,
                self.db_name]

        db_c = create_engine(args[0].format(args[1], args[2], args[3]))
        self.conection = db_c

    def New_session(self):
        """ Create a new session"""
        Session = sessionmaker(self.conection)
        self.session = Session()


if __name__ == "__main__":
    BD_Conection = Conection(argv[1], argv[2], argv[3])

    """ Establecer una Conexion """
    BD_Conection.New_conection()
    """ Crear nueva Sesión """
    BD_Conection.New_session()

    """ Consulta a Base de Datos """
    query = BD_Conection.session.query(State).first()

    """ Mostrar en pantalla el resultado """
    if query is None:
        print("Nothing")
    else:
        print("{}: {}".format(query.id, query.name))
