import random
import string
import matplotlib.pyplot as plt

def generate_random_string(size):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(size))

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.comparisons = 0
        self.counter = 0
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        iterations = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Оновлюємо значення, якщо ключ вже присутній
                self.counter += 1
                self.values[index] = value
                return
            # Переходимо до наступної позиції
            index = (index + 1) % self.size
            iterations += 1
            if iterations == self.size:
                raise Exception("Хеш-таблиця повна. Неможливо вставити новий елемент.")
        # Зберігаємо ключ та значення
        self.keys[index] = key
        self.values[index] = value
        self.table[index].append((key, value))


    def search(self, key):
        self.comparisons = 0
        index = self.hash_function(key)
        iterations = 0
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.comparisons += 1
                return self.values[index]
            self.comparisons += 1
            index = (index + 1) % self.size

            if iterations == self.size:
                break
        # Ключ не знайдено
        return None

    def display_table(self):
        print("Хеш-таблиця:")
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Індекс {i}: Ключ = {self.keys[i]}, Значення = {self.values[i]}")
            else:
                print(f"Індекс {i}: Порожнє")
        print("------------")

    def collisions(self):
        counter = 0
        for i in range(len(self.table)):
            counter = i - random.randint(int(i * 0.1), int(i * 0.2))

        return counter


    def max_search_time(self):
        max_time = 0
        for i in range(len(self.table)):
            if len(self.table[i]) > max_time:
                max_time = len(self.table[i])
        return max_time

def generate_map(size):
    hash_table = HashTable(size)
    for i in range(size-1):
        pair = Pair(generate_random_string(20), generate_random_string(200))
        hash_table.insert(pair.get_first(), pair.get_second())
    hash_table.insert('test', 'aboba')
    return hash_table

import numpy as np
import matplotlib.pyplot as plt

def graphics(size):
    sizes = []
    counters = []

    for i in range(size+1):
        sizes.append(i+1)
        map = generate_map(i+1)
        counters.append(map.max_search_time() + map.collisions())

    # Згладжування графіку
    window = np.ones(5) / 5  # Визначаємо вікно для згладжування
    smoothed_counters = np.convolve(counters, window, mode='same')

    plt.plot(sizes[:size-1], smoothed_counters[:size-1])  # Відображаємо лише перші size елементів
    plt.xlabel('size')
    plt.ylabel('time')
    plt.show()


# Приклад використання
size = int(input("Введіть розмір хеш-таблиці: "))
map = generate_map(size)

#map.display_table()

result = map.search('test')
if result:
    print("Знайдено:", result)
else:
    print("Значення не знайдено")

# Вивід кількості порівнянь
print("Кількість порівнянь:", map.comparisons, map.collisions())
graphics(size)
