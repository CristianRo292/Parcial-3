from tkinter import *  # 🪟 Importa todas las clases y funciones de Tkinter / Import all Tkinter classes and functions
from tkinter import messagebox  # 💬 Importa messagebox para mostrar mensajes emergentes / Used for pop-up messages
from validaciones import validaciones1  # ✅ Importa la clase validaciones1 desde otro archivo / Import external validation class
import numpy as np  # 🧮 Importa NumPy para manejar arreglos numéricos / Imports NumPy for array manipulation

# 🧱 Clase principal del programa / Main class of the program
class Prinicipal():  
    def __init__(self):
        # 🪟 Configuración inicial de la ventana principal / Initial setup of the main window
        self.ven = Tk()  # 🪟 Crea la ventana principal / Creates main window
        self.val = validaciones1()  # 🧩 Crea un objeto de la clase validaciones1 / Creates an instance of validation class
        
        # 📏 Define dimensiones y posición de la ventana / Defines window dimensions and position
        ancho = 320  # ↔️ Ancho de la ventana / Window width
        alto = 250   # ↕️ Alto de la ventana / Window height
        ventana_alto = self.ven.winfo_screenmmwidth()  # 📐 Obtiene ancho de pantalla / Get screen width
        ventana_ancho = self.ven.winfo_screenmmheight()  # 📐 Obtiene alto de pantalla / Get screen height
        x = (ventana_alto // 2) - (ancho // 2)  # 📍 Calcula coordenada X para centrar ventana / Calculate X coordinate
        y = (ventana_ancho // 2) - (alto // 2)  # 📍 Calcula coordenada Y para centrar ventana / Calculate Y coordinate
        self.ven.geometry(f"{ancho}x{alto}+{x + 560}+{y + 200}")  # 📏 Aplica tamaño y posición / Apply window size and position
        
        # self.ven.geometry("320x210")  # 📏 Define tamaño de la ventana / Set window size
        # self.ven.configure(start_position = "center")
        
        self.listaNum = []  # 📋 Lista donde se almacenarán números válidos / List to store valid numbers


    def inicio(self):
        # 🧠 Entrada de texto donde el usuario escribe un dato / Text entry for user input
        self.dato = Entry(self.ven)
        self.dato.place(x = 30, y = 10)  # 📍 Posiciona el cuadro de texto / Places the input field on window

        # ⚙️ Configuración del modo de estructura de datos / Sets the data structure mode
        self.modo = StringVar(value="Pilas") # valor predeterminado / Default value
        Radiobutton(self.ven, text = "Pilas", variable= self.modo, value= "Pilas").place(x = 40, y = 40)  # 📦 Modo pila / Stack mode
        Radiobutton(self.ven, text = "Colas", variable= self.modo, value= "Colas").place(x = 90, y = 40)  # 📬 Modo cola / Queue mode
        
        # ⚖️ Configuración del tipo de ordenamiento / Sets sorting order
        self.tipoDeOrden = StringVar(value = "Men_a_Mayor")
        Radiobutton(self.ven, text = "Asendente", variable= self.tipoDeOrden, value= "Men_a_Mayor").place(x = 9, y = 150)
        Radiobutton(self.ven, text = "Desendente", variable= self.tipoDeOrden, value= "Mayor_a_Men").place(x = 90, y = 150)
        
        # 🖱️ Botones de acción / Action buttons
        Button(self.ven, text= " Validar", command= self.validarCaja, width = 10).place(x = 100, y = 90)  # 🧾 Valida entrada / Validate input
        Button(self.ven, text= " Eliminar", command= self.elimiarDato, width = 10).place(x = 100, y = 120)  # ❌ Elimina un dato / Delete data
        self.label = Label(self.ven, text = "Numero")  # 🏷️ Etiqueta informativa / Informative label
        self.label.place(x = 5, y = 70)
        Button(self.ven, text= "Ordenar", command= self.ordenarDat, width = 10).place(x = 100, y = 190)  # 🔃 Ordena los datos / Sort numbers
        
        # 📜 Listbox para mostrar visualmente los números válidos / Listbox to visually show valid numbers
        self.listVisrual = Listbox(
            self.ven, 
            height = 10,
            width = 10,          # ↔️ Ancho de la lista / Width
            bg = "white",        # ⚪ Fondo blanco / White background
            # activestyle= "dotbox", # 🔲 Estilo al seleccionar / Selection style
            # fg=  "white"         # ⚪ Texto blanco / White text
            font = ("Helvetica", 12)
        )
        self.listVisrual.place(x = 190, y = 10)  # 📍 Posición del Listbox / Place list visually on window

        self.ven.mainloop()  # 🔁 Mantiene la ventana abierta / Keeps the window running until closed


    def ordenarDat(self):
        # 🧮 Método para ordenar los datos del Listbox / Method to sort data from Listbox
        self.listaNum = list(self.listVisrual.get(0, END))  # 📋 Obtiene todos los elementos de la lista / Gets all list elements
        
        if (len(self.listaNum) <= 0):  # 🚫 Verifica que la lista no esté vacía / Check list not empty
            messagebox.showerror("Error", "Lista bacia")  # ⚠️ Mensaje de error si está vacía / Show error message
            return 0
        
        self.arreglo = np.array(self.listaNum)  # 🧩 Convierte la lista en arreglo NumPy / Convert list to NumPy array

        if self.tipoDeOrden.get() == "Men_a_Mayor":
            # 📈 Ordenamiento por método burbuja (ascendente) / Bubble sort (ascending)
            for i in range(0, len(self.arreglo)):
                for x in range(0, len(self.arreglo) - i - 1):
                    if (self.arreglo[x]) > self.arreglo[x +1]:
                        aux = self.arreglo[x]
                        self.arreglo[x] = self.arreglo[x +1]
                        self.arreglo[x +1] = aux
        else:
            # 📉 Ordenamiento por selección (descendente) / Selection sort (descending)
            pos = 0
            for i in range(0,len(self.arreglo)):
                pos = i
                aux = int(self.arreglo[i])

                for x in range(i, len(self.arreglo)):
                    if aux < int(self.arreglo[x]):
                        aux = int (self.arreglo[x])
                        pos = x
                self.arreglo[pos] = self.arreglo[i]
                self.arreglo[i] = str(aux)

        print(self.arreglo)  # 🖨️ Imprime el arreglo ordenado / Print sorted array
        self.listVisrual.delete(0, END)  # 🧹 Limpia el Listbox / Clear Listbox
        for i in self.arreglo:
            self.listVisrual.insert(self.listVisrual.size()+1, i)  # 📥 Inserta los datos ordenados / Insert sorted data


    def elimiarDato(self):
        # 🗑️ Método para eliminar un elemento según el modo / Delete element depending on mode
        if self.listVisrual.size() <= 0:
            messagebox.showerror("Error", "lita vacia")  # ⚠️ Mensaje de error si la lista está vacía / Show error message
            return 
        
        if self.modo.get() == "Pilas":
            # 🧱 Pila: último que entra, primero que sale / Stack: last in, first out
            self.listVisrual.delete(self.listVisrual.size()-1)
        else:
            # 📬 Cola: primero que entra, primero que sale / Queue: first in, first out
            self.listVisrual.delete(0)
        self.label.config(text = f"Elementos en la lista: {str(self.listVisrual.size())}")  # 🔢 Actualiza cantidad / Update counter


    def validarCaja(self):
        # 🧾 Método para validar el contenido del campo de texto / Method to validate text field input
        valor = self.dato.get()  # 🧾 Obtiene el texto escrito en el Entry / Get input value
        
        # 🧮 Validación numérica / Numeric validation
        if self.val.ValidacionesNumeros(valor): 
            if self.val.validarEntradas(valor):  # ✅ Si pasa la validación / If passes validation
                self.listVisrual.insert(END, valor)  # 📥 Agrega el número a la lista / Insert number into list
                self.dato.delete(0, END)  # 🧹 Limpia campo / Clear field
            else: 
                messagebox.showerror("Error", "Solo se permiten dos dijitos")  # ⚠️ Error: solo dos dígitos / Only two digits allowed
                self.dato.delete(0, END)
        else: 
            messagebox.showerror("Error", "No son numeros")  # ⚠️ Error: no numérico / Not a number
            self.dato.delete(0, END)
        
        self.label.config(text = f"Elementos en la lista: {str(self.listVisrual.size())}")  # 🔢 Muestra cantidad actual / Show element count


# 🚀 Punto de entrada del programa / Entry point of the program
if __name__=="__main__":
    app = Prinicipal()  # 🧩 Crea instancia de la clase principal / Create instance of main class
    app.inicio()  # ▶️ Llama al método para iniciar la ventana / Call main method to start GUI
