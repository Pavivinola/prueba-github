class Disco:
    def __init__(self, autor, titulo, genero):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        
    def descripcion(self):
        return f"El disco {self.titulo} es del artista {self.autor} cuyo género musical es {self.genero}"
    
mi_disco = Disco("Johann Sebastian Bach", "Conciertos de Brandemburgo", "Música Barroca")

print(mi_disco.descripcion())