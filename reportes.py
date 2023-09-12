import tkinter as tk
from tkinter import ttk
import mergesort
import heapsort
import shellsort

class ReportesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Reportes")
        
        # Botón para ordenar por rango
        btn_ordenar_rango = tk.Button(self.root, text="Ordenar fecha - Mergesort", command=mergesort.mostrar_ventana_mergesort)
        btn_ordenar_rango.grid(row=0, column=0, padx=10, pady=10)

        # Botón para listar clientes ascendente o descendente
        btn_listar_clientes = tk.Button(self.root, text="Listar Clientes - Shellsort", command=shellsort.mostrar_ventana_shellsort)
        btn_listar_clientes.grid(row=0, column=1, padx=10, pady=10)

        # Botón para listar reservaciones ascendente o descendente por duración de estadía
        btn_listar_reservaciones = tk.Button(self.root, text="Ordenar por estadía - Heapsort", command=heapsort.mostrar_ventana_heapsort)
        btn_listar_reservaciones.grid(row=0, column=2, padx=10, pady=10)

        # Botón para cerrar la ventana
        btn_cerrar = tk.Button(self.root, text="Cerrar", command=self.root.destroy)
        btn_cerrar.grid(row=0, column=3, padx=10, pady=10)

def abrir_ventana_reportes():
    root = tk.Tk()
    app = ReportesWindow(root)
    root.mainloop()

