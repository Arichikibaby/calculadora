import tkinter as tk
from tkinter import messagebox

def click_boton(valor):
    """Agregar el valor del botón al campo de entrada."""
    entrada.insert(tk.END, valor)

def limpiar():
    """Limpiar el campo de entrada."""
    entrada.delete(0, tk.END)

def calcular():
    """Evaluar la expresión matemática y mostrar el resultado en un mensaje."""
    try:
        # Obtener la expresión del campo de entrada
        expresion = entrada.get()
        # Verificar que solo contenga números y operadores válidos
        if not all(c.isdigit() or c in "+-*/.()" for c in expresion.replace(" ", "")):
            raise ValueError("Expresión inválida")
        # Evaluar la expresión matemática
        resultado = eval(expresion)
        limpiar()
        entrada.insert(tk.END, str(resultado))
        # Mostrar el resultado en un mensaje de alerta
        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
    except Exception as e:
        # Si ocurre un error, mostrar el mensaje de error
        messagebox.showerror("Error", "Expresión inválida")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Crear el campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), bd=5, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Colores de los botones
colores_numeros = "#FFEB3B"  # Amarillo para los números
colores_operadores = "#2196F3"  # Azul para los operadores
colores_igual = "#4CAF50"  # Verde para el "="
colores_limpiar = "#f44336"  # Rojo para "C"

# Distribuir los botones
fila = 1
columna = 0

for boton in botones:
    if boton == "=":
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      bg=colores_igual, fg="white", command=calcular)
    elif boton == "C":
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      bg=colores_limpiar, fg="white", command=limpiar)
    elif boton in "0123456789":  # Números
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      bg=colores_numeros, command=lambda valor=boton: click_boton(valor))
    else:  # Operadores
        b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 15),
                      bg=colores_operadores, fg="white", command=lambda valor=boton: click_boton(valor))
    
    b.grid(row=fila, column=columna, padx=5, pady=5)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Iniciar la aplicación
ventana.mainloop()
