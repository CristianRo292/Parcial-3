from tkinter import *  # 🪟 Importa todas las clases y funciones de Tkinter / Import all Tkinter classes and functions
from tkinter import messagebox  # 💬 Importa messagebox para mostrar mensajes emergentes / Used for pop-up messages
from validaciones import validaciones1  # ✅ Importa la clase validaciones1 desde otro archivo / Import external validation class
import numpy as np  # 🧮 Importa NumPy para manejo de arreglos (aunque no se usa en este ejemplo) / Imports NumPy (not used here)

# 🧱 Clase principal que gestiona toda la interfaz / Main class that manages the entire interface
class Prinicipal():  
    def __init__(self):
        # 🪟 Creación de la ventana principal / Creation of the main window
        self.ven = Tk()  # 🪟 Crea la ventana principal / Creates main window
        self.ven.title("Practica 3")  # 🏷️ Título de la ventana / Sets window title

        self.val = validaciones1()  # 🧩 Crea instancia de la clase de validaciones / Creates an instance of validation class

        # 📏 Configuración de tamaño de la ventana / Set window dimensions
        ancho_ventana = 350
        alto_ventana = 250

        # 📺 Obtiene dimensiones de pantalla / Get screen dimensions
        ancho_pantalla = self.ven.winfo_screenwidth()
        alto_pantalla = self.ven.winfo_screenheight()

        # 📍 Cálculo para centrar ventana en pantalla / Calculate coordinates to center window
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        # 🧭 Aplica posición y tamaño de la ventana / Apply window size and position
        self.ven.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
       

    def inicio(self):
        # 📦 Cajas de texto con placeholders para guiar al usuario / Text boxes with placeholders to guide user input
        
        # 📋 Caja de texto para el nombre / Text box for name
        self.placeholderNom = "Nombre"
        self.nombre = Entry(self.ven, fg="gray")
        self.nombre.insert(0, self.placeholderNom)
        self.nombre.bind("<FocusIn>", self.quitar_placeholderNom)  # 👀 Evento al enfocar / Event when focused
        self.nombre.bind("<FocusOut>", self.poner_placeholder)  # 👀 Evento al salir / Event when unfocused
        # self.nombre.bind("<Return>", self.validarCaja) # accion si presionas enter / Press enter to validate
        self.nombre.place(x=10, y=10, width=100)

        # ☎️ Caja de texto para el teléfono / Text box for phone number
        self.placeholderTel = "Telefono"
        self.telefono = Entry(self.ven, fg="gray")
        self.telefono.insert(0, self.placeholderTel)
        self.telefono.bind("<FocusIn>", self.quitar_placeholderTel)
        self.telefono.bind("<FocusOut>", self.poner_placeholder)
        # self.telefono.bind("<Return>", self.validarCaja)
        self.telefono.place(x=120, y=10, width=100)

        # 🏠 Caja de texto para domicilio / Text box for address
        self.placeholderDom = "Domicilio"
        self.domicilio = Entry(self.ven, fg="gray")
        self.domicilio.insert(0, self.placeholderDom)
        self.domicilio.bind("<FocusIn>", self.quitar_placeholderDom)  # 👀 Detecta si estás dentro / Detect if focused
        self.domicilio.bind("<FocusOut>", self.poner_placeholder)  # 👀 Detecta si saliste / Detect if unfocused
        self.domicilio.bind("<Return>", self.validarCaja)  # 🏃‍♂️ Ejecuta validación al presionar Enter / Run validation on Enter
        self.domicilio.place(x=250, y=10, width=100)

        # ⚧️ Sección para seleccionar el sexo / Section to select gender
        Label(self.ven, text = "Sexo: ").place(x = 10, y = 30)
        self.modo = StringVar(value="F")  # Valor predeterminado Femenino / Default value Female
        Radiobutton(self.ven, text="F", variable=self.modo, value="F").place(x=10,y=50)  # Opción Femenino / Female option
        Radiobutton(self.ven, text="M", variable=self.modo, value="M").place(x=10,y=70)  # Opción Masculino / Male option

        # 📜 Listbox para mostrar los registros / Listbox to display registered people
        self.lista = Listbox(self.ven, height=6, width=35, bg="white",font=("Helvetica", 12))
        self.lista.place(x=10, y=100)

        # 🖱️ Botón para agregar registro / Button to add a record
        Button(self.ven, text = "Agregar", command= self.validarCaja).place(x= 210, y = 60, width = 100, height = 20)

        self.ven.mainloop()  # 🔁 Mantiene la ventana abierta / Keeps the window running


    def agregar(self):
        # 🔹 Método reservado para futuras funciones de agregar / Placeholder for future add function
        pass
        
    def validarCaja(self, event = 0):
        # 🧮 Validación de campos de entrada / Validation of text box data
        if (self.nombre.get() == self.placeholderNom 
            or self.telefono.get() == self.placeholderTel 
            or self.domicilio.get() == self.placeholderDom
            or self.domicilio.get() == ""):

            messagebox.showerror("Error", "Campo vacios")  # ⚠️ Error si hay campos vacíos / Error if any field is empty

        else: 
            # messagebox.showinfo("Ventana", "✋ Hola mundo ✋")
            nombre = self.nombre.get()  # 🧾 Obtiene nombre / Get name
            telefono = self.telefono.get()  # ☎️ Obtiene teléfono / Get phone
            domicilio = self.domicilio.get()  # 🏠 Obtiene domicilio / Get address

            # ✅ Validaciones: letras para nombre y números para teléfono / Validations: letters for name, numbers for phone
            if self.val.ValidarLetra(nombre) and self.val.ValidacionesNumeros(telefono):
                if self.modo.get() == "F":
                    sexo = "Femenino"
                else:
                    sexo = "Masculino"

                # 🧠 Genera una clave combinando datos / Generate a key combining parts of input
                clave = nombre[0] + telefono[0] + domicilio[2:] 
                persona = clave + " - " + nombre + " - " + telefono + " - " + domicilio + " - " + sexo
                
                # 📥 Inserta registro en la lista / Insert record into list
                self.lista.insert(END, persona)

                # 🧹 Limpia campos de texto / Clear input fields
                self.nombre.delete(0, END)
                self.telefono.delete(0, END)
                self.domicilio.delete(0, END)

            # ❌ Si el nombre es válido pero el teléfono no / If name is valid but phone invalid
            elif self.val.ValidarLetra(nombre):
                messagebox.showerror("Erro", "Telefono no valido")
                self.telefono.delete(0, END)

            # ❌ Si el teléfono es válido pero el nombre no / If phone is valid but name invalid
            elif self.val.ValidacionesNumeros(telefono): 
                messagebox.showerror("Erro", "Nombre no valido")
                self.nombre.delete(0, END)
 

    # 🎯 Métodos para gestionar placeholders de entrada / Methods to handle input placeholders
    
    def quitar_placeholderNom(self, event):
        # ✏️ Elimina el texto de ayuda cuando el usuario hace clic / Removes hint text when user clicks
        if self.nombre.get() == self.placeholderNom:
            self.nombre.delete(0, END)
            self.nombre.config(fg="black")
            return 0
           
    def quitar_placeholderTel(self, event):
        if self.telefono.get() == self.placeholderTel:
            self.telefono.delete(0, END)
            self.telefono.config(fg="black")
            return 0
        
    def quitar_placeholderDom(self, event):
        if self.domicilio.get() == self.placeholderDom:
            self.domicilio.delete(0, END)
            self.domicilio.config(fg="black")
            return 0
            

    def poner_placeholder(self, event):
        # 🔁 Restaura texto de ayuda si el campo queda vacío / Restore hint text if field left empty
        if self.nombre.get() == "":
            self.nombre.insert(0, self.placeholderNom)
            self.nombre.config(fg="gray")
        elif self.telefono.get() == "":
            self.telefono.insert(0, self.placeholderTel)
            self.telefono.config(fg="gray")
        elif self.domicilio.get() == "":
            self.domicilio.insert(0, self.placeholderDom)
            self.domicilio.config(fg="gray")


# 🚀 Punto de entrada principal / Main entry point
if __name__ == "__main__":
    app = Prinicipal()  # 🧩 Crea una instancia de la clase / Create an instance of the class
    app.inicio()  # ▶️ Inicia la interfaz gráfica / Start the graphical interface
