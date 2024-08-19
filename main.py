# ЗАДАНИЕ
# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
#
# # Параметры нормального распределения
#
# mean = 0 # Среднее значение
#
# std_dev = 1 # Стандартное отклонение
#
# num_samples = 1000 # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
#
# data = np.random.normal(mean, std_dev, num_samples)
#
# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.
#
# import numpy as np
#
# random_array = np.random.rand(5) # массив из 5 случайных чисел
#
# print(random_array)
#
# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

# Настройка заголовков и меток
plt.title('Гистограмма случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()


# Количество точек данных
num_points = 5

# Генерация двух наборов случайных данных
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='blue', alpha=0.5, edgecolor='black')

# Настройка заголовков и меток
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Показать диаграмму
plt.show()




browser = webdriver.Firefox()

url = 'https://www.divan.ru/category/divany-i-kresla'
browser.get(url)
time.sleep(5)  # Даем время для загрузки страницы

prices = []
product_elements = browser.find_elements(By.CLASS_NAME, '_Ud0k')

for price_element in product_elements:
    prices.append(price_element.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text)

browser.quit()

# Сохраняем данные в CSV
df_prices = pd.DataFrame({'Цена': prices})
df_prices.to_csv('divan_prices.csv', index=False)
