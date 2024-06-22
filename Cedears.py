import yfinance as yf
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class CEDEARApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CEDEAR Cotizaciones")
        
        self.cedears = [
            "AAPL.BA", "MSFT.BA", "GOOGL.BA", "AMZN.BA", "FB.BA",
            "TSLA.BA", "NFLX.BA", "NVDA.BA", "PYPL.BA", "INTC.BA"
        ]
        
        self.create_widgets()
        
    def create_widgets(self):
        self.tree = ttk.Treeview(self.master, columns=('Símbolo', 'Precio'), show='headings')
        self.tree.heading('Símbolo', text='Símbolo')
        self.tree.heading('Precio', text='Precio')
        self.tree.pack(pady=10)
        
        self.update_button = tk.Button(self.master, text="Actualizar precios", command=self.update_prices)
        self.update_button.pack(pady=5)
        
        self.tree.bind("<ButtonRelease-1>", self.on_select)
        
        self.graph_frame = tk.Frame(self.master)
        self.graph_frame.pack(pady=10)
        
    def update_prices(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for cedear in self.cedears:
            ticker = yf.Ticker(cedear)
            price = ticker.info['regularMarketPrice']
            self.tree.insert('', 'end', values=(cedear, f"${price:.2f}"))
    
    def on_select(self, event):
        selected_item = self.tree.focus()
        symbol = self.tree.item(selected_item)['values'][0]
        self.show_graph(symbol)
    
    def show_graph(self, symbol):
        ticker = yf.Ticker(symbol)
        
        fig, ax = plt.subplots(figsize=(8, 4))
        
        periods = {'1d': '1 día', '5d': '1 semana', '1mo': '1 mes'}
        for period, label in periods.items():
            data = ticker.history(period=period)
            ax.plot(data.index, data['Close'], label=label)
        
        ax.set_title(f"Variación de precio - {symbol}")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Precio")
        ax.legend()
        
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

root = tk.Tk()
app = CEDEARApp(root)
root.mainloop()
