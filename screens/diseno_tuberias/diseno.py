import tkinter as tk
from tkinter import messagebox, ttk
from utils.prandtl_colebrook import calcular_velocidad, perdida_friccion
import math

# Función que crea y muestra la interfaz gráfica para el cálculo de tuberías simples
def diseno_tuberias_simples():

    data = formulario() # Obtener los datos del formulario y guardarlos en la variable "data"

    def on_button_click():
        calcular(data)

    # Función que se ejecuta cuando se hace click en el botón "Calcular" y ejecuta la función on_button_click 
    boton_calcular = ttk.Button(data["ventana"], text="Calcular", command=on_button_click)
    boton_calcular.grid(row=13, column=0, columnspan=2, pady=15)


# Función que crea y muestra el formulario para el cálculo de tuberías simples
def formulario():
    formulario_ventana = tk.Toplevel() # Crear una nueva ventana para el formulario    
    formulario_ventana.title("Formulario de cálculo de potencia de tuberías simples") # Establecer el título de la ventana

    # Inicio de la creación de variables para los campos del formulario
    qd = tk.StringVar(value=5)
    sum_d = tk.StringVar(value=3)
    diametro = tk.StringVar(value=0.0001)
    epsilon = tk.StringVar(value=3)
    h = tk.StringVar(value=3)
    l = tk.StringVar(value=1)
    tolerancia = tk.StringVar(value=1)
    z_2 = tk.StringVar(value=1)
    sum_km = tk.StringVar(value=1)
    u = tk.StringVar(value=1)
    viscosidad = tk.StringVar(value=1)
    densidad = tk.StringVar(value=1)
    iteraciones = tk.IntVar(value=10)
    # Fin de la creación de variables para los campos del formulario
    
    # Creamos un label y un entry para cada campo del formulario
    ttk.Label(formulario_ventana, text="qd:").grid(row=0, column=0, pady=3, sticky='e') # Crear un label para el campo "qd"
    entry_qd = ttk.Entry(formulario_ventana, textvariable=qd) # guardar el valor del campo "qd" en la variable "qd"
    entry_qd.grid(row=0, column=1, pady=3) # Estilo de la caja de texto

    ttk.Label(formulario_ventana, text="sum_d:").grid(row=1, column=0, pady=3, sticky='e')
    entry_sum_d = ttk.Entry(formulario_ventana, textvariable=sum_d)
    entry_sum_d.grid(row=1, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Diametro:").grid(row=2, column=0, pady=3, sticky='e')
    entry_diametro = ttk.Entry(formulario_ventana, textvariable=diametro)
    entry_diametro.grid(row=2, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Epsilon:").grid(row=3, column=0, pady=3, sticky='e')
    entry_epsilon = ttk.Entry(formulario_ventana, textvariable=epsilon)
    entry_epsilon.grid(row=3, column=1, pady=3)

    ttk.Label(formulario_ventana, text="H:").grid(row=4, column=0, pady=3, sticky='e')
    entry_h = ttk.Entry(formulario_ventana, textvariable=h)
    entry_h.grid(row=4, column=1, pady=3)

    ttk.Label(formulario_ventana, text="L:").grid(row=5, column=0, pady=3, sticky='e')
    entry_l = ttk.Entry(formulario_ventana, textvariable=l)
    entry_l.grid(row=5, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Tolerancia:").grid(row=6, column=0, pady=3, sticky='e')
    entry_tolerancia = ttk.Entry(formulario_ventana, textvariable=tolerancia)
    entry_tolerancia.grid(row=6, column=1, pady=3)

    ttk.Label(formulario_ventana, text="z_2:").grid(row=7, column=0, pady=3, sticky='e')
    entry_z2 = ttk.Entry(formulario_ventana, textvariable=z_2)
    entry_z2.grid(row=7, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Sum_km:").grid(row=8, column=0, pady=3, sticky='e')
    entry_sum_km = ttk.Entry(formulario_ventana, textvariable=sum_km)
    entry_sum_km.grid(row=8, column=1, pady=3)

    ttk.Label(formulario_ventana, text="u:").grid(row=9, column=0, pady=3, sticky='e')
    entry_u = ttk.Entry(formulario_ventana, textvariable=u)
    entry_u.grid(row=9, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Viscosidad:").grid(row=10, column=0, pady=3, sticky='e')
    entry_viscosidad = ttk.Entry(formulario_ventana, textvariable=viscosidad)
    entry_viscosidad.grid(row=10, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Densidad:").grid(row=11, column=0, pady=3, sticky='e')
    entry_densidad = ttk.Entry(formulario_ventana, textvariable=densidad)
    entry_densidad.grid(row=11, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Iteraciones:").grid(row=12, column=0, pady=3, sticky='e')
    entry_iteraciones = ttk.Entry(formulario_ventana, textvariable=iteraciones)
    entry_iteraciones.grid(row=12, column=1, pady=3)

    resultado_label = ttk.Label(formulario_ventana, text="") # Crear un label para mostrar el resultado
    resultado_label.grid(row=14, column=0, columnspan=2, padx=10, pady=10) # Estilo del label

    # Crear el widget Treeview para la tabla
    tree = ttk.Treeview(formulario_ventana, columns=("Iteración", "diametro", "velocidad", "Q", "Q>=qd"), show="headings") 
    tree.grid(row=15, column=0, columnspan=2, padx=10, pady=10) # Estilo de la tabla

    # Configurar las columnas de la tabla
    tree.heading("#1", text="Iteración") 
    tree.heading("#2", text="diametro")
    tree.heading("#3", text="velocidad")
    tree.heading("#4", text="Q")
    tree.heading("#5", text="Q>=qd")

    # 
    tree.column("#1", anchor="center")
    tree.column("#2", anchor="center")
    tree.column("#3", anchor="center")
    tree.column("#4", anchor="center")
    tree.column("#5", anchor="center")

    formulario_ventana.grid_columnconfigure(0, weight=1)
    formulario_ventana.grid_columnconfigure(1, weight=1)

    return {
        "ventana": formulario_ventana,
        "qd": entry_qd,
        "sum_d": entry_sum_d,
        "epsilon": entry_epsilon,
        "diametro": diametro,
        "h": entry_h,
        "l": entry_l,
        "tolerancia": entry_tolerancia,
        "viscosidad": entry_viscosidad,
        "z_2": entry_z2,
        "sum_km": entry_sum_km,
        "u": entry_u,
        "densidad": entry_densidad,
        "iteraciones": entry_iteraciones,
        "resultado_label": resultado_label,
        "tree": tree
    }

def calcular(data):
    # Se obtienen los valores de los campos del formulario
    try:

        qd = float(data["qd"].get())
        sum_d = float(data["sum_d"].get())
        epsilon = float(data["epsilon"].get())
        h = float(data["h"].get())
        l = float(data["l"].get())
        diametro = float(data["diametro"].get())
        viscosidad = float(data["viscosidad"].get())
        tolerancia = float(data["tolerancia"].get())
        z_2 = float(data["z_2"].get())
        sum_km = float(data["sum_km"].get())
        u = float(data["u"].get())
        densidad = float(data["densidad"].get())
        iteraciones = int(data["iteraciones"].get())
    except ValueError:
        messagebox.showerror(title="Error de tipo de dato", message="Los valores ingresados deben ser números")
        return
    area = math.pi * (sum_d**2) / 4
    
    # 
    hl = h - z_2

    # Se crea una lista con los diámetros comerciales
                        #  0.0127 === 0.0127
    diam_comerciales = [0.0127, 0.0191, 0.0254, 0.0508, 0.106, 0.1524, 0.2032, 0.254,
                        0.3048, 0.3556, 0.4064, 0.4572, 0.508, 0.6096, 0.7112, 0.8128,
                        0.9144, 1.016, 1.2192]
    
    data["tree"].delete(*data["tree"].get_children())
        
    # Iterar hasta que se cumpla la condición de caudal
    for i in range(iteraciones):
        
        # Calcular la velocidad
        resultado_velocidad = calcular_velocidad(diametro, epsilon, hl, viscosidad, l)
        # Calcular el caudal
        q = resultado_velocidad * area
        # Almacenar Sí o no en la variable cumplido dependiendo de si se cumple la condición de caudal
        cumplido = "Sí" if q >= qd else "No"

        # Actualizar la tabla con los resultados de la iteración
        data["tree"].insert("", "end", values=(i + 1, diametro, resultado_velocidad, q, cumplido))

        # verificar si se cumple la condición de caudal Q>=Qd
        if q >= qd:            
            # Calcular un nuevo valor de hl
            hl_iteracion = perdida_friccion(h, z_2, sum_km, resultado_velocidad) # Calcular la pérdida de carga por fricción
            # Verificar si la diferencia entre la pérdida de carga inicial y la pérdida de carga de la iteración es 
            # menor o igual a la tolerancia
            if hl - hl_iteracion <= tolerancia:
                if q >= qd:
                    mensaje = f"El diámetro seleccionado en la iteración {i +1} es {diametro} m" # Crear el mensaje de resultado
                    data["resultado_label"].config(text=mensaje) # Mostrar el resultado en el label                    
                    break # Salir del ciclo
                else:
                    for diam_comer in diam_comerciales: # Iterar sobre los diámetros comerciales
                        if diametro == diam_comer: # Verificar si el diámetro es igual al diámetro comercial                                                    
                            hl = h - z_2 # Calcular nuevo valor de hl
                            break # Salir del ciclo
                        else:
                            diametro = diametro + sum_d # Calcular nuevo valor de diámetro
                            hl = h - z_2 # Calcular nuevo valor de hl
                            break # Salir del ciclo
            else:
                resultado_velocidad = calcular_velocidad(diametro, epsilon, hl, viscosidad, l) # Calcular nueva velocidad
                q = resultado_velocidad * area # Calcular nuevo caudal
                hl_iteracion = perdida_friccion(h, z_2, sum_km, resultado_velocidad) # Calcular nueva pérdida de carga por fricción
                break # Salir del ciclo
        else:
            # 0.0127
            for diam_comer in diam_comerciales: # Iterar sobre los diámetros comerciales
                if diametro == diam_comer: # Verificar si el diámetro es igual al diámetro comercial
                    diametro = diam_comer # Asignar el diametro inicial por el diámetro comercial
                    resultado_velocidad = calcular_velocidad(diametro, epsilon, hl, viscosidad, l) # Calcular nueva velocidad
                    break # Salir del ciclo
                else:                    
                    diametro = diametro + sum_d # Calcular nuevo valor de diámetro
                    resultado_velocidad = calcular_velocidad(diametro, epsilon, hl, viscosidad, l) # Calcular nueva velocidad
                    break # Salir del ciclo
            