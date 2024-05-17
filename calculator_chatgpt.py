import tkinter as tk
from tkinter import messagebox

def agregar_caracter(caracter):
    entrada_texto.insert(tk.END, caracter)

def borrar_caracter():
    entrada_texto.delete(len(entrada_texto.get()) - 1)

def limpiar_pantalla():
    entrada_texto.delete(0, tk.END)

def calcular():
    try:

        resultado = eval(entrada_texto.get())

        limpiar_pantalla()
        entrada_texto.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", "Expresión inválida")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear y posicionar la entrada de texto
entrada_texto = tk.Entry(ventana, font=("Arial", 18), bd=5, justify="right")
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir botones para la calculadora
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("(", 4, 1), (")", 4, 2), ("+", 4, 3)
]

# Crear botones y posicionarlos en la ventana
for boton_texto, fila, columna in botones:
    boton = tk.Button(ventana, text=boton_texto, font=("Arial", 18), padx=20, pady=10,
                      command=lambda texto=boton_texto: agregar_caracter(texto))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

# Botón de borrar, limpiar y calcular
boton_borrar = tk.Button(ventana, text="←", font=("Arial", 18), padx=20, pady=10, command=borrar_caracter)
boton_borrar.grid(row=1, column=4, padx=5, pady=5)

boton_limpiar = tk.Button(ventana, text="C", font=("Arial", 18), padx=20, pady=10, command=limpiar_pantalla)
boton_limpiar.grid(row=2, column=4, padx=5, pady=5)

boton_calcular = tk.Button(ventana, text="=", font=("Arial", 18), padx=20, pady=10, command=calcular)
boton_calcular.grid(row=3, column=4, rowspan=2, padx=5, pady=5, sticky="ns")

# Ejecutar la aplicación
ventana.mainloop()