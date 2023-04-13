import pandas as pd
import numpy as np
import random
from scipy.stats import ks_2samp




chat_id = 628156322 # Ваш chat ID, не меняйте название переменной

def solution(data) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
# чтение данных из файлов
data_hist = np.loadtxt('historical_data.csv')
data1 = np.loadtxt('modified_data_of_type_1.csv')
data2 = np.loadtxt('modified_data_of_type_2.csv')
data3 = np.loadtxt('modified_data_of_type_3.csv')

# вычисление эмпирических функций распределения
ecdf_hist = np.arange(1, len(data_hist) + 1) / len(data_hist)
ecdf1 = np.arange(1, len(data1) + 1) / len(data1)
ecdf2 = np.arange(1, len(data2) + 1) / len(data2)
ecdf3 = np.arange(1, len(data3) + 1) / len(data3)

# вычисление статистики критерия Колмогорова-Смирнова
ks_stat1, p_value1 = ks_2samp(data_hist, data1)
ks_stat2, p_value2 = ks_2samp(data_hist, data2)
ks_stat3, p_value3 = ks_2samp(data_hist, data3)

# сравнение полученной статистики с критическим значением
n = len(data_hist)
alpha = 0.04
critical_value = np.sqrt(-0.5 * np.log(alpha / 2)) / np.sqrt(n)
if ks_stat1 > critical_value or ks_stat2 > critical_value or ks_stat3 > critical_value:
    print(True)
else:
    print(False)











    return random_bool
