import tkinter as tk
import math
from tkinter import messagebox
from tkinter import ttk

from utils.factor_fraccion import calcular_factor_friction
from utils.potencia import calcular_h, calcular_hf, calcular_hl, calcular_nr, calcular_p, calcular_rugosidad_relativa

def calculo_potencia_tuberias():
    data = formulario()
    def on_button_click():
        calcular(data)

    boton_calcular = ttk.Button(data["ventana"], text="Calcular", command=on_button_click, style="TButton")
    boton_calcular.grid(row=10, column=0, columnspan=2, pady=15)
    # Aquí puedes agregar la lógica para el cálculo de potencia de tuberías
    # messagebox.showinfo("Cálculo de Potencia de Tuberías", "Funcionalidad en desarrollo")
def formulario():
    formulario_ventana = tk.Toplevel()
    formulario_ventana.title("Formulario de cálculo de potencia de tuberías simples")
    q = tk.StringVar()
    diametro = tk.StringVar()
    epsilon = tk.StringVar()
    sum_hm = tk.StringVar()
    l = tk.StringVar()
    densidad = tk.StringVar()
    viscosidad = tk.StringVar()
    z2 = tk.StringVar()

    ttk.Label(formulario_ventana, text="Caudal (Q):").grid(row=0, column=0, pady=3, padx=10, sticky='e')
    entry_q = ttk.Entry(formulario_ventana, textvariable=q)
    entry_q.grid(row=0, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="Diámetro (D):").grid(row=1, column=0, pady=3, padx=10, sticky='e')
    entry_diametro = ttk.Entry(formulario_ventana, textvariable=diametro)
    entry_diametro.grid(row=1, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="Rugosidad (ε):").grid(row=2, column=0, pady=3, padx=10, sticky='e')
    entry_epsilon = ttk.Entry(formulario_ventana, textvariable=epsilon)
    entry_epsilon.grid(row=2, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="Suma de Hm:").grid(row=3, column=0, pady=3, padx=10, sticky='e')
    entry_sum_hm = ttk.Entry(formulario_ventana, textvariable=sum_hm)
    entry_sum_hm.grid(row=3, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="Longitud (L):").grid(row=4, column=0, pady=3, padx=10, sticky='e')
    entry_l = ttk.Entry(formulario_ventana, textvariable=l)
    entry_l.grid(row=4, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="Densidad (ρ):").grid(row=5, column=0, pady=3, padx=10, sticky='e')
    entry_densidad = ttk.Entry(formulario_ventana, textvariable=densidad)
    entry_densidad.grid(row=5, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="n:").grid(row=6, column=0, pady=3, padx=10, sticky='e')
    entry_viscosidad = ttk.Entry(formulario_ventana, textvariable=viscosidad)
    entry_viscosidad.grid(row=6, column=1, pady=3, padx=10)

    ttk.Label(formulario_ventana, text="z_2:").grid(row=7, column=0, pady=3, padx=10, sticky='e')
    entry_z2 = ttk.Entry(formulario_ventana, textvariable=z2)
    entry_z2.grid(row=7, column=1, pady=3, padx=10)

    resultado_label = ttk.Label(formulario_ventana, text="")
    resultado_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

    formulario_ventana.grid_columnconfigure(0, weight=1)
    formulario_ventana.grid_columnconfigure(1, weight=1)

    return {
        "ventana": formulario_ventana,
        "q": entry_q,
        "diametro": entry_diametro,
        "epsilon": entry_epsilon,
        "sum_hm": entry_sum_hm,
        "l": entry_l,
        "densidad": entry_densidad,
        "viscosidad": entry_viscosidad,
        "z2": entry_z2,
        "resultado_label": resultado_label
    }

def calcular(data):
    try:
        q = float(data["q"].get())
        diametro = float(data["diametro"].get())
        epsilon = float(data["epsilon"].get())
        sum_hm = float(data["sum_hm"].get())
        l = float(data["l"].get())
        densidad = float(data["densidad"].get())
        viscosidad = float(data["viscosidad"].get())
        z2 = float(data["z2"].get())
    except ValueError:
        messagebox.showerror("Error", "Los valores ingresados deben ser numéricos")
        return
    area = math.pi * (diametro / 2) ** 2
    velocidad = q / area

    resultado_nr = calcular_nr(velocidad, diametro, densidad, viscosidad)
    resultado_rugosidad_relativa = calcular_rugosidad_relativa(epsilon, diametro)

    resultado_friccion = calcular_factor_friction(diametro, epsilon, resultado_nr)

    resultado_hl = calcular_hl(resultado_friccion, l, velocidad, diametro)

    resultado_hf = calcular_hf(resultado_hl, sum_hm)

    resultado_h = calcular_h(z2, resultado_hf)

    resultado_p = calcular_p(densidad, q, resultado_h)

    mensaje = f"El resultado de P: {resultado_p}"
    data["resultado_label"].config(text=mensaje)

    


