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
import math

def calculate_distance(lat1, lng1, lat2, lng2):
    """
    Обчислює відстань між двома координатами (в кілометрах).
    """
    radius = 6371  # Радіус Землі в кілометрах

    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlng/2) * math.sin(dlng/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance

def find_shortest_route(cities):
    num_cities = len(cities)
    visited = [False] * num_cities  # Список, що позначає, чи було місто відвідане
    route = []  # Маршрут

    # Вибір початкового міста (City1)
    start_city = cities[0]
    current_city = start_city
    visited[0] = True
    route.append(start_city['name'])

    # Пошук найближчого до поточного міста
    for _ in range(num_cities - 1):
        min_distance = float('inf')
        nearest_city = None

        for city in cities:
            if not visited[cities.index(city)]:
                distance = calculate_distance(current_city['lat'], current_city['lng'],
                                              city['lat'], city['lng'])
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city

        current_city = nearest_city
        visited[cities.index(current_city)] = True
        route.append(current_city['name'])

    # Додавання останнього міста для завершення циклу
    distance = calculate_distance(current_city['lat'], current_city['lng'],
                                  start_city['lat'], start_city['lng'])
    route.append(start_city['name'])

    return route, distance

cities = [
    {'name': 'Буенос-Айрес', 'lat': -34.6037, 'lng': -58.3816},
    {'name': 'Кордова', 'lat': -31.4201, 'lng': -64.1888},
    {'name': 'Росаріо', 'lat': -32.9442, 'lng': -60.6505},
    {'name': 'Мендоса', 'lat': -32.8895, 'lng': -68.8458},
    {'name': 'Сан-Мігель-де-Тукуман', 'lat': -26.8167, 'lng': -65.2167},
    {'name': 'Ла-Плата', 'lat': -34.9206, 'lng': -57.9536},
    {'name': 'Мар-дель-Плата', 'lat': -38.0055, 'lng': -57.5426},
    {'name': 'Салта', 'lat': -24.7829, 'lng': -65.4122},
    {'name': 'Санта-Фе', 'lat': -31.6333, 'lng': -60.7000},
    {'name': 'Сан-Хуан', 'lat': -31.5375, 'lng': -68.5364},
    {'name': 'Сан-Луїс', 'lat': -33.3016, 'lng': -66.3378},
    {'name': 'Тукуман', 'lat': -26.8241, 'lng': -65.2226},
    {'name': 'Реконкіста', 'lat': -29.1395, 'lng': -59.6500},
    {'name': 'Нюкві-Берга', 'lat': -41.1335, 'lng': -71.3103},
    {'name': 'Посадас', 'lat': -27.3621, 'lng': -55.9007},
    {'name': 'Санта-Роса', 'lat': -36.6167, 'lng': -64.2833}
]

route, distance = find_shortest_route(cities)

# Виведення результатів
route_str = ' → '.join(route)
print(f"Маршрут: {route_str}, Довжина: {distance} км")
