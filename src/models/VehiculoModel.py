from database.db import get_connection
from .entities.Vehiculo import Vehiculo


class VehiculoModel():

#LISTAR VEHICULOS
    @classmethod
    def listar_vehiculos(self):
        try:
            connection = get_connection()
            vehiculos = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT placa, marca, modelo, color, categoria FROM vehiculos")
                resultset = cursor.fetchall()

                for row in resultset:
                    vehiculo = Vehiculo(row[0], row[1], row[2], row[3], row[4])
                    vehiculos.append(vehiculo.to_JSON())

            connection.close()
            return vehiculos
        except Exception as ex:
            raise Exception(ex)

#BUSCAR VEHICULO
    @classmethod
    def buscar_vehiculo_id(self, placa):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT placa, marca, modelo, color, categoria FROM vehiculos WHERE placa = %s", (placa,))
                row = cursor.fetchone()

                vehiculo = None
                if row != None:
                    vehiculo = Vehiculo(row[0], row[1], row[2], row[3], row[4])
                    vehiculo = vehiculo.to_JSON()

            connection.close()
            return vehiculo
        except Exception as ex:
            raise Exception(ex)

#AGREGAR VEHICULO
    @classmethod
    def agregar_vehiculo(self, vehiculo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO vehiculos (placa, marca, modelo, color, categoria) 
                                VALUES (%s, %s, %s, %s, %s)""", (vehiculo.placa, vehiculo.marca, vehiculo.modelo, vehiculo.color, vehiculo.categoria))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

#EDITAR VEHICULO
    @classmethod
    def editar_vehiculo(self, vehiculo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE vehiculos SET marca = %s, modelo = %s, color = %s, categoria = %s 
                                WHERE placa = %s""", (vehiculo.marca, vehiculo.modelo, vehiculo.color, vehiculo.categoria, vehiculo.placa))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

#ELIMINAR VEHICULO
    @classmethod
    def eliminar_vehiculo(self, vehiculo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM vehiculos WHERE placa = %s", (vehiculo.placa,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)