import sqlite3 as sql
import os
import sys
from datetime import datetime


def resource_path(relative_path):
    try: #Logica para encontrar la base de datos en el build del programa
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class BaseDatos():
    @staticmethod
    def CrearBd():
        db_path = resource_path("BaseDatos.db")
        conn = sql.connect(db_path)
        conn.commit()
        conn.close()



    #creacion de tablas

    def crearTablaInv():
        db_path = resource_path("BaseDatos.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Inventario (
            nombre TEXT,
            cantidad REAL,
            medido_en TEXT
            )"""
        )
    
    # Metodos de inventario
    @staticmethod
    def insertarElemento(instruccion):
        db_path = resource_path("BaseDatos.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"INSERT INTO Inventario VALUES ('{instruccion[0]}', {instruccion[1]}, '{instruccion[2]}')"
        cursor.execute(datos)
        conn.commit()
        conn.close()

    @staticmethod
    def leerFilas():
        db_path = resource_path("BaseDatos.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos= "SELECT * FROM Inventario"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()

    @staticmethod
    def leerEnOrden(field):
        db_path = resource_path("BaseDatos.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"SELECT * FROM Inventario ORDER BY {field}"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def buscarEnBd(pista):
        db_path = resource_path("BaseDatos.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"SELECT * FROM Inventario WHERE nombre LIKE '{pista}%'"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores
