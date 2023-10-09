import cProfile
import timeit
from memory_profiler import profile
import line_profiler
from algorithms import algoritmo1, algoritmo2
from utils import cargar_datos

@profile
def main():
    datos = cargar_datos('data/dataset.csv')
    
    # Perfilado con cProfile
    profiler = cProfile.Profile()
    profiler.enable()
    
    resultado1 = algoritmo1(datos)
    resultado2 = algoritmo2(datos)
    
    profiler.disable()
    profiler.print_stats()

    # Benchmarking con timeit
    tiempo_algoritmo1 = timeit.timeit("algoritmo1(datos)", globals=globals(), number=10)
    tiempo_algoritmo2 = timeit.timeit("algoritmo2(datos)", globals=globals(), number=10)
    
    print(f'Tiempo promedio Algoritmo 1: {tiempo_algoritmo1 / 10} segundos')
    print(f'Tiempo promedio Algoritmo 2: {tiempo_algoritmo2 / 10} segundos')

if __name__ == "__main__":
    line_prof = line_profiler.LineProfiler()
    line_prof.add_function(algoritmo1)
    line_prof.add_function(algoritmo2)
    line_prof.run('main()')

    # Para visualizar el perfilado en tiempo real con py-spy, ejecuta en la terminal:
    # py-spy top -- python main.py

