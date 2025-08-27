class Libro:
    
    def __init__(self, autor, titulo, materia):
        self.autor = autor
        self.titulo = titulo
        self.materia = materia
        
    def descripcion(self):
        return f"{self.autor} es autor del libro {self.titulo} cuya materia es {self.materia}"
    
