class Sandwich:
    def __init__(self, pan, precio):
        self.pan = pan
        #ahora viene una variable privada
        self.__precio = precio
    #getter devolver el precio
    def get_precio(self):
        return self.__precio
    
    #setter modificar el precio
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        
        else:
            print("El precio debe ser mayor que 0")



#Método que sera sobreescrito con Polimorfismo

    def descripcion(self):
        return f"Sandwich con pan {self.pan}"





        
        