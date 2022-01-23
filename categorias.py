class Categoria:
    secuencia=2
    categorias = [{"codigo":1,"descripcion":"Lacteos"},{"codigo":2,"descripcion":"Bebidas"}]
    def __init__(self,categoria):
        Categoria.secuencia +=1
        self.codigo=Categoria.secuencia
        self.descripcion=categoria
    def mostrar(self):
        print("{} - {}".format(self.codigo,self.descripcion))
        
    def datos(self):
        return [self.codigo,self.descripcion]
    
    def registro(self):
        return {"codigo":self.codigo,"descripcion":self.descripcion}
