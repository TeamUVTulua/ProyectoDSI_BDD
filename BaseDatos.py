# ****** Librerias importadas ******#

import psycopg2
from tkinter import messagebox

# ****** Clase BaseDeDatos  ******#
class BaseDatos:
    def __init__(self):

        # ****** Conexion con la base de datos ******#

        self.conexion = psycopg2.connect(
            host="localhost",
            database="MotoSocios",
            user="postgres",
            password="12345"
        )

        # ****** Comandos ejecutados en la base de datos ******#

        self.cursor = self.conexion.cursor()
        print("conexion exitosa")

    def ObtenerDatos(self, dato):
        self.cursor.execute(dato)
        return self.cursor

    def ObtenerTodosLosdatos(self, dato):
        self.cursor.execute(dato)
        row = self.cursor.fetchall()
        return row

    def crear_cursor(self, dato1, dato2):
        self.cursor.execute(dato1, dato2)
        self.conexion.commit()

    def crear_cursorlogin(self, dato):
        self.cursor.execute(dato)
        self.conexion.commit()

    def cursor_fetchall(self):
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conexion.close()