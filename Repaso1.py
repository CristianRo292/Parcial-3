'''
hacer unprograma que lea nombre, apelido paterno, y apellido materno
en 3 cajas separadas, ademas, leer, dia, mes y años de nacimiento en 3 cajas de texto
separadas.

al preciopnar un bton se agregara al un lis box, el rfc de la persona
ademas, contendra dos botones, para eliminar elemtnos del lisbox mediante pilas o colas

rfc = 
primera letra y priera vocal del primer apellido
pimera letra del segundo apellido
ultimos dos digittos del año
dos digotos del mes
dos digotos del dia
'''
from tkinter import *  # 🪟 Importa todas las clases y funciones de Tkinter / Import all Tkinter classes and functions
from tkinter import messagebox  # 💬 Importa messagebox para mostrar mensajes emergentes / Used for pop-up messages
from validaciones import validaciones1  # ✅ Importa la clase validaciones1 desde otro archivo / Import external validation class

class Principal():  # 🧱 Clase principal de la aplicación / Main class of the application
    def __init__(self):
        self.ventana = Tk()  # 🪟 Crea la ventana principal / Creates the main window
        self.ventana.geometry("450x350")  # 📐 Define tamaño de la ventana / Sets window size
        self.valida = validaciones1()  # 🧩 Crea objeto de validación / Creates validation object

    def inicio(self):
        # 🧍 Campos para ingresar nombre y apellidos / Entry fields for name and surnames
        Label(self.ventana, text = "Nombre").place(x = 3, y = 10)
        self.name = Entry(self.ventana)
        self.name.place(x = 3, y = 50, width= 80)

        Label(self.ventana, text = "Apellido Paterno").place(x = 100, y = 10)
        self.apPaterno = Entry(self.ventana)
        self.apPaterno.place(x = 100, y = 50, width= 80)

        Label(self.ventana, text = "Apellido Materno").place(x = 200, y = 10)
        self.apMaterno = Entry(self.ventana)
        self.apMaterno.place(x = 200, y = 50, width= 80)

        # 📅 Campos para fecha de nacimiento / Fields for birth date
        Label(self.ventana, text = "Dia").place(x = 3, y = 100)
        self.dia = Entry(self.ventana)
        self.dia.place(x = 3, y = 150, width= 80)

        Label(self.ventana, text = "Mes").place(x = 100, y = 100)
        self.mes = Entry(self.ventana)
        self.mes.place(x = 100, y = 150, width= 80)

        Label(self.ventana, text = "Año").place(x = 200, y = 100)
        self.año = Entry(self.ventana)
        self.año.place(x = 200, y = 150, width= 80)

        # 🔘 Botón para agregar y botones de selección de modo / Add button and mode selectors
        Button(self.ventana, text = "Agregar",  command= self.agregar).place(x = 10, y = 190)
        self.modo = StringVar(value="Pilas") # valor predeterminado / default value

        Radiobutton(self.ventana, text = "Pilas", variable= self.modo, value= "Pilas").place(x = 70, y = 195)
        Radiobutton(self.ventana, text = "Colas", variable= self.modo, value= "Colas").place(x = 70, y = 220)

        Button(self.ventana, text = "Eliminar", command= self.eliminar).place(x = 10, y = 220)

        # 📋 Listbox para mostrar los RFC generados / Listbox to display generated RFCs
        self.listVisual = Listbox(
            self.ventana, 
            height = 10,           # ↕️ Altura de la lista / List height
            width = 16,            # ↔️ Ancho de la lista / List width
            bg = "white",          # ⚪ Fondo blanco / White background
            font = ("Helvetica", 12)  # 🔤 Tipo y tamaño de letra / Font type and size
        )
        self.listVisual.place(x = 300, y = 10)  # 📍 Posición del Listbox / Position of the Listbox

        # 🔁 Inicia el ciclo principal de la interfaz / Starts main loop
        self.ventana.mainloop()

    def eliminar(self):
        # 🗑️ Elimina elementos del Listbox según el modo seleccionado / Deletes items using selected mode (stack or queue)

        if self.listVisual.size() <= 0:
            messagebox.showerror("Error", "lita vacía")  # ⚠️ Mensaje si la lista está vacía / Error if list is empty
            return 
        
        if self.modo.get() == "Pilas":
            # 🔁 Último que entra, primero que sale / Last In, First Out (Stack)
            self.listVisual.delete(self.listVisual.size()-1)
        else:
            # 🔁 Primero que entra, primero que sale / First In, First Out (Queue)
            self.listVisual.delete(0)
       

    def agregar(self):
        # ➕ Genera el RFC y lo agrega al Listbox / Generates RFC and adds it to the Listbox
        try:
            nombre = self.name.get().upper()  # 🧍 Convierte nombre a mayúsculas / Converts name to uppercase
            primerApe = self.apPaterno.get().upper()  # 🧓 Apellido paterno en mayúsculas / Paternal surname uppercase
            segundoApe = self.apMaterno.get().upper()  # 👵 Apellido materno en mayúsculas / Maternal surname uppercase
            año = self.año.get()  # 📆 Año de nacimiento / Birth year
            mes = self.mes.get()  # 🗓️ Mes de nacimiento / Birth month
            dia = self.dia.get()  # 📅 Día de nacimiento / Birth day
            est = True  # ✅ Variable de control de validez / Validation flag
            
            # 🧩 Validaciones de campos de texto / Validations for text inputs
            if len(nombre) == 0 or not(self.valida.ValidarLetra(nombre)):
                self.name.delete(0, END)
                est = False

            if len(primerApe) == 0 or not(self.valida.ValidarLetra(primerApe)):
                self.apPaterno.delete(0, END)
                est = False

            if len(segundoApe) == 0 or not(self.valida.ValidarLetra(segundoApe)):
                self.apMaterno.delete(0, END)
                est = False

            # 🔢 Validación del año / Year validation
            if len(año) != 4 or not(self.valida.ValidacionesNumeros(año)):
                self.año.delete(0, END)
                est = False

            elif int(año) > 2025 or int(año) < 1900:
                self.año.delete(0, END)
                est = False

            # 📆 Validación del mes / Month validation
            if self.valida.validaMes(mes):
                if len(mes) == 1:
                    mes = f"0{mes}"  # ➕ Agrega cero inicial / Adds leading zero
            else:
                self.mes.delete(0,END)
                est = False

            # 📅 Validación del día / Day validation
            if self.valida.validaDia(dia, mes):
                if len(dia) == 1:
                    dia = f"0{dia}"  # ➕ Agrega cero inicial / Adds leading zero
            else:
                self.dia.delete(0, END)
                est = False

            # ✅ Si todos los datos son válidos / If all data is valid
            if est:
                # 🧮 Construye el RFC siguiendo la regla / Builds the RFC using the rule
                rfc = f"{self.valida.extraerdatos(primerApe)}{segundoApe[0]}{nombre[0]}{año[2:]}{mes}{dia}"
                self.listVisual.insert(END, rfc.upper())  # 🗒️ Agrega RFC al Listbox / Inserts RFC into the Listbox

                # 🧹 Limpia las cajas de texto / Clears all input fields
                self.name.delete(0, END)
                self.apPaterno.delete(0, END)
                self.apMaterno.delete(0, END)
                self.año.delete(0, END)
                self.mes.delete(0, END)
                self.dia.delete(0, END)
                return 0

            # ⚠️ Mensaje si los datos no son válidos / Error if data invalid
            messagebox.showerror("Error", "Datos no validos")

        except ValueError:
            # ⚠️ Error al detectar campo vacío o formato incorrecto / Error for empty or invalid input
            messagebox.showerror("Error", "Campo vacio")


if __name__ == "__main__":  # 🚀 Punto de inicio del programa / Program entry point
    app = Principal()  # 🧱 Crea instancia de la clase principal / Creates instance of the main class
    app.inicio()  # ▶️ Llama al método inicio / Calls the start method
