import json
import sys
import random
from print_result.print_result import print_result
from cm_timer.cm_timer import cm_timer_1

# Получаем путь к файлу из аргументов командной строки
path = sys.argv[1] if len(sys.argv) > 1 else "data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    # Отсортированный список профессий без повторений (игнорируя регистр)
    return sorted(set(item.get("job-name", "") for item in arg), key=lambda s: s.lower())

@print_result
def f2(arg):
    # Фильтруем профессии, содержащие слово "программист"
    return list(filter(lambda s: "программист" in s.lower(), arg))

@print_result
def f3(arg):
    # Добавляем "с опытом Python" к каждой профессии
    return list(map(lambda job: f"{job} с опытом Python", arg))

@print_result
def f4(arg):
    # Генерируем зарплаты и объединяем с профессиями
    salaries = [random.randint(100000, 200000) for _ in range(len(arg))]
    return [f"{prof}, зарплата {salary} руб." for prof, salary in zip(arg, salaries)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
