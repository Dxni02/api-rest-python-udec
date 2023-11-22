class Vehiculo():

    def __init__(self, placa=None, marca=None, modelo=None, color=None, categoria=None) -> None:
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.categoria = categoria

    def to_JSON(self):
        return {
            'placa': self.placa,
            'marca': self.marca,
            'modelo': self.modelo,
            'color': self.color,
            'categoria': self.categoria
        }