from field.field import field
from gen_random.gen_random import gen_random
from unique.unique import Unique
from sort.sort import data as sort_data
from print_result.print_result import print_result
from cm_timer.cm_timer import cm_timer_1, cm_timer_2
import time

def main():
    print("=== Лабораторная работа: Функциональное программирование ===\n")

    # Тест 1: Генератор field
    print("1. Тест field - работа со словарями:")
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 3000},
        {'price': 2500, 'color': 'white'},
        {'title': 'Стул', 'price': None, 'color': 'brown'}
    ]

    print("   • Один аргумент 'title':")
    for title in field(goods, 'title'):
        print(f"     {title}")

    print("\n   • Несколько аргументов 'title', 'price':")
    for item in field(goods, 'title', 'price'):
        print(f"     {item}")

    # Тест 2: Генератор случайных чисел
    print("\n2. Тест gen_random - генератор случайных чисел:")
    print("   • 5 чисел от 1 до 3:", list(gen_random(5, 1, 3)))
    print("   • 10 чисел от 0 до 100:", list(gen_random(10, 0, 100)))

    # Тест 3: Итератор Unique - удаление дубликатов
    print("\n3. Тест Unique - удаление дубликатов:")

    print("   • Числа:", list(Unique([1, 1, 1, 2, 2, 2])))

    strings_data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print("   • Строки (разный регистр):", list(Unique(strings_data)))
    print("   • Строки (игнорировать регистр):", list(Unique(strings_data, ignore_case=True)))

    print("   • С генератором:", list(Unique(gen_random(10, 1, 3))))

    # Тест 4: Сортировка по модулю
    print("\n4. Тест сортировки по модулю:")
    print("   • Исходные данные:", sort_data)

    result1 = sorted(sort_data, key=abs, reverse=True)
    result2 = sorted(sort_data, key=lambda x: abs(x), reverse=True)

    print("   • Без lambda:", result1)
    print("   • С lambda:", result2)
    print("   • Результаты совпадают:", result1 == result2)

    # Тест 5: Декоратор print_result
    print("\n5. Тест print_result - декоратор для вывода результатов:")

    @print_result
    def simple_number():
        return 42

    @print_result
    def simple_string():
        return "Hello BMSTU"

    @print_result
    def simple_dict():
        return {'name': 'Ivan', 'age': 20}

    @print_result
    def simple_list():
        return [1, 2, 3, 4, 5]

    simple_number()
    simple_string()
    simple_dict()
    simple_list()

    # Тест 6: Контекстные менеджеры для замера времени
    print("\n6. Тест cm_timer - контекстные менеджеры:")

    print("   • cm_timer_1 (на основе класса):")
    with cm_timer_1():
        time.sleep(1.2)

    print("   • cm_timer_2 (с использованием contextlib):")
    with cm_timer_2():
        time.sleep(0.8)

    print("\n=== Все тесты завершены! ===")

if __name__ == '__main__':
    main()
