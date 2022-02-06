# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    fig = plt.figure()
    fig.suptitle('Población histórica mundial', fontsize=16)
    ax1 = fig.add_subplot(2, 2, 1)  # 1 fila, 2 columnas, axes nº1
    ax2 = fig.add_subplot(2, 2, 2)  # 1 fila, 2 columnas, axes nº2
    ax3 = fig.add_subplot(2, 2, 3)  # 1 fila, 2 columnas, axes nº3
    ax4 = fig.add_subplot(2, 2, 4)  # 1 fila, 2 columnas, axes nº4

    # Como los datos no están ordenados por año
    # el plot no funcionará bien en este caso

    ax1.plot(x, y1, c='red', label = 'Y al cuadrado')
    ax1.legend()
    ax1.grid()
 
    ax2.plot(x, y2, c='blue', label = 'Y al cubo')
    ax2.legend()
    ax2.grid()

    ax3.scatter(x, y3, c='green', label = 'Y a la cuarta')
    ax3.legend()
    ax3.grid()

    ax4.scatter(x, y4, c='orange', label = 'raiz cuadrada de X')
    ax4.legend()
    ax4.grid()
    plt.show()
    print("Fin scatter plot")
    print("terminamos")
