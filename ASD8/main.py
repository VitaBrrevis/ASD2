"""""
Задача
комівояжера,
пошук маршруту
та його довжини

Жадібний пошук
метод включення
найближчої
вершини
 
 Для задачі комівояжера. Розробити програму, яка буде знаходити
маршрут мінімальної довжини, що включає усі міста. У якості методів
знаходження маршруту вибрати заданий за варіантом жадібний метод.
Відповідь вивести у вигляді (Маршрут: Місто1 → Місто3 → Місто4 →
Місто2 → Місто1, Довжина: 234км). 

Для задачі комівояжера, вибрати 15 міст в Аргентині і записати для них найкоротшу відстань по дорозі, у випадку прямого
сполучення між ними. Для визначення відстані рекомендується використовувати
інтернет сервіси (наприклад Google Maps).
"""""
from itertools import permutations
from math import sqrt

# Список міст в Аргентині з координатами їх центрів
cities = [
    {'name': 'City1', 'lat': 40.7128, 'lng': -74.0060},
    {'name': 'City2', 'lat': 34.0522, 'lng': -118.2437},
    {'name': 'City3', 'lat': 41.8781, 'lng': -87.6298},
    {'name': 'City4', 'lat': 29.7604, 'lng': -95.3698},
    {'name': 'City5', 'lat': 39.9526, 'lng': -75.1652},
    {'name': 'City6', 'lat': 32.7157, 'lng': -117.1611},
    {'name': 'City7', 'lat': 47.6062, 'lng': -122.3321},
    {'name': 'City8', 'lat': 37.7749, 'lng': -122.4194},
    {'name': 'City9', 'lat': 38.9072, 'lng': -77.0369},
    {'name': 'City10', 'lat': 33.4484, 'lng': -112.0740},
    {'name': 'City11', 'lat': 42.3601, 'lng': -71.0589},
    {'name': 'City12', 'lat': 45.5051, 'lng': -122.6750},
    {'name': 'City13', 'lat': 36.1699, 'lng': -115.1398},
    {'name': 'City14', 'lat': 38.5816, 'lng': -121.4944},
    {'name': 'City15', 'lat': 25.7617, 'lng': -80.1918}
]


# Функція для обчислення відстані між двома координатами
def calculate_distance(lat1, lng1, lat2, lng2):
    return sqrt((lat2 - lat1) ** 2 + (lng2 - lng1) ** 2)


# Знаходимо найкоротшу відстань між усіма парами міст
distances = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            city1 = cities[i]
            city2 = cities[j]
            distance = calculate_distance(city1['lat'], city1['lng'], city2['lat'], city2['lng'])
            distances[(city1['name'], city2['name'])] = distance


# Жадібний пошук методом включення найближчої вершини
def find_shortest_route(cities, distances):
    shortest_distance = float('inf')
    shortest_route = None

    for permutation in permutations(cities):
        route_distance = 0
        for i in range(len(permutation) - 1):
            city1 = permutation[i]
            city2 = permutation[i + 1]
            route_distance += distances[(city1['name'], city2['name'])]

        if route_distance < shortest_distance:
            shortest_distance = route_distance
            shortest_route = permutation

    return shortest_route, shortest_distance


# Знаходимо маршрут мінімальної довжини
shortest_route, shortest_distance = find_shortest_route(cities, distances)

# Формуємо відповідь
route_str = ' → '.join(city['name'] for city in shortest_route)
answer = f"Маршрут: {route_str}, Довжина: {shortest_distance}км."

# Виводимо результат
print(answer)
