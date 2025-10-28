from tkinter import *  # 🪟 Importa todas las clases y funciones de Tkinter / Import all Tkinter classes and functions
from tkinter import messagebox  # 💬 Importa messagebox para mostrar mensajes emergentes / Used for pop-up messages
from validaciones import validaciones1  # ✅ Importa la clase validaciones1 desde otro archivo / Import external validation class
import numpy as np

class Prinicipal():  # 🧱 Clase principal del programa / Main class of the program
    def __init__(self):
        self.ven = Tk()  # 🪟 Crea la ventana principal / Creates main window
        self.val = validaciones1()  # 🧩 Crea un objeto de la clase validaciones1 / Creates an instance of validation class
        ancho = 320
        alto = 250
        ventana_alto = self.ven.winfo_screenmmwidth()
        ventana_ancho = self.ven.winfo_screenmmheight()
        x = (ventana_alto // 2) - (ancho // 2)
        y = (ventana_ancho // 2) - (alto // 2)
        self.ven.geometry(f"{ancho}x{alto}+{x + 560}+{y + 200}")
        # self.ven.geometry("320x210")  # 📏 Define tamaño de la ventana / Set window size
        # self.ven.configure(start_position = "center")
        self.listaNum = []  # 📋 Lista donde se almacenarán números válidos / List to store valid numbers


    def inicio(self):
        # 🧠 Entrada de texto donde el usuario escribe un dato / Text entry for user input
        self.dato = Entry(self.ven)
        self.dato.place(x = 30, y = 10)  # 📍 Posiciona el cuadro de texto / Places the input field on window
        self.modo = StringVar(value="Pilas") # valor predeterminado
        Radiobutton(self.ven, text = "Pilas", variable= self.modo, value= "Pilas").place(x = 40, y = 40)
        Radiobutton(self.ven, text = "Colas", variable= self.modo, value= "Colas").place(x = 90, y = 40)
        self.tipoDeOrden = StringVar(value = "Men_a_Mayor")
        Radiobutton(self.ven, text = "Asendente", variable= self.tipoDeOrden, value= "Men_a_Mayor").place(x = 9, y = 150)
        Radiobutton(self.ven, text = "Desendente", variable= self.tipoDeOrden, value= "Mayor_a_Men").place(x = 90, y = 150)
        # 🖱️ Botón que ejecuta la validación / Button to trigger validation
        Button(self.ven, text= " Validar", command= self.validarCaja, width = 10).place(x = 100, y = 90)
        Button(self.ven, text= " Eliminar", command= self.elimiarDato, width = 10).place(x = 100, y = 120)
        self.label = Label(self.ven, text = "Numero")
        self.label.place(x = 5, y = 70)
        Button(self.ven, text= "Ordenar", command= self.ordenarDat, width = 10).place(x = 100, y = 190)
        # 📜 Listbox para mostrar visualmente los números válidos / Listbox to visually show valid numbers
        self.listVisrual = Listbox(
            self.ven, 
            height = 10,
            width = 10,          # ↔️ Ancho de la lista / Width
            bg = "white",        # ⚫ Fondo negro / Black background
            # activestyle= "dotbox", # 🔲 Estilo al seleccionar / Selection style
            # fg=  "white"         # ⚪ Texto blanco / White text
            font = ("Helvetica", 12)
        )
        self.listVisrual.place(x = 190, y = 10)  # 📍 Posición del Listbox / Place list visually on window

        self.ven.mainloop()  # 🔁 Mantiene la ventana abierta / Keeps the window running until closed

    def ordenarDat(self):

        self.listaNum = list(self.listVisrual.get(0, END))
        if (len(self.listaNum) <= 0):
            messagebox.showerror("Error", "Lista bacia")
            return 0
        
        self.arreglo = np.array(self.listaNum)

        if self.tipoDeOrden.get() == "Men_a_Mayor":
            # por burbuja 
            for i in range(0, len(self.arreglo)):
                for x in range(0, len(self.arreglo) - i - 1):
                    if (self.arreglo[x]) > self.arreglo[x +1]:
                        aux = self.arreglo[x]
                        self.arreglo[x] = self.arreglo[x +1]
                        self.arreglo[x +1] = aux
        else:
            # por seleccion 
            pos = 0
            for i in range(0,len(self.arreglo)):
                pos = i
                aux = int(self.arreglo[i])

                for x in range(i, len(self.arreglo)):

                    if aux < int(self.arreglo[x]):
                        aux = int (self.arreglo[x])
                        pos = x
                    # print(f"Posible mauor {aux}")
                self.arreglo[pos] = self.arreglo[i]
                self.arreglo[i] = str(aux)

        print(self.arreglo)
        self.listVisrual.delete(0, END)
        for i in self.arreglo:
            self.listVisrual.insert(self.listVisrual.size()+1, i)

    def elimiarDato(self):
        if self.listVisrual.size() <= 0:
            messagebox.showerror("Error", "lita vacia")
            return 
        
        if self.modo.get() == "Pilas":
            #ultipo que entra primero que sale
            self.listVisrual.delete(self.listVisrual.size()-1)
        else:
            # primero que entra primero que sale
            self.listVisrual.delete(0)
        self.label.config(text = f"Elementos en la lista: {str(self.listVisrual.size())}")

    def validarCaja(self):
        valor = self.dato.get()  # 🧾 Obtiene el texto escrito en el Entry / Get input value
        # if valor == "":  # 🚫 Si el campo está vacío / If field is empty
        #     messagebox.showinfo("Error", "Campo bacio")  # ⚠️ Muestra aviso de error / Show error message
        #     return 1  # 🔙 Sale del método / Exit the method
        
        # # ✅ Si pasa la validación numérica / If validation passes (is a number)
        # if self.val.ValidacionesNumeros(valor):
        #     messagebox.showinfo("correcto", "Si es numero")  # 👍 Muestra mensaje de éxito / Show success message
        #     # self.listaNum.append(valor)  # (comentado) podría almacenar el número / Could append number to list
        #     # self.listVisrual(despues de que elemto colocar, valor a colocar)
        #     self.listVisrual.insert(END, valor)  # 📥 Inserta el valor al final de la lista visual / Add value to Listbox
        #     self.dato.delete(0, END)  # 🧹 Limpia el Entry / Clear input field
        #     return 0  # 🔙 Finaliza función correctamente / Return success
        
        # # ❌ Si no pasa la validación numérica / If not a number
        # messagebox.showinfo("Error", "no es numero")  # ⚠️ Muestra mensaje de error / Show error message
        # self.dato.delete(0, END)  # 🧹 Limpia campo para volver a intentar / Clear field for next attempt
        # print (self.val.validarEntradas(valor))
        if self.val.ValidacionesNumeros(valor): 
            if self.val.validarEntradas(valor):
                self.listVisrual.insert(END, valor)
                self.dato.delete(0, END)
            else: 
                messagebox.showerror("Error", "Solo se permiten dos dijitos")
                self.dato.delete(0, END)
        else: 
            messagebox.showerror("Error", "No son numeros")
            self.dato.delete(0, END)
        self.label.config(text = f"Elementos en la lista: {str(self.listVisrual.size())}")
        # 📝 Bloque comentado alternativo / Alternate commented validation block:
        # if (self.val.ValidacionesNumeros(valor)):
        #     messagebox.showinfo("correcto", "Si es numero")
        # else:
        #      messagebox.showinfo("Error", "no es numero")


# 🚀 Punto de entrada del programa / Entry point of the program
if __name__=="__main__":
    app = Prinicipal()  # 🧩 Crea instancia de la clase principal / Create instance of main class
    app.inicio()  # ▶️ Llama al método para iniciar la ventana / Call main method to start GUI
