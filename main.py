import tkinter as tk
import reservaciones
import actualizar
import json
from tkinter import Grid, messagebox, ttk
from quicksort import sort_by, sort_states
import reportes

def actualizar_tabla():
    actualizar.cargar_datos_y_actualizar_tabla(table)
    generar_titulos()

# Función para borrar el elemento seleccionado
def borrar_seleccionado():
    seleccion = table.selection()  # Obtiene la selección actual de la tabla
    # Obtiene el ID de la fila seleccionada
    if not seleccion:
        tk.messagebox.showwarning("Advertencia","Debes seleccionar una fila para borrar.")
    else:
        id_seleccionado = table.item(seleccion, "values")[-1]  # Suponemos que el ID es la última columna
        # Llama a la función para borrar la reservación en actualizar.py
        actualizar.borrar_reservacion(id_seleccionado)
        # Actualiza la tabla para reflejar los cambios
        actualizar.cargar_datos_y_actualizar_tabla(table)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Reservaciones")

# Botón para cargar una nueva reservación
new_reservation_button = tk.Button(root, text="Cargar Nueva Reservación", command=reservaciones.abrir_formulario)
new_reservation_button.grid(row=0, column=0, padx=5, pady=5)

# Botón para generar reportes (debes implementar la función correspondiente)
generate_report_button = tk.Button(root, text="Generar Reportes", command=reportes.abrir_ventana_reportes)
generate_report_button.grid(row=0, column=1, padx=1, pady=5)

# Botón para actualizar
update_table_button = tk.Button(root, text="Actualizar tabla", command=actualizar_tabla)
update_table_button.grid(row=0, column=2, padx=1, pady=5)

# Botón para borrar elemento seleccionado
delete_selected_button = tk.Button(root, text="Borrar Seleccionado", command=borrar_seleccionado)
delete_selected_button.grid(row=0, column=3, padx=1, pady=5)

# Crear la tabla
table = ttk.Treeview(root, columns=("Fecha", "Cliente", "Reserva", "Entrada", "Salida", "Habitación", "Estadia", "Tipo", "Preferencias", "Personas", "Contacto", "Precio Total", "Pago", "Notas", "Estado", "ID"))

# Configurar los encabezados de la tabla con casillas de verificación
def generar_titulos():
    headers = ["Fecha", "Cliente", "Reserva", "Entrada", "Salida", "Habitación", "Estadia", "Tipo", "Preferencias", "Personas", "Contacto", "Precio Total", "Pago", "Notas", "Estado", "ID"]
    for i, header in enumerate(headers):
        table.heading(f"#{i+1}", text=header, anchor="w", command=lambda col=f"#{i+1}": sort_by(col, table, sort_states))

# Establecer el ancho de las columnas
table.column("#0", width=0)
for i in range(1, 17):
    table.column(f"#{i}", width=110)

# Función para cargar datos desde el archivo JSON y actualizar la tabla
actualizar.cargar_datos_y_actualizar_tabla(table)
generar_titulos()

# Agregar la tabla a la ventana
table.grid(row=1, column=0, columnspan=4, padx=15, pady=20)
# Iniciar el bucle principal de la interfaz
root.mainloop()