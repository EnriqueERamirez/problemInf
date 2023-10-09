import matplotlib.pyplot as plt

def comparar_tiempos(tiempo1, tiempo2):
    plt.bar(['Algoritmo 1', 'Algoritmo 2'], [tiempo1, tiempo2])
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.savefig('results/performance_graph.png')
    plt.show()

