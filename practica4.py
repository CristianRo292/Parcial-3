from tkinter import *  # 🪟 Importa todas las clases y funciones de Tkinter / Import all Tkinter classes and functions
from tkinter import messagebox  # 💬 Importa messagebox para mostrar mensajes emergentes / Used for pop-up messages
from tkinter import ttk  # 🎛️ Importa ttk para usar widgets avanzados (Treeview, Scrollbar, etc.) / Imports ttk for advanced widgets
from validaciones import validaciones1  # ✅ Importa la clase validaciones1 desde otro archivo / Import external validation class
import numpy as np  # 🔢 Importa NumPy para operaciones numéricas / Imports NumPy for numeric operations
import random  # 🎲 Importa random para generar números aleatorios / Imports random for generating random numbers

class Prinicipal():  # 🧱 Clase principal del programa / Main class of the program
    def __init__(self):
        self.ven = Tk()  # 🪟 Crea la ventana principal / Creates main window
        self.ven.title("Practica 3")  # 🏷️ Título de la ventana / Sets window title
        self.val = validaciones1()  # 🧩 Crea un objeto de la clase validaciones1 / Creates an instance of validation class
        ancho_ventana  = 500  # 📏 Ancho de la ventana / Window width
        alto_ventana = 300  # 📐 Alto de la ventana / Window height

        # ⚙️ Obtiene el ancho y alto de la pantalla en milímetros / Gets screen width and height in millimeters
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.ven.winfo_screenwidth()
        alto_pantalla = self.ven.winfo_screenheight()

        # Calcular posición para centrar
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        # Aplicar geometría
        self.ven.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        self.cont = 0  # 🔢 Contador para generar claves únicas / Counter for unique IDs
        self.bandera = False  # 🚩 Indica si se está en modo edición / Flag to indicate edit mode
        self.renglon = -1  # 📄 Guarda el índice del renglón seleccionado / Stores selected row index
        self.index = ""  # 🔑 Guarda parte de la clave para edición / Stores partial key for editing
        
    def inicio(self):
        #Caja de texo nombre:
        # 🧍 Campo para capturar el nombre del usuario / Text field to enter user's name
        Label(self.ven, text= "Nombre").place(x = 10, y = 10)
        self.nombre = Entry(self.ven, fg="blue")
        self.nombre.place(x=10, y=30, width=100)

        #caja de texto edad:
        # 🎂 Campo para capturar la edad / Text field to enter age
        Label(self.ven, text= "Edad").place(x = 120, y = 10)
        self.edad = Entry(self.ven, fg="green")
        self.edad.place(x=120, y=30, width=100)

        #Caja de texto domiciolio:
        # 📧 Campo para capturar el correo electrónico / Text field to enter email
        Label(self.ven, text= "Correo").place(x = 250, y = 10)
        self.correo = Entry(self.ven, fg="purple")
        self.correo.place(x=250, y=30, width=100)

        # 🔘 Botones principales del programa / Main control buttons
        Button(self.ven, text = "Agregar", command= self.agregarElemento).place(x= 380, y = 50, width = 100, height = 30)
        Button(self.ven, text = "Eliminar", command= self.eliminar).place(x= 380, y = 90, width = 100, height = 30)
        Button(self.ven, text = "Seleccionar", command= self.seleccionar).place(x= 380, y = 130, width = 100, height = 30)

        # dataGrid:
        # 📋 Crea la tabla (Treeview) con encabezados / Creates data table (Treeview) with headers
        columnas = ("Clave", "Nombre", "Correo", "Edad")
        self.tabla = ttk.Treeview(self.ven, columns = columnas, show= "headings")
        self.tabla.place(x = 10, y = 100, width = 350, heigh = 190)

        # 🔠 Configura encabezados y columnas centradas / Sets up headers and centers columns
        for col in columnas:
            self.tabla.heading(col, text = col)
            self.tabla.column(col, anchor="center", width = 30)

        # 🧭 Barras de desplazamiento vertical y horizontal / Vertical and horizontal scrollbars
        scrolly = ttk.Scrollbar(self.ven, orient = "vertical", command = self.tabla.yview)
        scrollx= ttk.Scrollbar(self.ven, orient = "horizontal", command = self.tabla.xview)
        scrolly.place(x = 360, y = 100, height = 190)
        scrollx.place(x = 10, y = 280, width = 350 )

        # 🔁 Inicia el bucle principal de la interfaz / Starts main event loop
        self.ven.mainloop()

    def seleccionar(self):
        # 🖱️ Obtiene la fila seleccionada en la tabla / Gets selected row in table
        self.renglon = self.tabla.selection()
        
        if self.renglon:
            valores = self.tabla.item(self.renglon, "values")  # 📦 Extrae los valores del renglón / Extracts row values
            # print(valores)
            self.index = valores[0]  # 🔑 Guarda la clave / Stores key value
            self.index = self.index[:len(self.index)-2]  # ✂️ Elimina los últimos dos caracteres / Removes last two characters
            # 📝 Inserta los datos en las cajas de texto / Inserts data back into entry fields
            self.nombre.insert(0,valores[1])
            self.edad.insert(0, valores[3])
            self.correo.insert(0, valores[2])
            self.bandera = True  # 🚩 Activa modo edición / Enables edit mode
            return 0
        
        messagebox.showerror("Error", "Elije un fila")  # ⚠️ Mensaje si no hay selección / Error if no row is selected

    def agregarElemento(self):
        # 🧾 Verifica si los campos están vacíos / Checks if any input fields are empty
        if len(self.nombre.get()) == 0 or len(self.edad.get()) == 0 or len(self.correo.get()) == 0:
            messagebox.showerror("Error", "Campos bacios")  # ⚠️ Muestra error si hay campos vacíos / Shows error if empty fields
        else:
            # if self.val.validarLetrasrRecursivo(self.nombre.get()):
            #     print("Eureca funciono")
                
            nombre = self.nombre.get()  # 🧍 Captura nombre / Gets name
            edad = self.edad.get()  # 🎂 Captura edad / Gets age
            correo = self.correo.get()  # 📧 Captura correo / Gets email
            
            if not(self.bandera):  # ➕ Si no está en modo edición / If not in edit mode
                self.cont += 1  # 🔢 Incrementa el contador / Increases counter
                # 🔑 Genera clave única usando contador, número aleatorio y primeras letras del nombre / Generates unique key
                clave = str(self.cont) + str(random.randint(1, 100)) + self.nombre.get()[0:2].upper() 
                self.tabla.insert("", "end", values = (clave, nombre, correo, edad))  # 🧮 Inserta fila en la tabla / Inserts row in table
                
            else:
                # ✏️ Modo edición activado / Edit mode activated
                claveEd = self.index + nombre[:2].upper()
                print("Modo edicion Activado")  # 🖨️ Mensaje en consola / Console message
                # 🔁 Actualiza los valores de la fila seleccionada / Updates selected row data
                self.tabla.item(self.renglon, values = (claveEd, nombre, correo, edad))
                self.bandera = False  # 🚩 Desactiva modo edición / Turns off edit mode
                self.renglon = -1  # 🔄 Reinicia índice / Resets row index
                messagebox.showinfo("Correcto", "Datos Actualizados")  # ✅ Mensaje de éxito / Success message

            # 🧹 Limpia los campos de texto / Clears all entry fields
            self.nombre.delete(0, END)
            self.edad.delete(0, END)
            self.correo.delete(0, END)

    def eliminar(self):
        # ❌ Elimina la fila seleccionada de la tabla / Deletes selected row from table
        self.renglon = self.tabla.selection()
        if self.renglon:
            self.tabla.delete(self.renglon)  # 🗑️ Borra la fila / Deletes the row
            messagebox.showinfo("Correcto", "Correcto, dato eliminado")  # ✅ Confirmación / Success message
            return 0
        messagebox.showerror("Error", "Elije un fila")  # ⚠️ Error si no hay selección / Error if no row selected
    


if __name__ == "__main__":  # 🚀 Punto de entrada del programa / Program entry point
    app = Prinicipal()  # 🧱 Crea instancia de la clase principal / Creates main class instance
    app.inicio()  # ▶️ Llama al método para iniciar la interfaz / Calls method to start interface
