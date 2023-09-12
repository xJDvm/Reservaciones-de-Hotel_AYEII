import tkinter as tk
from tkinter import ttk
import json


def cargar_datos_y_actualizar_tabla(table):
    # Borrar todos los elementos actuales de la tabla
    table.delete(*table.get_children())
    
    # Cargar datos desde el archivo JSON y generar IDs por orden de llegada
    with open("datos.json", "r") as json_file:
        data = json.load(json_file)
        for i, item in enumerate(data):
            # Asignar un ID incremental basado en el orden de llegada
            item["ID"] = i + 1
            table.insert("", "end", values=tuple(item.values()))

def borrar_reservacion(id):
    # Cargar datos actuales desde el archivo JSON
    with open("datos.json", "r") as json_file:
        data = json.load(json_file)
    
    # Buscar y eliminar el elemento con el ID especificado
    for reservacion in data:
        if str(reservacion["ID"]) == str(id):
            data.remove(reservacion)
            break
    
    # Actualizar los IDs basados en el orden de llegada
    for i, item in enumerate(data):
        item["ID"] = i + 1
    
    # Guardar los datos actualizados en el archivo JSON
    with open("datos.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
