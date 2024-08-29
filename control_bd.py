import sqlite3 as sql
import os
import sys
from datetime import datetime

def resource_path(relative_path):
    """Logica para conseguir la ruta del archivo de la bd"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class BaseDatos():
    @staticmethod
    def CrearBD():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        conn.commit()
        conn.close()

    # Creación de las tablas
    @staticmethod
    def createTablaInv():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Inventario (
                nombre TEXT,
                cantidad REAL,
                medido_en TEXT
            )"""
        )
        conn.commit()
        conn.close()

    @staticmethod
    def createTablaVen():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS NumOrdenes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_orden INTEGER
            )"""
        )
        conn.commit()
        conn.close()

    @staticmethod
    def createTablaPlat():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute( """CREATE TABLE IF NOT EXISTS Pedido (
                    id_orden INTERGER,
                    nombre TEXT,
                    precioUni REAL
                    )
            """)
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS OrdenInfo (
                id_orden INTEGER,
                hora_creacion TEXT,
                hora_validacion TEXT,
                precioTotal REAL,
                FOREIGN KEY(id_orden) REFERENCES NumOrdenes(id)
            )"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Platos (
            nombre TEXT,
            precioUni REAL 
            )"""
        )
        conn.commit()
        conn.close()

    @staticmethod
    def createTablaEdiciones():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Registro (
                fecha TEXT,
                hora TEXT,
                desc TEXT
            )"""
        )
        conn.commit()
        conn.close()

    @staticmethod
    def createTablaPlatoIngredientes():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS PlatoIngredientes (
                plato_nombre TEXT,
                ingrediente_nombre TEXT,
                cantidad REAL,
                PRIMARY KEY (plato_nombre, ingrediente_nombre),
                FOREIGN KEY (plato_nombre) REFERENCES Platos(nombre),
                FOREIGN KEY (ingrediente_nombre) REFERENCES Inventario(nombre)
            )"""
        )
        conn.commit()
        conn.close()

    # Métodos de inventario
    @staticmethod
    def insertarElemento(instruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        
        # Normalizar el nombre
        nombre_normalizado = instruccion[0].capitalize()
        
        datos = f"INSERT INTO Inventario VALUES('{nombre_normalizado}', {instruccion[1]}, '{instruccion[2]}')"
        cursor.execute(datos)
        conn.commit()
        conn.close()

    @staticmethod
    def leerFilas():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "SELECT * FROM Inventario"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores
    
    def leerIngredientes():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "SELECT nombre, medido_en FROM Inventario"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def insertarElementosVarios(listaInstruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "INSERT INTO Inventario VALUES(?, ?, ?)"
        cursor.executemany(datos, listaInstruccion)
        conn.commit()
        conn.close()

    @staticmethod
    def leerEnOrden(field):
        db_path = resource_path("Inventario.db")
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
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Normalizar la pista de búsqueda
        pista_normalizada = pista.capitalize()

        datos = f"SELECT * FROM Inventario WHERE nombre LIKE '{pista_normalizada}%'"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    
    def buscarIngredientes(pista):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"SELECT nombre, medido_en FROM Inventario WHERE nombre LIKE '{pista}%'"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores
        

    @staticmethod
    def buscarEnBdUnic(pista):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        # Normalizar la pista de búsqueda
        pista_normalizada = pista.capitalize()

        datos = f"SELECT * FROM Inventario WHERE nombre = '{pista_normalizada}'"
        cursor.execute(datos)
        valores = cursor.fetchone()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def actualizarBd(instruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"UPDATE Inventario SET cantidad = {instruccion[1]} WHERE nombre = '{instruccion[0]}'"
        cursor.execute(datos)
        conn.commit()
        conn.close()

    @staticmethod
    def borrarBd(instruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"DELETE FROM Inventario WHERE nombre = '{instruccion}'"
        cursor.execute(datos)
        conn.commit()
        conn.close()

    @staticmethod
    def existeEnLaBase(pista):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
    
        # Normalizar la pista de búsqueda
        pista_normalizada = pista.capitalize()
        
        datos = f"SELECT COUNT(*) FROM Inventario WHERE nombre = '{pista_normalizada}'"
        cursor.execute(datos)
        resultado = cursor.fetchone()[0]
        conn.close()
        return resultado > 0

    # Métodos de registros
    @staticmethod
    def guardarEdicion(instruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "INSERT INTO Registro VALUES (?, ?, ?)"
        cursor.execute(datos, (instruccion[0], instruccion[1], instruccion[2]))
        conn.commit()
        conn.close()

    @staticmethod
    def ultimaEd():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "SELECT fecha, hora FROM Registro ORDER BY fecha DESC, hora DESC LIMIT 1"
        cursor.execute(datos)
        resultado = cursor.fetchone()
        conn.commit()
        conn.close()
        if resultado:
            fecha, hora = resultado
            return f"{fecha} {hora}"
        else:
            return ""

    @staticmethod
    def leerRegistros():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "SELECT * FROM Registro ORDER BY hora DESC"
        cursor.execute(datos)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    # Metodos Ventas
    @staticmethod
    def insertarElementoPlatos(instruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"INSERT INTO Platos VALUES('{instruccion[0]}', {instruccion[1]})"
        cursor.execute(datos)
        conn.commit()
        conn.close()

    @staticmethod
    def borrarOrden(instruccion):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        try:
            datos = f"DELETE FROM OrdenInfo WHERE id_orden = ?"
            cursor.execute(datos, (instruccion,))
            conn.commit()
            datos = f"DELETE FROM Pedido WHERE id_orden = ?"
            cursor.execute(datos, (instruccion,))
            conn.commit()
        except sql.Error as e:
            print(f"Error al borrar la orden: {e}")
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def agregarPlatoConIngredientes(plato, precio, ingredientes):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO Platos (nombre, precioUni) VALUES (?, ?)", (plato, precio))
            for ingrediente, cantidad in ingredientes.items():
                cursor.execute(
                    "INSERT INTO PlatoIngredientes (plato_nombre, ingrediente_nombre, cantidad) VALUES (?, ?, ?)",
                    (plato, ingrediente, cantidad)
                )
            conn.commit()
        except sql.Error as e:
            print(f"Error al agregar el plato con ingredientes: {e}")
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def datosOrden(id):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Pedido WHERE id_orden = ? """, id)
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def actualizarVal(num, horaVal):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"""UPDATE OrdenInfo SET hora_validacion = ? WHERE id_orden = ?"""
        cursor.execute(datos, (horaVal, num))
        conn.commit()
        conn.close()

    @staticmethod
    def leerPlatos():
        db = resource_path("Inventario.db")
        conn = sql.connect(db)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Platos""")
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def leerOrdenes():
        db = resource_path("Inventario.db")
        conn = sql.connect(db)
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM OrdenInfo""")
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def buscarEnPlatos(pista):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = "SELECT * FROM Platos WHERE nombre LIKE ?"
        cursor.execute(datos, (f'{pista}%',))
        valores = cursor.fetchall()
        conn.commit()
        conn.close()
        return valores

    @staticmethod
    def existeEnPlatos(pista):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        datos = f"SELECT COUNT(*) FROM Inventario WHERE nombre = '{pista}'"
        cursor.execute(datos)
        resultado = cursor.fetchone()[0]
        conn.close()
        return resultado > 0

    @staticmethod
    def registrarVenta(platos):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        try:
            # Verificar si la tabla NumOrdenes está vacía
            cursor.execute("SELECT COUNT(*) FROM NumOrdenes")
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.execute("DROP TABLE IF EXISTS NumOrdenes")
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS NumOrdenes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero_orden INTEGER
                    )"""
                )
                numero_orden = 1
            else:
                cursor.execute("SELECT MAX(numero_orden) FROM NumOrdenes")
                max_orden = cursor.fetchone()[0]
                numero_orden = max_orden + 1

            # Insertar el nuevo número de orden
            cursor.execute("INSERT INTO NumOrdenes (numero_orden) VALUES (?)", (numero_orden,))
            id_orden = cursor.lastrowid

            # Preparar la lista de platos para insertar en la tabla Pedido
            datos_plato = "INSERT INTO Pedido (id_orden, nombre, precioUni) VALUES (?, ?, ?)"
            lista_platos = []
            for plato in platos:
                # Normalizar el nombre del plato
                nombre_plato = plato.capitalize()

                # Buscar el plato en la base de datos
                cursor.execute("SELECT precioUni FROM Platos WHERE nombre = ?", (nombre_plato,))
                precio_unitario = cursor.fetchone()

                if precio_unitario:
                    lista_platos.append((id_orden, nombre_plato, precio_unitario[0]))
                else:
                    print(f"Error: El plato '{nombre_plato}' no existe en la tabla Platos.")
                    print(nombre_plato,platos)
                    conn.rollback()
                    return


                # Actualizar el inventario restando los ingredientes usados
                cursor.execute("SELECT ingrediente_nombre, cantidad FROM PlatoIngredientes WHERE plato_nombre = ?", (nombre_plato,))
                ingredientes = cursor.fetchall()
                for ingrediente, cantidad in ingredientes:
                    cursor.execute("SELECT cantidad FROM Inventario WHERE nombre = ?", (ingrediente,))
                    inventario = cursor.fetchone()
                    if inventario:
                        nueva_cantidad = inventario[0] - cantidad
                        cursor.execute("UPDATE Inventario SET cantidad = ? WHERE nombre = ?", (nueva_cantidad, ingrediente))
                    else:
                        print(f"Error: El ingrediente '{ingrediente}' no existe en la tabla Inventario.")
                        conn.rollback()
                        return

            # Insertar los platos en la tabla Pedido
            cursor.executemany(datos_plato, lista_platos)
            conn.commit()

        except sql.Error as e:
            print(f"Error al registrar la venta: {e}")
            conn.rollback()
        finally:
            conn.close()


    def obtenerReceta(plato_nombre):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(
                """SELECT pi.ingrediente_nombre, pi.cantidad, i.medido_en 
                   FROM PlatoIngredientes pi
                   JOIN Inventario i ON UPPER(pi.ingrediente_nombre) = UPPER(i.nombre)
                   WHERE UPPER(pi.plato_nombre) = UPPER(?)""",
                (plato_nombre.upper(),)
            )
            receta = cursor.fetchall()
            conn.commit()
        except sql.Error as e:
            print(f"Error al obtener la receta del plato {plato_nombre}: {e}")
            receta = []
        finally:
            conn.close()

        return receta

    def registrarOrden(precioTotal):
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT MAX(numero_orden) FROM NumOrdenes")
            result = cursor.fetchone()
            if result and result[0] is not None:
                id_orden = result[0]
            else:
                id_orden = 0  

            hora = datetime.now()
            hora_creacion = hora.strftime("%H:%M")
            hora_validacion = "N/A"
            ins = f"INSERT INTO OrdenInfo (id_orden, hora_creacion, hora_validacion, precioTotal) VALUES (?, ?, ?, ?)"
            cursor.execute(ins, (id_orden, hora_creacion, hora_validacion, precioTotal))
            conn.commit()
            print(f"Orden registrada exitosamente. ID de orden: {id_orden}")
        except sql.Error as e:
            print(f"Error al registrar la orden: {e}")
            conn.rollback()
        finally:
            conn.close()

    @staticmethod
    def generarTodo():
        BaseDatos.CrearBD()
        BaseDatos.createTablaEdiciones()
        BaseDatos.createTablaInv()
        BaseDatos.createTablaPlat()
        BaseDatos.createTablaVen()
        BaseDatos.createTablaPlatoIngredientes()

    @staticmethod
    def eliminar():
        db_path = resource_path("Inventario.db")
        conn = sql.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS OrdenInfo")
        cursor.execute("DROP TABLE IF EXISTS Inventario")
        cursor.execute("DROP TABLE IF EXISTS Registro")
        cursor.execute("DROP TABLE IF EXISTS Pedido")
        cursor.execute("DROP TABLE IF EXISTS NumOrdenes")
        cursor.execute("DROP TABLE IF EXISTS Platos")
        cursor.execute("DROP TABLE IF EXISTS PlatoIngredientes")
        conn.commit()
        conn.close()