import numpy as np
from astropy.io import fits
from sklearn.cluster import KMeans

def load_fits_data(filename):
    """Загружает данные из файла FITS."""
    hdul = fits.open(filename)
    data = hdul[0].data
    hdul.close()
    return data

def preprocess_data(data):
    """Применяет предварительную обработку данных с использованием ИИ."""
    # Пример простого алгоритма: кластеризация с KMeans
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)
    labels = kmeans.predict(data)
    return labels

def main():
    """Основная функция программы."""
    filename = 'euclid_fits_file.fits'
    data = load_fits_data(filename)
    
    print("Данные загружены. Размерность данных:", data.shape)
    
    labels = preprocess_data(data)
    print("Данные предварительно обработаны. Количество кластеров:", np.unique(labels).size)

if __name__ == "__main__":
    main()