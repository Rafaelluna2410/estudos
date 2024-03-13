class Livro:
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    def __repr__(self):  
        return  self.titulo
    
    def __str__(self): # preferencia pelo __str__ qnd houver __repr__
        return self.titulo
    
    def __len__(self): 
        return self.paginas
    
    def __del__(self):
        return print('livro foi deletado da memoria')
    
    def __add__(self, outro):
        return f'{self} - {outro}'
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg= ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não pode multiplicar'

livro1 = Livro('Python Rocks', 'Geek', 400)
livro2 = Livro(' teste32', 'te', 800)

print(livro1)
print(len(livro1))
print(livro1 + livro2)
print(livro1 * 3)
#del livro1