import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, ventana):
        """Inicializa la calculadora y su interfaz gráfica."""
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("400x400")
        self.ventana.resizable(False, False)

        # Crear el campo de entrada
        self.entrada = tk.Entry(self.ventana, font=("Arial", 20), bd=5, justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Definir los botones de la calculadora
        self.botones = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        # Colores de los botones
        self.colores_numeros = "#FFEB3B"  # Amarillo para los números
        self.colores_operadores = "#2196F3"  # Azul para los operadores
        self.colores_igual = "#4CAF50"  # Verde para el "="
        self.colores_limpiar = "#f44336"  # Rojo para "C"

        # Disposición de los botones en la ventana
        self.distribuir_botones()

    def distribuir_botones(self):
        """Distribuye los botones en la cuadrícula."""
        fila = 1
        columna = 0

        for boton in self.botones:
            if boton == "=":
                b = tk.Button(self.ventana, text=boton, width=5, height=2, font=("Arial", 15),
                              bg=self.colores_igual, fg="white", command=self.calcular)
            elif boton == "C":
                b = tk.Button(self.ventana, text=boton, width=5, height=2, font=("Arial", 15),
                              bg=self.colores_limpiar, fg="white", command=self.limpiar)
            elif boton in "0123456789":  # Números
                b = tk.Button(self.ventana, text=boton, width=5, height=2, font=("Arial", 15),
                              bg=self.colores_numeros, command=lambda valor=boton: self.click_boton(valor))
            else:  # Operadores
                b = tk.Button(self.ventana, text=boton, width=5, height=2, font=("Arial", 15),
                              bg=self.colores_operadores, fg="white", command=lambda valor=boton: self.click_boton(valor))

            b.grid(row=fila, column=columna, padx=5, pady=5)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

    def click_boton(self, valor):
        """Agregar el valor del botón al campo de entrada."""
        self.entrada.insert(tk.END, valor)

    def limpiar(self):
        """Limpiar el campo de entrada."""
        self.entrada.delete(0, tk.END)

    def calcular(self):
        """Evaluar la expresión matemática y mostrar el resultado en un mensaje."""
        try:
            # Obtener la expresión del campo de entrada
            expresion = self.entrada.get()

            # Validar que solo contenga caracteres permitidos
            if not all(c.isdigit() or c in "+-*/.()" for c in expresion.replace(" ", "")):
                raise ValueError("Expresión inválida")

            # Intentar evaluar la expresión
            resultado = eval(expresion)

            # Limpiar y mostrar el resultado
            self.limpiar()
            self.entrada.insert(tk.END, str(resultado))

            # Mostrar el resultado en un mensaje de alerta
            messagebox.showinfo("Resultado", f"El resultado es: {resultado}")

        except ZeroDivisionError:
            messagebox.showerror("Error", "Error: División por cero")
        except Exception as e:
            # Mostrar un error si ocurre cualquier otro tipo de excepción
            messagebox.showerror("Error", f"Expresión inválida: {str(e)}")


# Crear la ventana principal
ventana = tk.Tk()

# Crear la calculadora
calculadora = Calculadora(ventana)

# Iniciar la aplicación
ventana.mainloop()

