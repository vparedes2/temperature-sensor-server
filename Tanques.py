import tkinter as tk
from tkinter import messagebox

def calcular_contenido():
    try:
        nivel_vacio = float(entrada_nivel.get())
        tipo_tanque = var_tipo_tanque.get()
        
        if tipo_tanque == 1:
            volumen_total = 5400
            radio = (volumen_total / (3 * 3.14159))**(1/3)
        else:
            volumen_total = 4100
            radio = (volumen_total / (3 * 3.14159))**(1/3)
        
        altura_agua = 3 - (nivel_vacio / 100)
        volumen_agua = 3.14159 * (radio**2) * altura_agua
        area_base = 3.14159 * (radio**2)
        
        resultado.config(text=f"Contenido: {volumen_agua:.2f} m³\nÁrea base: {area_base:.2f} m²")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para el nivel de vacío.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Tanques Australianos")
ventana.geometry("300x200")

# Crear y colocar los widgets
tk.Label(ventana, text="Nivel de vacío (cm):").pack()
entrada_nivel = tk.Entry(ventana)
entrada_nivel.pack()

var_tipo_tanque = tk.IntVar()
var_tipo_tanque.set(1)
tk.Radiobutton(ventana, text="Tanque de 5400 m³", variable=var_tipo_tanque, value=1).pack()
tk.Radiobutton(ventana, text="Tanque de
