# el programa con eventos en la caja de texto / Program with text box events
from tkinter import *  # 🪟 Importa todas las clases y funciones de Tkinter / Imports all classes and functions from Tkinter
from tkinter import messagebox  # 💬 Permite mostrar mensajes emergentes / Allows pop-up messages
from validaciones import validaciones1  # ✅ Importa la clase validaciones1 desde otro archivo / Imports validation class from another file
import numpy as np  # 🔢 Biblioteca usada para cálculos numéricos / Library used for numerical computations

class Principal():  # 🧱 Clase principal que controla la interfaz y la lógica / Main class controlling GUI and logic
    def __init__(self):
        self.val = validaciones1()  # ⚙️ Crea un objeto de validaciones / Creates validation object
        self.ven = Tk()  # 🪟 Crea la ventana principal de la aplicación / Creates main application window
        
        ancho_ventana = 320  # 📏 Define ancho de la ventana / Window width
        alto_ventana = 220  # 📏 Define alto de la ventana / Window height

        # Obtener dimensiones de la pantalla / Get screen dimensions
        ancho_pantalla = self.ven.winfo_screenwidth()  # 🖥️ Ancho total de pantalla / Total screen width
        alto_pantalla = self.ven.winfo_screenheight()  # 🖥️ Alto total de pantalla / Total screen height

        # Calcular posición para centrar / Calculate position to center
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)  # 📐 Posición horizontal centrada / Horizontal centered position
        y = (alto_pantalla // 2) - (alto_ventana // 2)  # 📐 Posición vertical centrada / Vertical centered position

        # Aplicar geometría / Apply geometry
        self.ven.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")  # 📦 Define tamaño y posición de la ventana / Sets window size and position
        self.lis = []  # 📋 Lista para almacenar elementos ingresados / List to store entered elements
        
    def validarCaja(self, event):
        valor = self.dato.get()  # 🔍 Obtiene texto de la caja de entrada / Gets text from entry field
        # if (self.val.ValidarLetra(valor)):
        #     messagebox.showinfo("Correcto", "Si comienza con Mayusculas")
        # else:
        #     messagebox.showinfo("Incorrecto", "No comienza con mayuscula")
        # if (self.val.ValidarNumeros(valor)):
        #     messagebox.showinfo("Correcto", "Si es un numero")
        # else:
        #     messagebox.showerror("Icoorrecto", "No es un numero")

        if (self.val.ValidacionesNumeros(valor)):  # ✅ Comprueba si el valor contiene solo números / Checks if input contains only numbers
            if (self.val.validarEntradas(valor)):  # 🔢 Verifica longitud válida (máx. 2 dígitos) / Validates correct input length (max 2 digits)
                self.lista.insert(self.lista.size()+1, valor)  # ➕ Agrega el valor a la lista visual / Adds value to visual list
                self.dato.delete(0,END)  # 🧹 Limpia la caja de texto / Clears the text box
            else:
                messagebox.showerror("Error", "Solo se permite 2 digitos")  # ⚠️ Mensaje si supera longitud / Error if length exceeds limit
                self.dato.delete(0,END)
        else:
            messagebox.showerror("Error", "No son numeros")  # 🚫 Mensaje si no es numérico / Shows error if input is not numeric
            self.dato.delete(0,END)

        # print(f'La cadena tiene {str(self.val.ValidarEntradas(valor))}')
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')  # 🔁 Actualiza el conteo en la etiqueta / Updates label with element count

    def eliminarDato(self):
        if self.lista.size() <= 0:  # 🚫 Verifica si la lista está vacía / Checks if list is empty
            messagebox.showerror("Error", "La lista esta vacia")
            return
        if self.modo.get() == 'Pilas':  # 🧱 Modo pila: último en entrar, primero en salir / Stack mode: last in, first out
            # ultimo que entra primero que sale / last in, first out
            self.lista.delete(self.lista.size()-1)
        else:  # 🧱 Modo cola: primero en entrar, primero en salir / Queue mode: first in, first out
            # primero que entra primero que sale / first in, first out
            self.lista.delete(0)
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')  # 🔁 Actualiza contador visual / Updates visual counter

    def ordenar(self):
        self.lis = list(self.lista.get(0,END))  # 📦 Convierte elementos del Listbox a una lista / Converts listbox items to Python list
        if len(self.lis) <= 0:
            messagebox.showerror("Error ","Lista vacia")  # ⚠️ Error si no hay elementos / Error if list empty
        else:
            #burbuja / bubble sort
            if self.modo2.get() == 'Burguja':  # 🫧 Selecciona el método de burbuja / Selects bubble sort method
                for i in range(0,len(self.lis)):  # 🔄 Recorre lista varias veces / Loops through list multiple times
                    for x in range(0,len(self.lis)-1):  # 🔄 Compara elementos adyacentes / Compares adjacent elements
                        if self.lis[x] > self.lis[x+1]:  # 📊 Si el elemento actual es mayor, intercambia / Swaps if current element is larger
                            aux = self.lis[x]
                            self.lis[x] = self.lis[x+1]
                            self.lis[x+1] = aux
                print(self.lis)  # 🧾 Muestra lista ordenada en consola / Displays sorted list
                self.lista.delete(0,END)  # 🧹 Limpia lista visual / Clears visual list
                for i in self.lis:
                    self.lista.insert(self.lista.size()+1, i)  # 🔁 Inserta los elementos ordenados / Inserts sorted elements
            else:
                # seleccion / selection sort
                p = 0  # 📍 Índice del valor máximo / Index of maximum value
                for i in range(0,len(self.lis)):
                    aux = int(self.lis[i])  # 🔢 Convierte elemento actual a entero / Converts current element to integer
                    p = i
                    for x in range(i,len(self.lis)):  # 🔄 Recorre sublista restante / Iterates remaining sublist
                        # print(self.lis[x])
                        if aux < int(self.lis[x]):  # 🔍 Si encuentra un valor mayor, lo guarda / Stores larger value found
                            aux = int(self.lis[x])
                            p = x
                    self.lis[p] = self.lis[i]  # 🔁 Intercambia valores / Swaps values
                    self.lis[i] = str(aux)  # 🔢 Convierte de nuevo a cadena / Converts back to string
                print(self.lis)
                self.lista.delete(0,END)  # 🧹 Limpia lista visual / Clears visual list
                for i in self.lis:
                    self.lista.insert(self.lista.size()+1, i)  # 🔁 Inserta valores ordenados / Inserts sorted values

    def quitar_placeholder(self, event):
        if self.dato.get() == self.placeholder:  # 🔍 Verifica si el texto es el placeholder / Checks if text is placeholder
            self.dato.delete(0, END)  # 🧹 Borra texto de guía / Deletes placeholder text
            self.dato.config(fg="black")  # ⚫ Cambia color de texto a negro / Changes text color to black

    def poner_placeholder(self, event):
        if self.dato.get() == "":  # 🔎 Si la caja está vacía / If text box is empty
            self.dato.insert(0, self.placeholder)  # 📝 Restaura texto guía / Restores placeholder text
            self.dato.config(fg="gray")  # 🌫️ Cambia color del texto a gris / Changes text color to gray

    def inicio(self):
        # self.dato = Entry(self.ven,)
        # self.dato.place(x=50, y=10)
        self.nombre = Entry(self.ven)  # 🧩 Campo de texto auxiliar no usado / Auxiliary unused text field
        self.nombre.place(x=1,y=1)
        self.placeholder = "Escribe un número"  # ✍️ Texto guía de la caja / Placeholder text
        self.dato = Entry(self.ven, fg="gray")  # 🎨 Caja de texto principal con color gris / Main text box with gray color
        self.dato.insert(0, self.placeholder)  # 🧠 Inserta texto guía inicial / Inserts initial placeholder
        self.dato.bind("<FocusIn>", self.quitar_placeholder)  # 🖱️ Evento al hacer clic / Event when focus in
        self.dato.bind("<FocusOut>", self.poner_placeholder)  # 💭 Evento al perder foco / Event when focus out
        self.dato.bind("<Return>", self.validarCaja)  # ⏎ Evento al presionar Enter / Event when pressing Enter
        self.dato.place(x=50, y=10, width=100)  # 📍 Posición y tamaño de la caja / Sets text box position and size
        self.modo = StringVar(value="Pilas")  # ⚙️ Variable que almacena el modo de eliminación / Stores removal mode
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=50,y=40)  # 🔘 Botón para modo pila / Radio for stack mode
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=100,y=40)  # 🔘 Botón para modo cola / Radio for queue mode
        Button(self.ven, text="Validar", command=self.validarCaja, width=10).place(x=100,y=90)  # ✅ Botón para validar entrada / Button to validate input
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=100,y=120)  # ❌ Botón para eliminar dato / Button to delete data
        self.modo2 = StringVar(value="Burguja")  # ⚙️ Variable que controla tipo de ordenamiento / Controls sorting method
        Radiobutton(self.ven, text="Burguja", variable=self.modo2, value="Burguja").place(x=50,y=150)  # 🫧 Opción burbuja / Bubble sort option
        Radiobutton(self.ven, text="Seleccion", variable=self.modo2, value="Seleccion").place(x=100,y=150)  # 🔽 Opción selección / Selection sort option
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=100,y=180)  # 📊 Botón para ordenar lista / Button to sort list
        self.label = Label(text="Numero")  # 🏷️ Etiqueta de estado / Status label
        self.label.place(x=5,y=70)
        self.lista = Listbox(self.ven, height=10, width=10, bg="white",font=("Helvetica", 12))  # 📋 Lista visual para mostrar elementos / Visual listbox for elements
        self.lista.place(x=190, y=10)
        self.ven.mainloop()  # 🔁 Inicia el bucle principal de la aplicación / Starts main event loop

if __name__=='__main__':
    app = Principal()  # 🧱 Crea la instancia principal de la clase / Creates main class instance
    app.inicio()  # ▶️ Ejecuta la interfaz gráfica / Runs graphical interface
