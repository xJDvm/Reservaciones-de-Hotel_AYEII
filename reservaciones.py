import tkinter as tk
import json
import random
import actualizar 
from tkcalendar import DateEntry

# Función para guardar una nueva reservación en el archivo JSON
def guardar_reservacion(entries, nueva_reservacion_window):
    nueva_reservacion = {
        "Fecha": entries["Fecha"].get_date(),
        "Cliente": entries["Cliente"].get(),
        "Reserva": entries["Reserva"].get_date(),
        "Entrada": entries["Entrada"].get_date(),
        "Salida": entries["Salida"].get_date(),
        "Habitación": entries["Habitación"].get(),
        "Estadia": entries["Estadia"].get(),
        "Tipo": entries["Tipo"].get(),
        "Preferencias": entries["Preferencias"].get(),
        "Personas": entries["Personas"].get(),
        "Contacto": entries["Contacto"].get(),
        "Precio Total": entries["Precio Total"].get(),
        "Pago": entries["Pago"].get(),
        "Notas": entries["Notas"].get(),
        "Estado": entries["Estado"].get(),
        "ID": random.randint(1, 1000)  # Generar un ID aleatorio
    }
    
    # Cargar datos actuales desde el archivo JSON
    with open("datos.json", "r") as json_file:
        data = json.load(json_file)
    
    # Agregar la nueva reservación a los datos existentes
    data.append(nueva_reservacion)
    
    # Guardar los datos actualizados en el archivo JSON
    with open("datos.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    # Cerrar la ventana del formulario
    nueva_reservacion_window.destroy()

# Función para abrir el formulario de nueva reservación
def abrir_formulario():
    nueva_reservacion_window = tk.Toplevel()
    nueva_reservacion_window.title("Nueva Reservación")
    
    # Crear y colocar etiquetas y campos de entrada en el formulario
    campos = ["Fecha", "Cliente", "Reserva", "Entrada", "Salida", "Habitación", "Estadia", "Tipo", "Preferencias", "Personas", "Contacto", "Precio Total", "Pago", "Notas", "Estado"]
    entries = {}
    for i, campo in enumerate(campos):
        tk.Label(nueva_reservacion_window, text=campo + ":").grid(row=i, column=0, sticky="e")
        if campo in ["Fecha", "Reserva", "Entrada", "Salida"]:
            entry = DateEntry(nueva_reservacion_window, date_pattern="yyyy-mm-dd")  # Usar DateEntry para fechas
        else:
            entry = tk.Entry(nueva_reservacion_window)
        entry.grid(row=i, column=1)
        entries[campo] = entry
    
    # Botón para guardar la nueva reservación
    tk.Button(nueva_reservacion_window, text="Guardar", command=lambda: guardar_reservacion(entries, nueva_reservacion_window)).grid(row=len(campos), columnspan=2)

    
    