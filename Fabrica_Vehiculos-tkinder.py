import tkinter as tk
from tkinter import messagebox

class Fabrica:
    def __init__(self, llantas, color, precio, stock):
        self.__llantas = llantas  # Atributos privados
        self.__color = color
        self.__precio = precio
        self.__stock = stock

    def vender(self):
        if self.__stock > 0:
            self.__stock -= 1
            print(f"Vehículo vendido. Quedan {self.__stock} en stock.")
        else:
            print("No hay stock suficiente para vender.")

    def mostrar_detalles(self):
        return f"Llantas: {self.__llantas}, Color: {self.__color}, Precio: ${self.__precio}, Stock: {self.__stock}"

class Moto(Fabrica):
    def __init__(self, color, precio, stock):
        super().__init__(2, color, precio, stock)  

class Carro(Fabrica):
    def __init__(self, color, precio, stock):
        super().__init__(4, color, precio, stock)  
class Bicicleta(Fabrica):
    def __init__(self, color, precio, stock):
        super().__init__(2, color, precio, stock)  
class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Fábrica de Vehículos")

        # Selección de tipo de vehículo
        tk.Label(master, text="Selecciona el tipo de vehículo:").pack(pady=5)
        self.tipo_var = tk.StringVar(value="Moto")
        tk.Radiobutton(master, text="Moto", variable=self.tipo_var, value="Moto").pack()
        tk.Radiobutton(master, text="Carro", variable=self.tipo_var, value="Carro").pack()
        tk.Radiobutton(master, text="Bicicleta", variable=self.tipo_var, value="Bicicleta").pack()

        # Entradas para atributos del vehículo
        tk.Label(master, text="Color:").pack(pady=5)
        self.entrada_color = tk.Entry(master)
        self.entrada_color.pack(pady=5)

        tk.Label(master, text="Precio:").pack(pady=5)
        self.entrada_precio = tk.Entry(master)
        self.entrada_precio.pack(pady=5)

        tk.Label(master, text="Stock:").pack(pady=5)
        self.entrada_stock = tk.Entry(master)
        self.entrada_stock.pack(pady=5)

        # Botón para crear vehículo
        self.boton_crear = tk.Button(master, text="Crear Vehículo", command=self.crear_vehiculo)
        self.boton_crear.pack(pady=20)

    def crear_vehiculo(self):
        color = self.entrada_color.get()
        precio = self.entrada_precio.get()
        stock = self.entrada_stock.get()

        # Validar entradas
        if not color or not precio or not stock:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return

        try:
            precio = float(precio)
            stock = int(stock)
        except ValueError:
            messagebox.showwarning("Advertencia", "El precio debe ser un número y el stock debe ser un entero.")
            return

        tipo_vehiculo = self.tipo_var.get()
        
        if tipo_vehiculo == "Moto":
            vehiculo = Moto(color, precio, stock)
        elif tipo_vehiculo == "Carro":
            vehiculo = Carro(color, precio, stock)
        elif tipo_vehiculo == "Bicicleta":
            vehiculo = Bicicleta(color, precio, stock)

        # Mostrar detalles del vehículo creado
        detalles = vehiculo.mostrar_detalles()
        messagebox.showinfo("Detalles del Vehículo", detalles)

# Crear la ventana principal
ventana = tk.Tk()
ventana.option_add("*Font", "Helvetica 12")
ventana.minsize(300, 400)  
ventana.maxsize(500, 400) 
app = Aplicacion(ventana)
ventana.mainloop()
