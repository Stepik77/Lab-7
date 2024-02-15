import numpy as np
from time import perf_counter

lt1 = [np.random.rand() for i in range(1000000)]
lt2 = [np.random.rand() for i in range(1000000)]
array1 = np.array(lt1)
array2 = np.array(lt2)

start_time = perf_counter()
result_list = [a * b for a, b in zip(lt1, lt2)]
end_time = perf_counter()
list_time = end_time - start_time

start_time = perf_counter()
result_array = np.multiply(array1, array2)
end_time = perf_counter()
numpy_time = end_time - start_time

print(f"Время выполнения для списков: {list_time} секунд")
print(f"Время выполнения для NumPy массивов: {numpy_time} секунд")
