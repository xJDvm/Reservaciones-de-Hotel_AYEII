import tkinter as tk
from tkinter import ttk
import json

# Función para cargar los datos desde el archivo JSON
def cargar_datos_desde_json():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

# Algoritmo Shellsort para ordenar la columna "Cliente"
def shellsort(datos, ascendente=True):
    n = len(datos)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = datos[i]
            j = i
            while j >= gap and (temp["Cliente"] < datos[j - gap]["Cliente"] if ascendente else temp["Cliente"] > datos[j - gap]["Cliente"]):
                datos[j] = datos[j - gap]
                j -= gap
            datos[j] = temp
        gap //= 2

# Función para mostrar la ventana con la tabla
def mostrar_ventana_shellsort():
    datos = cargar_datos_desde_json()

    def ordenar_cliente_ascendente():
        tabla.delete(*tabla.get_children())
        shellsort(datos, ascendente=True)
        for dato in datos:
            tabla.insert("", "end", values=(dato["Cliente"], dato["Personas"], dato["Contacto"], dato["ID"]))

    def ordenar_cliente_descendente():
        tabla.delete(*tabla.get_children())
        shellsort(datos, ascendente=False)
        for dato in datos:
            tabla.insert("", "end", values=(dato["Cliente"], dato["Personas"], dato["Contacto"], dato["ID"]))

    ventana = tk.Tk()
    ventana.title("Reporte por cliente")

    tabla = ttk.Treeview(ventana, columns=("Cliente", "Personas", "Contacto", "ID"))
    tabla.heading("Cliente", text="Cliente")
    tabla.heading("Personas", text="Personas")
    tabla.heading("Contacto", text="Contacto")
    tabla.heading("ID", text="ID")

    tabla.column("#0", width=0)


    for dato in datos:
        tabla.insert("", "end", values=(dato["Cliente"], dato["Personas"], dato["Contacto"], dato["ID"]))

    btn_ascendente = tk.Button(ventana, text="Ordenar Cliente Ascendente", command=ordenar_cliente_ascendente)
    btn_descendente = tk.Button(ventana, text="Ordenar Cliente Descendente", command=ordenar_cliente_descendente)

    tabla.pack()
    btn_ascendente.pack()
    btn_descendente.pack()

    ventana.mainloop()

