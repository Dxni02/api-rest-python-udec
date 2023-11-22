from flask import Blueprint, jsonify, request
# Entities
from models.entities.Vehiculo import Vehiculo
# Models
from models.VehiculoModel import VehiculoModel

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def listar_vehiculos():
    try:
        vehiculos = VehiculoModel.listar_vehiculos()
        return jsonify(vehiculos)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<placa>')
def buscar_vehiculo_id(placa):
    try:
        vehiculo = VehiculoModel.buscar_vehiculo_id(placa)
        if vehiculo != None:
            return jsonify(vehiculo)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/agregar', methods=['POST'])
def agregar_vehiculo():
    try:
        placa = request.json['placa']
        marca = request.json['marca']
        modelo = request.json['modelo']
        color = request.json['color']
        categoria = request.json['categoria']
        vehiculo = Vehiculo(placa, marca, modelo, color, categoria)

        affected_rows = VehiculoModel.agregar_vehiculo(vehiculo)

        if affected_rows == 1:
            return jsonify(vehiculo.placa)
        else:
            return jsonify({'message': "No fue posible agregar un vehiculo a la base de datos"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/editar/<placa>', methods=['PUT'])
def editar_vehiculo(placa):
    try:
        marca = request.json['marca']
        modelo = request.json['modelo']
        color= request.json['color']
        categoria = request.json['categoria']
        vehiculo = Vehiculo(placa, marca, modelo, color, categoria)

        affected_rows = VehiculoModel.editar_vehiculo(vehiculo)

        if affected_rows == 1:
            return jsonify(vehiculo.placa)
        else:
            return jsonify({'message': "No fue posible editar el vehiculo"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/eliminar/<placa>', methods=['DELETE'])
def eliminar_vehiculo(placa):
    try:
        vehiculo = Vehiculo(placa)

        affected_rows = VehiculoModel.eliminar_vehiculo(vehiculo)

        if affected_rows == 1:
            return jsonify(vehiculo.placa)
        else:
            return jsonify({'message': "No fue posible eliminar el vehiculo de la base de datos"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500