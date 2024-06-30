import tkinter as tk
from tkinter import ttk, messagebox
from utils.factor_fraccion import calcular_factor_friction, colebrook_white, derivada_colebrook_white, calcular_xi
import math

def calculo_factor_friccion():
    data = formulario()

    def on_button_click():
        calcular(data)

    boton_calcular = ttk.Button(data["ventana"], text="Calcular", command=on_button_click, style="TButton")
    boton_calcular.grid(row=10, column=0, columnspan=2, pady=15)

def formulario():
    # Crear una nueva ventana para el formulario
    formulario_ventana = tk.Toplevel()
    formulario_ventana.title("Formulario de cálculo")

    epsilon = tk.StringVar()    
    diametro = tk.StringVar()
    nr = tk.StringVar()    
    iteraciones = tk.IntVar(value=10)

    # Utilizamos ttk.Entry para una apariencia más moderna
    ttk.Label(formulario_ventana, text="Epsilon (ε):").grid(row=0, column=0, pady=3, sticky='e')
    entry_diametro = ttk.Entry(formulario_ventana, textvariable=epsilon)
    entry_diametro.grid(row=0, column=1, pady=3)

    ttk.Label(formulario_ventana, text="diametro (D):").grid(row=1, column=0, pady=3, sticky='e')
    entry_rugosidad = ttk.Entry(formulario_ventana, textvariable=diametro)
    entry_rugosidad.grid(row=1, column=1, pady=3)

    ttk.Label(formulario_ventana, text="N_r:").grid(row=2, column=0, pady=3, sticky='e')
    entry_H = ttk.Entry(formulario_ventana, textvariable=nr)
    entry_H.grid(row=2, column=1, pady=3)

    ttk.Label(formulario_ventana, text="Iteraciones:").grid(row=3, column=0, pady=3, sticky='e')
    entry_E = ttk.Entry(formulario_ventana, textvariable=iteraciones)
    entry_E.grid(row=3, column=1, pady=3)
    
    resultado_tuberia_simple = ttk.Label(formulario_ventana, text="")
    resultado_tuberia_simple.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    resultado_tuberia_rugosa = ttk.Label(formulario_ventana, text="")
    resultado_tuberia_rugosa.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

    # Crear el widget Treeview para la tabla
    tree = ttk.Treeview(formulario_ventana, 
                        columns=("Iteración", "Factor fricción inicial", "xi", "xi iteración"), 
                        show="headings")
    tree.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

    # Configurar las columnas de la tabla
    tree.heading("#1", text="Iteración")
    tree.heading("#2", text="Factor fricción inicial")
    tree.heading("#3", text="xi")
    tree.heading("#4", text="xi iteración")
    
    tree.column("#1", anchor="center")
    tree.column("#2", anchor="center")
    tree.column("#3", anchor="center")
    tree.column("#4", anchor="center")


    # Configurar el peso de las columnas para que se expandan con la ventana
    formulario_ventana.grid_columnconfigure(0, weight=1)
    formulario_ventana.grid_columnconfigure(1, weight=1)

    # se retorna un diccionario con todos los elementos del formulario y la tabla
    return {
        "ventana": formulario_ventana, 
        "diametro": diametro,
        "epsilon": epsilon,
        "nr": nr,
        "iteraciones": iteraciones,
        "resultado_tuberia_simple": resultado_tuberia_simple,
        "resultado_tuberia_rugosa": resultado_tuberia_rugosa,
        "tree": tree, # se retorna el widget Treeview para poder insertar los datos en la tabla
    }

def calcular(data):
    try:

        epsilon = float(data["epsilon"].get())
        diametro = float(data["diametro"].get())
        nr = float(data["nr"].get())
        iteraciones = data["iteraciones"].get()
    except ValueError:
        messagebox.showerror("Error de validación", "Al menos uno de los campos no es un número válido")
        return

    if nr <= 2000:
        f = 64 / nr
        mensaje = f"El número de Reynolds ingresado({nr}) es menor o igual 2000, se aplica 64/f = {f}"
        data["resultado_tuberia_simple"].config(text=mensaje)

    elif 2000 < nr < 4000:
        mensaje = f"El número de Reynolds ingresado({nr}) es mayor a 2000 y menor a 4000, no es permitido"
        data["resultado_tuberia_simple"].config(text=mensaje)
    else:        
        factor_friccion = calcular_factor_friction(diametro, epsilon, nr)
        xi = round(1 / math.sqrt(factor_friccion),3)
        mensaje = f"Tubería lisa con factor de fricción: {factor_friccion} y xi: {xi}"
        data["resultado_tuberia_simple"].config(text=mensaje)
        
        data["tree"].delete(*data["tree"].get_children())

        for i in range(0,iteraciones):
            fxi = colebrook_white(epsilon, diametro, xi, nr, factor_friccion)
            dfxi = derivada_colebrook_white(epsilon, diametro, xi, nr)
            xi_iteracion = calcular_xi(xi, fxi, dfxi)

            data["tree"].insert("", "end", values=(i + 1, factor_friccion, xi, xi_iteracion))

            if  xi == xi_iteracion:
                f = 1 / (xi ** 2)
                mensaje = f"En la iteración {i+1} se llegó al valor de xi: {xi_iteracion} y f: {f}"
                data["resultado_tuberia_rugosa"].config(text=mensaje)
                break
            elif xi_iteracion == math.inf or xi_iteracion == 0:
                mensaje = f"No se puede calcular el factor de fricción con el valor de xi: {xi_iteracion}"
                data["resultado_tuberia_rugosa"].config(text=mensaje)
                break
            elif i == iteraciones - 1:
                mensaje = f"No se encontró el valor de xi en las iteraciones indicadas"
                data["resultado_tuberia_rugosa"].config(text=mensaje)
                break
            else:
                xi = xi_iteracion        
        