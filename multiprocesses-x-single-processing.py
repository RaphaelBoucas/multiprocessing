#Este código exemplifica a diferença na execução de uma função utilizando o paralelismo e a mesma função 
#sendo executada em um único processo.


from multiprocessing import Pool
import time
import os

cpus = os.cpu_count()

def any_func(number):
    acc = 0
    for i in range(number):
        acc += (3 * 3)*2332423423
    return acc

if __name__ == '__main__':
    

    numbers = [180_000_000, 20_000_000, 150_000_000, 30_000_000, 50_000_000, 30_000_000, 150_000_000, 30_000_000, 50_000_000, 30_000_000]


    print("##############################################################################################")
    print(f"Execução de programa utilizando paralelismo (multiprocessing):")
    print(f"Esse computador possui {cpus} CPUs.")
    
    p = Pool()
    start_time = time.time()  # Start time
    result = p.map(any_func, numbers)
    p.close()
    p.join()
    
    
    end_time = time.time()  # End time
    
    print(f"Resultado: ", result)
    print(f"Para a conclusão da função any_func() foram necessários: {end_time - start_time:.2f} segundos")
    print("##############################################################################################")
    print("")
    print("")
    print("##############################################################################################")
    print(f"Execução de programa utilizando um único processo (single-process):")
    
    start_time = time.time()  # Start time
    
    for i in numbers:
        any_func(i)
    
    end_time = time.time()  # End time
    print(f"Resultado: ", result)
    print(f"Para a conclusão da função any_func() foram necessários: {end_time - start_time:.2f} segundos")
    print("##############################################################################################")
    




