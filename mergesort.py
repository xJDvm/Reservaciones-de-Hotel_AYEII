import tkinter as tk
from tkinter import ttk
import json

# Función para cargar los datos desde el archivo JSON
def cargar_datos_desde_json():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

# Función para mostrar la ventana con la tabla
def mostrar_ventana_mergesort():
    datos = cargar_datos_desde_json()

    def ordenar_fecha_ascendente():
        tabla.delete(*tabla.get_children())  
        datos_ordenados = sorted(datos, key=lambda x: x["Fecha"])
        for dato in datos_ordenados:
            tabla.insert("", "end", values=(dato["Fecha"], dato["Cliente"], dato["Reserva"], dato["Entrada"], dato["Salida"], dato["Precio Total"], dato["ID"]))

    def ordenar_fecha_descendente():
        tabla.delete(*tabla.get_children())  
        datos_ordenados = sorted(datos, key=lambda x: x["Fecha"], reverse=True)
        for dato in datos_ordenados:
            tabla.insert("", "end", values=(dato["Fecha"], dato["Cliente"], dato["Reserva"], dato["Entrada"], dato["Salida"], dato["Precio Total"], dato["ID"]))

    ventana = tk.Tk()
    ventana.title("Reporte por fecha")

    tabla = ttk.Treeview(ventana, columns=("Fecha", "Cliente", "Reserva", "Entrada", "Salida", "Precio", "ID"))
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Cliente", text="Cliente")
    tabla.heading("Reserva", text="Reserva")
    tabla.heading("Entrada", text="Entrada")
    tabla.heading("Salida", text="Salida")
    tabla.heading("Precio", text="Precio")
    tabla.heading("ID", text="ID")

    tabla.column("#0", width=0)


    for dato in datos:
        tabla.insert("", "end", values=(dato["Fecha"], dato["Cliente"], dato["Reserva"], dato["Entrada"], dato["Salida"], dato["Precio Total"], dato["ID"]))

    btn_ascendente = tk.Button(ventana, text="Ordenar Fecha Ascendente", command=ordenar_fecha_ascendente)
    btn_descendente = tk.Button(ventana, text="Ordenar Fecha Descendente", command=ordenar_fecha_descendente)

    tabla.pack()
    btn_ascendente.pack()
    btn_descendente.pack()

    ventana.mainloop()
