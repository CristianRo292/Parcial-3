class validaciones1():  # 🧠 Clase que contiene distintos métodos de validación / Class that holds multiple validation methods
    def __init__(self):
        self.con = 0  # 🔢 Contador interno usado en validaciones recursivas / Internal counter for recursive checks

    def ValidacionesNumeros(self, num):
        # 🔍 Verifica si toda la cadena está compuesta solo por números / Checks if entire string is digits only
        if num.isdigit():
            return True  # ✅ Devuelve True si son solo números / Returns True if only digits
        return False  # ❌ De lo contrario devuelve False / Otherwise returns False
        
    def ValidarLetra(self, dato):
        c = 0  # 🔢 Contador auxiliar / Helper counter
        dato = dato.upper()  # 🔡 Convierte todo a mayúsculas para simplificar validación / Converts all to uppercase
        
        for i in dato:  # 🔁 Recorre cada carácter del texto / Loops through each character
            if not(ord(i) >= 65 and ord(i) <= 90 or ord(i) == 32):  # 🔠 Solo se permiten letras (A-Z) y espacios / Only letters and spaces allowed
                return False  # ❌ Devuelve False si encuentra un carácter no permitido / Returns False if invalid char
        return True  # ✅ Si pasa todas las comprobaciones, es válido / Returns True if all chars are valid
    
    def validarLetrasrRecursivo(self, dato, con = 0):
        # 🔄 Versión recursiva para validar letras / Recursive version for letter validation
        if con >= len(dato):  # 📏 Caso base: si ya recorrió toda la cadena / Base case: end of string
            return True
        
        if ord(dato[con].upper()) >= 65 and ord(dato[con].upper()) <= 90 or ord(dato[con].upper()) == 32:
            con += 1  # ➕ Avanza al siguiente carácter / Move to next character
            return self.validarLetrasrRecursivo(dato, con)  # 🔁 Llamada recursiva / Recursive call

        return False  # ❌ Si encuentra un carácter no válido, retorna False / Invalid char found
        
    def validarEntradas(self, dato):
        # 📏 Verifica que la longitud del dato sea exactamente 2 / Ensures input has exactly two characters
        if len(dato) == 2:
            return True  # ✅ Válido si tiene dos caracteres / Valid if two characters
        return False  # ❌ De lo contrario, inválido / Otherwise invalid

    def extraerdatos(self, dato):
        # ✂️ Extrae una combinación de letras (por ejemplo, para generar iniciales) / Extracts letters (e.g., initials)
        c = 0 
        dato = dato.upper()  # 🔡 Convierte el texto a mayúsculas / Converts text to uppercase
        dat = ""  # 📦 Variable donde se guardará el resultado / Stores extracted result
        
        if " " in dato:  # 🔍 Si hay espacios, toma la última palabra / If there are spaces, take the last word
            tem = dato.split(" ")
            dato = tem[len(tem)-1]
        
        ctem = 0  # 🔢 Contador temporal / Temporary counter
        for i in dato:
            if c >= 1:
                if  i in ["A","E","I","O","U"]:  # 🗣️ Busca la primera vocal después de la inicial / Finds first vowel after initial
                    dat += i
                    c += 1
                elif ctem == len(dato) - 1:  # 📍 Si no hay vocal, usa la segunda letra / If no vowel found, use second letter
                    dat += dato[1]
            else:
                dat += i  # 🅰️ Agrega la primera letra / Adds first letter
                c += 1
            if c >= 2:
                break  # 🛑 Detiene cuando ya tiene dos letras / Stops after two letters
            ctem += 1
        return dat  # 🔁 Devuelve el resultado / Returns result
    
    def validaMes(self, mes):
        # 📅 Valida que el mes esté entre 1 y 12 / Validates month range
        if len(mes) <= 2:  # 🔢 Debe tener máximo 2 dígitos / Must have max 2 digits
            if mes.isdigit():  # 🔍 Debe ser numérico / Must be numeric
                if int(mes) > 0 and int(mes) <= 12:  # 🧮 Rango válido de meses / Valid month range
                    return True
        return False  # ❌ Mes no válido / Invalid month

    def validaDia(self, dia, mes = -1):
        # 📆 Verifica que el día sea válido según el mes / Validates day according to month
        try:
            dia_int = int(dia)  # 🔢 Convierte a entero / Converts to integer
            mes_int = int(mes)

            if mes_int >= 1 and mes_int <= 12:  # ✅ Verifica que el mes sea válido / Checks valid month
                if mes_int in [2,4,6,9,11]:  # 📋 Meses con 30 o menos días / Months with ≤ 30 days
                    if mes_int == 2 and dia_int <= 28:  # 🗓️ Febrero máximo 28 / February up to 28
                        return True
                    elif dia_int <= 30:  # 📅 Abril, junio, septiembre, noviembre hasta 30 / Up to 30
                        return True
                else:
                    if dia_int <= 31:  # 📅 Meses con 31 días / Months with 31 days
                        return True
            return False  # ❌ Día fuera de rango / Day out of range
        except ValueError:
            return False  # ⚠️ Si no se puede convertir a número / If conversion fails, return False
  
