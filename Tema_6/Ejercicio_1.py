class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return('Vehiculo color'+ self.color +', ' + str(self.ruedas) + ' ruedas, ' + str(self.puertas) + ' puertas.')

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return('Coche color '+ self.color +', ' + str(self.ruedas) + ' ruedas, ' + str(self.puertas) + ' puertas, '+ str(self.velocidad) + 'km/h, ' + str(self.cilindrada) + 'cc.')

coche = Coche("negro", 4, 3, 220, 1500)
print(coche)
