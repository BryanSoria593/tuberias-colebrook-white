import tkinter as tk
from tkinter import ttk, messagebox
from utils.prandtl_colebrook import calcular_velocidad, perdida_friccion
import math

def comprobacion_diseno_tuberias():
    # Obtener datos del formulario
    data = formulario()
    
    # Función que se ejecuta al hacer clic en el botón "Calcular"
    def on_button_click():
        calcular(data)

    # Crear un botón en la ventana principal
    boton_calcular = ttk.Button(data["ventana"], text="Calcular", command=on_button_click)
    boton_calcular.grid(row=10, column=0, columnspan=2, pady=15)

def formulario():
    # Crear una nueva ventana para el formulario
    formulario_ventana = tk.Toplevel()
    formulario_ventana.title("Formulario de cálculo")

    # Variables para almacenar datos del formulario    
    diametro = tk.StringVar()
    rugosidad = tk.StringVar()
    h = tk.StringVar()
    E = tk.StringVar()
    viscosidad = tk.StringVar()
    densidad = tk.StringVar()
    n = tk.StringVar()
    z_2 = tk.StringVar()
    km = tk.StringVar()
    longitud = tk.StringVar()
    iteraciones = tk.IntVar(value=10)

    ttk.Label(formulario_ventana, text="Diametro (D):").grid(row=0, column=0, pady=3, sticky='e')
    entry_diametro = ttk.Entry(formulario_ventana, textvariable=diametro)
    entry_diametro.grid(row=0, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Rugosidad (ε):").grid(row=1, column=0, pady=3, sticky='e')
    entry_rugosidad = ttk.Entry(formulario_ventana, textvariable=rugosidad)
    entry_rugosidad.grid(row=1, column=1, pady=3)

    ttk.Label(formulario_ventana, text="H:").grid(row=2, column=0, pady=3, sticky='e')
    entry_H = ttk.Entry(formulario_ventana, textvariable=h)
    entry_H.grid(row=2, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Tolerancia (E):").grid(row=3, column=0, pady=3, sticky='e')
    entry_E = ttk.Entry(formulario_ventana, textvariable=E)
    entry_E.grid(row=3, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Viscosidad (v):").grid(row=4, column=0, pady=3, sticky='e')
    entry_viscosidad = ttk.Entry(formulario_ventana, textvariable=viscosidad)
    entry_viscosidad.grid(row=4, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Densidad (ρ):").grid(row=5, column=0, pady=3, sticky='e')
    entry_densidad = ttk.Entry(formulario_ventana, textvariable=densidad)
    entry_densidad.grid(row=5, column=1, pady=3)

    ttk.Label(formulario_ventana, text="z_2:").grid(row=6, column=0, pady=3, sticky='e')
    entry_z_2 = ttk.Entry(formulario_ventana, textvariable=z_2)
    entry_z_2.grid(row=6, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Longitud (L):").grid(row=7, column=0, pady=3, sticky='e')
    entry_longitud = ttk.Entry(formulario_ventana, textvariable=longitud)
    entry_longitud.grid(row=7, column=1, pady=3)

    ttk.Label(formulario_ventana, text="km:").grid(row=8, column=0, pady=3, sticky='e')
    entry_km = ttk.Entry(formulario_ventana, textvariable=km)
    entry_km.grid(row=8, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Iteraciones:").grid(row=9, column=0, pady=3, sticky='e')
    entry_iteraciones = ttk.Entry(formulario_ventana, textvariable=iteraciones)
    entry_iteraciones.grid(row=9, column=1, pady=3)

    resultado_label = ttk.Label(formulario_ventana, text="")
    resultado_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
    
    tree = ttk.Treeview(formulario_ventana, columns=("Iteración", "Velocidad", "Error inicial (hl)", "Error iteración (hli)", "Error tolerado"), show="headings")
    tree.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

    # Configurar las columnas de la tabla
    tree.heading("#1", text="Iteración")
    tree.heading("#2", text="Velocidad")
    tree.heading("#3", text="Error inicial")
    tree.heading("#4", text="Error iteración")
    tree.heading("#5", text="Error tolerado")

    tree.column("#1", anchor="center")
    tree.column("#2", anchor="center")
    tree.column("#3", anchor="center")
    tree.column("#4", anchor="center")
    tree.column("#5", anchor="center")


    # Configurar el peso de las columnas para que se expandan con la ventana
    formulario_ventana.grid_columnconfigure(0, weight=1)
    formulario_ventana.grid_columnconfigure(1, weight=1)

    # se retorna un diccionario con todos los elementos del formulario y la tabla
    return {
        "ventana": formulario_ventana,
        "diametro": diametro,
        "rugosidad": rugosidad,
        "H": h,
        "Tolerancia": E,
        "viscosidad": viscosidad,
        "densidad": densidad,
        "N": n,
        "z_2": z_2,
        "km": km,
        "longitud": longitud,
        "iteraciones": iteraciones,
        "resultado_label": resultado_label,
        "tree": tree, # se retorna el widget Treeview para poder insertar los datos en la tabla
    }

def calcular(data):
    try:
        diametro = float(data["diametro"].get())
        rugosidad = float(data["rugosidad"].get())
        h = float(data["H"].get())
        z_2 = float(data["z_2"].get())
        viscosidad = float(data["viscosidad"].get())
        km = float(data["km"].get())
        error = float(data["Tolerancia"].get())
        iteraciones = int(data["iteraciones"].get())
        longitud = float(data["longitud"].get())
    except ValueError:
        messagebox.showerror("Error", "Al menos uno de los campos no es un número válido")
        return

    area = math.pi * (diametro**2) / 4
    # Suponer h_l = h - z_2
    perdida_inicial = round(h - z_2, 4)
    
    # Validar que los datos no sean cero
    if 0 in (diametro, rugosidad, h, viscosidad, longitud):
        messagebox.showerror("Error", "Ningún dato puede ser igual a cero")
        return
    # Validar que h y z_2 no sean iguales
    if h == z_2:
        messagebox.showerror("Error", "H y z_2 no pueden ser iguales")
        return
    
    # Eliminar los datos de la tabla antes de calcular
    data["tree"].delete(*data["tree"].get_children())
    
    for i in range(0, iteraciones):
        velocidad = calcular_velocidad(diametro, rugosidad, perdida_inicial, viscosidad, longitud)
        perdida_iteracion = perdida_friccion(h, z_2, km, velocidad)
        error_iteracion = abs(round(perdida_iteracion - perdida_inicial, 4))

        # Insertar los datos en la tabla
        data["tree"].insert("", "end", values=(i + 1,velocidad,perdida_inicial, error_iteracion, error))

        # Comprobar si se alcanzó la tolerancia
        if error_iteracion <=  error:
            Q = velocidad * area
            mensaje = f"La velocidad del flujo es {velocidad}\nEn la iteración {i+1} se encontró el caudal {Q}"
            data["resultado_label"].config(text=mensaje)
            break
        elif error_iteracion == math.inf or error_iteracion == 0:
            data["resultado_label"].config(text="")
            data["tree"].delete(*data["tree"].get_children())
            messagebox.showerror("Error", "No se puede calcular la velocidad con el valor de error_iteracion porque es infinito o cero")
            break

        elif i == iteraciones - 1 and error_iteracion > error:
            data["resultado_label"].config(text="")
            data["tree"].delete(*data["tree"].get_children())
            messagebox.showerror("Error", "No se encontró una solución durante todas las iteraciones")
            break
        else:
            perdida_inicial = perdida_iteracion
