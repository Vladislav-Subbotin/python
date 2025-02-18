import math

def task_1():
    print("\nЗадача 1: Определение скорости")
    distance = float(input("Введите расстояние в километрах: "))
    time = float(input("Введите время в часах: "))
    speed = distance / time
    print('Скорость:', speed, 'км/ч[')

def task_2():
    print("\nЗадача 2: Определение массы")
    force = float(input("Введите силу в ньютонах: "))
    acceleration = float(input("Введите ускорение в м/с²: "))
    mass = force / acceleration
    print('Масса:', mass, 'кг')

def task_3():
    print("\nЗадача 3: Определение температуры по Цельсию")
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print('Температура:', celsius, '°C')

def task_4():
    print("\nЗадача 4: Определение работы")
    force = float(input("Введите силу в ньютонах: "))
    distance = float(input("Введите расстояние в метрах: "))
    work = force * distance
    print('Работа:', work, 'Дж')

def task_5():
    print("\nЗадача 5: Определение кинетической энергии")
    mass = float(input("Введите массу в килограммах: "))
    velocity = float(input("Введите скорость в м/с: "))
    kinetic_energy = 0.5 * mass * velocity ** 2
    print('Кинетическая энергия:', kinetic_energy, 'Дж')

def task_6():
    print("\nЗадача 6: Определение потенциальной энергии")
    mass = float(input("Введите массу в килограммах: "))
    height = float(input("Введите высоту в метрах: "))
    gravity = float(input("Введите ускорение свободного падения (по умолчанию 9.81 м/с²): ") or 9.81)
    potential_energy = mass * gravity * height
    print('Потенциальная энергия:', potential_energy, 'Дж')

def task_7():
    print("\nЗадача 7: Определение давления")
    force = float(input("Введите силу в ньютонах: "))
    area = float(input("Введите площадь в квадратных метрах: "))
    pressure = force / area
    print('Давление:', pressure, 'Па')

def task_8():
    print("\nЗадача 8: Определение теплоты")
    mass = float(input("Введите массу в килограммах: "))
    specific_heat = float(input("Введите удельную теплоёмкость: "))
    delta_temp = float(input("Введите изменение температуры в °C: "))
    heat = mass * specific_heat * delta_temp
    print('Количество теплоты:', heat, 'Дж')

def task_9():
    print("\nЗадача 9: Определение частоты")
    period = float(input("Введите период колебаний в секундах: "))
    frequency = 1 / period
    print('Частота:', frequency, 'Гц')

def task_10():
    print("\nЗадача 10: Определение объема цилиндра")
    radius = float(input("Введите радиус основания в метрах: "))
    height = float(input("Введите высоту цилиндра в метрах: "))
    volume = math.pi * radius ** 2 * height
    print('Объем цилиндра:', volume, 'м³')


def main():
    tasks = {
        1: task_1,
        2: task_2,
        3: task_3,
        4: task_4,
        5: task_5,
        6: task_6,
        7: task_7,
        8: task_8,
        9: task_9,
        10: task_10,
    }

    while True:
        print("\nВыберите задачу (1-10) или введите 'q' для выхода:")
        user_input = input("> ")

        if user_input == 'q':
            print("Выход из программы.")
            break

        try:
            task_number = int(user_input)
            if task_number < 1 or task_number > 10:
                print("Пожалуйста, введите число от 1 до 10.")
                continue

            task = tasks[task_number]
            task()
        except ValueError:
            print("Пожалуйста, введите число от 1 до 10 или 'q' для выхода.")
main()