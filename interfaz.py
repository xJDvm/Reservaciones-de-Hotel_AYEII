import tkinter as tk
from tkinter import ttk
import json
import random
import reservaciones

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Reservaciones")

# Botón para cargar una nueva reservación (debes implementar la función correspondiente)
new_reservation_button = tk.Button(root, text="Cargar Nueva Reservación", command=reservaciones.abrir_formulario)
new_reservation_button.pack()

# Botón para generar reportes (debes implementar la función correspondiente)
generate_report_button = tk.Button(root, text="Generar Reportes")
generate_report_button.pack()

# Crear la tabla
table = ttk.Treeview(root, columns=("Fecha", "Cliente", "Reserva", "Entrada", "Salida", "Habitación", "Estadia", "Tipo", "Preferencias", "Personas", "Contacto", "Precio Total", "Pago", "Notas", "Estado", "ID"))
table.heading("#1", text="Fecha")
table.heading("#2", text="Cliente")
table.heading("#3", text="Reserva")
table.heading("#4", text="Entrada")
table.heading("#5", text="Salida")
table.heading("#6", text="Habitación")
table.heading("#7", text="Estadia")
table.heading("#8", text="Tipo")
table.heading("#9", text="Preferencias")
table.heading("#10", text="Personas")
table.heading("#11", text="Contacto")
table.heading("#12", text="Precio Total")
table.heading("#13", text="Pago")
table.heading("#14", text="Notas")
table.heading("#15", text="Estado")
table.heading("#16", text="ID")

# Establecer el ancho de las columnas
table.column("#0", width=0)
for i in range(1, 17):
    table.column(f"#{i}", width=100)

# Cargar datos desde un archivo JSON y generar IDs aleatorios
with open("reservaciones.json", "r") as json_file:
    data = json.load(json_file)
    for item in data:
        # Generar un ID aleatorio (por ejemplo, un número entre 1 y 1000)
        item["ID"] = random.randint(1, 1000)
        table.insert("", "end", values=tuple(item.values()))

# Agregar la tabla a la ventana
table.pack(padx=20, pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()
