import tkinter as tk
from tkinter import ttk, messagebox
import requests
from flask import Flask, request, jsonify
import threading

# Crear el servidor Flask
app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_volume():
    data = request.json
    tank_size = data['tank_size']
    vacuum_level = data['vacuum_level']

    # Convertir vacío en cm a altura de agua en cm
    height = 300 - vacuum_level
    
    # Calcular el radio del tanque basado en el tamaño
    if tank_size == 5400:
        radius = (5400 / (3.14159 * 3)) ** 0.5
    elif tank_size == 4100:
        radius = (4100 / (3.14159 * 3)) ** 0.5
    else:
        return jsonify({'error': 'Invalid tank size'}), 400

    # Calcular el volumen
    volume = 3.14159 * (radius ** 2) * (height / 100)  # Convertir altura de cm a metros
    return jsonify({'volume': volume})

def run_flask():
    app.run(debug=True, use_reloader=False)

# Crear la interfaz de usuario con Tkinter
class TankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tank Measurement App")

        self.create_widgets()

    def create_widgets(self):
        self.tank_size_label = tk.Label(self.root, text="Select Tank Size (in cubic meters):")
        self.tank_size_label.pack()

        self.tank_size = tk.StringVar()
        self.tank_size_combo = ttk.Combobox(self.root, textvariable=self.tank_size)
        self.tank_size_combo['values'] = ('5400', '4100')
        self.tank_size_combo.current(0)
        self.tank_size_combo.pack()

        self.vacuum_level_label = tk.Label(self.root, text="Enter vacuum level (cm):")
        self.vacuum_level_label.pack()

        self.vacuum_level_entry = tk.Entry(self.root)
        self.vacuum_level_entry.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_volume)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def calculate_volume(self):
        tank_size = int(self.tank_size.get())
        vacuum_level = int(self.vacuum_level_entry.get())

        response = requests.post('http://127.0.0.1:5000/calculate', json={'tank_size': tank_size, 'vacuum_level': vacuum_level})
        if response.status_code == 200:
            volume = response.json()['volume']
            self.result_label.config(text=f"Calculated Volume: {volume:.2f} cubic meters")
        else:
            messagebox.showerror("Error", "An error occurred while calculating the volume.")

if __name__ == '__main__':
    # Iniciar el servidor Flask en un hilo separado
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Iniciar la interfaz de usuario Tkinter
    root = tk.Tk()
    app = TankApp(root)
    root.mainloop()
