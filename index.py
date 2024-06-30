# Importar la librería tkinter con el alias "tk"
import tkinter as tk

# Importar funciones desde módulos en otros archivos
# Aquí estás importando funciones desde diferentes archivos
# comprobacion_diseno_tuberias, calculo_factor_friccion, calculo_potencia_tuberias, diseno_tuberias_simples
from screens.comprobacion_diseno.comprobacion import comprobacion_diseno_tuberias
from screens.calculo_factor.factor import calculo_factor_friccion
from screens.calculo_potencia.potencia import calculo_potencia_tuberias
from screens.diseno_tuberias.diseno import diseno_tuberias_simples

# Definición de la función principal "main"
def main():
    # Crear una ventana principal usando tkinter
    ventana = tk.Tk()

    # Establecer el título de la ventana
    ventana.title("Herramientas de Ingeniería para Tuberías")

    # Establecer el tamaño de la ventana
    ventana.geometry("500x250")

    # Ancho fijo para todos los botones
    ancho_botones = 30

    # Crear un botón para la comprobación de diseño de tuberías
    boton_comprobacion_diseno = tk.Button(ventana, text="Comprobación de Diseño Tuberías", command=comprobacion_diseno_tuberias, width=ancho_botones)
    # Empaquetar el botón en la ventana y añadir un espacio vertical
    boton_comprobacion_diseno.pack(pady=10)

    # Crear un botón para el cálculo del factor de fricción
    boton_calculo_friccion = tk.Button(ventana, text="Cálculo de Factor de Fricción", command=calculo_factor_friccion, width=ancho_botones)
    # Empaquetar el botón en la ventana y añadir un espacio vertical
    boton_calculo_friccion.pack(pady=10)

    # Crear un botón para el cálculo de la potencia de tuberías
    boton_calculo_potencia = tk.Button(ventana, text="Cálculo de Potencia de Tuberías", command=calculo_potencia_tuberias, width=ancho_botones)
    # Empaquetar el botón en la ventana y añadir un espacio vertical
    boton_calculo_potencia.pack(pady=10)

    # Crear un botón para el diseño de tuberías simples
    boton_diseno_tuberias_simples = tk.Button(ventana, text="Diseño de Tuberías Simples", command=diseno_tuberias_simples, width=ancho_botones)
    # Empaquetar el botón en la ventana y añadir un espacio vertical
    boton_diseno_tuberias_simples.pack(pady=10)

    # Iniciar el bucle principal de la interfaz gráfica
    ventana.mainloop()

# Verificar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    # Llamar a la función principal "main"
    main()
