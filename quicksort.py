import tkinter as tk
from tkinter import ttk

# Función para ordenar la tabla
# Variable para realizar seguimiento del estado de ordenación de cada columna
sort_states = {}

def sort_by(column, table, sort_states):
    if column.startswith("#"):
        column_num = int(column.lstrip("#")) - 1
    else:
        column_num = 0

    # Obtener el estado de ordenación actual para esta columna
    current_state = sort_states.get(column, None)

    # Determinar el estado de ordenación siguiente
    if current_state is None or current_state == "descendente":
        reverse = False
        sort_states[column] = "ascendente"
    else:
        reverse = True
        sort_states[column] = "descendente"

    # Agregar una flecha al encabezado de columna ordenada
    arrow = "Ascendente ▲" if not reverse else "Descendente ▼"
    table.heading(column, text=f"{arrow}")

    def limpiar_flechas(table, sort_states):
        for col in sort_states.keys():
            table.heading(col, text=col)

    items = [(table.item(item)['values'], item) for item in table.get_children('')]

    def get_criterion(item):
        value = item[0][column_num]
        try:
            return int(value)
        except (ValueError, TypeError):
            return value

    def quicksort_recursive(items):
        if len(items) <= 1:
            return items

        pivot = items[len(items) // 2]
        left = [item for item in items if get_criterion(item) < get_criterion(pivot)]
        middle = [item for item in items if get_criterion(item) == get_criterion(pivot)]
        right = [item for item in items if get_criterion(item) > get_criterion(pivot)]

        left = sorted(left, key=lambda x: get_criterion(x))
        right = sorted(right, key=lambda x: get_criterion(x))

        if reverse:
            return right + middle + left
        else:
            return left + middle + right

    sorted_items = quicksort_recursive(items)

    for item in table.get_children(''):
        table.delete(item)

    for item in sorted_items:
        values, item_id = item
        table.insert('', 'end', values=values)
        
