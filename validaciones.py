class validaciones1():
    def __init__(self):
        self.con = 0

    def ValidacionesNumeros(self, num):
        if  self.con >= len(num):
            self.con = 0
            return True
        if ord(num[self.con]) >= 47 and ord(num[self.con]) <= 58:
            self.con += 1
            return self.ValidacionesNumeros(num)
        else :
            self.con = 0
            return False
        
    def ValidarLetra(self, dato):
        if ord(dato[0]) >= 65 and ord(dato[0]) <= 90:
            return True
        return False
    
    def validarEntradas(self, dato):
        # if dato == "":
        #     return False
        # if len(dato) == 2:
        #     return True
        # else:
        #    return False
        if len(dato) == 2:
            return True
        
        return False

