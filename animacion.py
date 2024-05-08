
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import constantes as cte


def update(n, x, norm, line_norm):
    line_norm.set_data(x, norm[:, n])
    line_norm.set_label('Prob')
    return line_norm,


def make_anim(norma, x, path):
    name = "norma T=10000, n_ciclos=250, h=0.001, lambda=0.8,normalizado"
    file_out = path + "/" + name  # Nombre del fichero de salida (sin extensión)
    interval = 15  # Tiempo entre fotogramas en milisegundos

    # False: muestra la animación por pantalla
    # True: la guarda en un fichero
    save_to_file = True

    dpi = 150  # Calidad del vídeo de salida (dots per inch)

    # Crea los objetos figure y axis
    fig, ax = plt.subplots()

    # Define el rango de los ejes
    ax.set_xlim([np.min(x), np.max(x)])
    ax.set_ylim([np.min(norma), np.max(norma)])

    # Inicializa la gráfica con los datos del primer fotograma
    line, = ax.plot(x, norma[:, 0])

    height = cte.landa if cte.landa < 1 else cte.landa / (cte.landa + 1)
    ax.fill_between(x[2 * cte.N // 5: 3 * cte.N // 5], 0, height, color='orange')

    # Calcula el nº de fotogramas o instantes de tiempo
    nframes = norma.shape[1]

    # Si hay más de un instante de tiempo, genera la animación
    if nframes > 1:
        animation = FuncAnimation(
            fig, update,
            fargs=(x, norma, line), frames=nframes, blit=True, interval=interval)

        # Muestra por pantalla o guarda según parámetros
        if save_to_file:
            animation.save("{}.mp4".format(file_out), dpi=dpi)
        else:
            plt.show()
    # En caso contrario, muestra o guarda una imagen
    else:
        # Muestra por pantalla o guarda según parámetros
        if save_to_file:
            fig.savefig("{}.pdf".format(file_out))
        else:
            plt.show()
