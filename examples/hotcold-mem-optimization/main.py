import pandas as pd
from h5py import File

# Создаем данные для холодного хотпаса
cold_mem_data = pd.DataFrame({'cold': [1, 2, 3], 'hot': [4, 5, 6]})

# Создаем данные для кеша
cache_data = pd.DataFrame({'hot': [7, 8, 9], 'cold': [10, 11, 12]})

# Размещаем данные в холодном хотпасе
cold_mem_data.to_hdf('cold_mem_data.h5', 'cold_mem_data')

# Размещаем данные в кеше
cache_data.to_hdf('cache_data.h5', 'cache_data')

if __name__ == "__main__":
    # Чтение данных из холодного хотпаса
    with File('cold_mem_data.h5', 'r') as f:
        cold_mem_data_from_hdf = f['cold_mem_data'][()]

    # Чтение данных из кеша
    with File('cache_data.h5', 'r') as f:
        cache_data_from_hdf = f['cache_data'][()]

    # Вывод данных
    print("Data from cold_mem_data.h5:")
    print(cold_mem_data_from_hdf)
    print("\nData from cache_data.h5:")
    print(cache_data_from_hdf)