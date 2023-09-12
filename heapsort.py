import tkinter as tk
from tkinter import ttk
import json

# Función para cargar los datos desde el archivo JSON
def cargar_datos_desde_json():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

# Función para ordenar los datos utilizando heapsort
def heapsort(datos, ascendente=True):
    n = len(datos)

    for i in range(n // 2 - 1, -1, -1):
        heapify(datos, n, i)

    for i in range(n - 1, 0, -1):
        datos[0], datos[i] = datos[i], datos[0]
        heapify(datos, i, 0)

    if not ascendente:
        datos.reverse()

# Función para convertir la duración de la estancia en un número entero para el ordenamiento
def duracion_estancia(dato):
    return int(dato["Estadia"])

# Función para mantener la propiedad de heap
def heapify(datos, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and duracion_estancia(datos[left]) > duracion_estancia(datos[largest]):
        largest = left

    if right < n and duracion_estancia(datos[right]) > duracion_estancia(datos[largest]):
        largest = right

    if largest != i:
        datos[i], datos[largest] = datos[largest], datos[i]
        heapify(datos, n, largest)

# Función para mostrar la ventana con la tabla
def mostrar_ventana_heapsort():
    datos = cargar_datos_desde_json()

    def ordenar_por_estadia_ascendente():
        tabla.delete(*tabla.get_children())
        heapsort(datos, ascendente=True)
        for dato in datos:
            tabla.insert("", "end", values=(dato["Fecha"], dato["Cliente"], dato["Reserva"], dato["Entrada"], dato["Salida"], dato["Estadia"], dato["ID"]))

    def ordenar_por_estadia_descendente():
        tabla.delete(*tabla.get_children())
        heapsort(datos, ascendente=False)
        for dato in datos:
            tabla.insert("", "end", values=(dato["Fecha"], dato["Cliente"], dato["Reserva"], dato["Entrada"], dato["Salida"], dato["Estadia"], dato["ID"]))

    ventana = tk.Tk()
    ventana.title("Reporte de estadía")

    tabla = ttk.Treeview(ventana, columns=("Fecha", "Cliente", "Reserva", "Entrada", "Salida", "Estadia", "ID"))
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Cliente", text="Cliente")
    tabla.heading("Reserva", text="Reserva")
    tabla.heading("Entrada", text="Entrada")
    tabla.heading("Salida", text="Salida")
    tabla.heading("Estadia", text="Estadia")
    tabla.heading("ID", text="ID")

    tabla.column("#0", width=0)


    for dato in datos:
        tabla.insert("", "end", values=(dato["Fecha"], dato["Cliente"], dato["Reserva"], dato["Entrada"], dato["Salida"], dato["Estadia"], dato["ID"]))

    btn_ascendente = tk.Button(ventana, text="Ordenar Estadia Ascendente", command=ordenar_por_estadia_ascendente)
    btn_descendente = tk.Button(ventana, text="Ordenar Estadia Descendente", command=ordenar_por_estadia_descendente)

    tabla.pack()
    btn_ascendente.pack()
    btn_descendente.pack()

    ventana.mainloop()

