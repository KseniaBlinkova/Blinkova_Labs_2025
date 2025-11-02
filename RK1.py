from operator import itemgetter

class Driver:
    def __init__(self, id, fio, salary, park_id):
        self.id = id
        self.fio = fio
        self.salary = salary
        self.park_id = park_id

class Park:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DriverPark:
    def __init__(self, park_id, driver_id):
        self.park_id = park_id
        self.driver_id = driver_id

parks = [
    Park(1, 'Восточный автопарк'),
    Park(2, 'Западный автопарк'),
    Park(3, 'Северный автопарк'),
    Park(11, 'Восточный отдел логистики'),
    Park(22, 'Западный отдел транспорта'),
    Park(33, 'Центральный отдел грузоперевозок'),
]

drivers = [
    Driver(1, 'Алексеев', 25000, 1),
    Driver(2, 'Антонов', 35000, 2),
    Driver(3, 'Кузнецов', 45000, 3),
    Driver(4, 'Иванов', 35000, 3),
    Driver(5, 'Петров', 25000, 3),
    Driver(6, 'Сидоров', 40000, 11),
    Driver(7, 'Никитин', 30000, 22),
]

drivers_parks = [
    DriverPark(1, 1),
    DriverPark(2, 2),
    DriverPark(3, 3),
    DriverPark(3, 4),
    DriverPark(3, 5),
    DriverPark(11, 6),
    DriverPark(22, 7),
    DriverPark(33, 1),
    DriverPark(33, 3),
]

def main():
    one_to_many = [(d.fio, d.salary, p.name)
                   for p in parks
                   for d in drivers
                   if d.park_id == p.id]

    many_to_many_temp = [(p.name, dp.park_id, dp.driver_id)
                         for p in parks
                         for dp in drivers_parks
                         if p.id == dp.park_id]

    many_to_many = [(d.fio, d.salary, park_name)
                    for park_name, park_id, driver_id in many_to_many_temp
                    for d in drivers if d.id == driver_id]

    print('Задание A1')
    print('Список всех связанных водителей и автопарков, отсортированный по автопаркам:')

    sorted_by_parks_and_names = sorted(one_to_many, key=itemgetter(2, 0))

    for item in sorted_by_parks_and_names:
        print(f"  {item[2]}: {item[0]} - {item[1]} руб.")

    print('\nЗадание A2')
    print('Список автопарков с суммарной зарплатой водителей, отсортированный по суммарной зарплате:')
    parks_total_salary_unsorted = []
    for p in parks:
        p_drivers = list(filter(lambda i: i[2] == p.name, one_to_many))
        if len(p_drivers) > 0:
            p_sals = [sal for _, sal, _ in p_drivers]
            p_sals_sum = sum(p_sals)
            parks_total_salary_unsorted.append((p.name, p_sals_sum))

    parks_sorted_by_salary = sorted(parks_total_salary_unsorted, key=itemgetter(1), reverse=True)
    for item in parks_sorted_by_salary:
        print(f"  {item[0]}: {item[1]} руб.")

    print('\nЗадание A3')
    print('Список автопарков, у которых в названии присутствует слово "отдел", и список работающих в них водителей:')
    parks_with_drivers = {}
    for p in parks:
        if 'отдел' in p.name.lower():
            p_drivers = list(filter(lambda i: i[2] == p.name, many_to_many))
            p_drivers_names = [x for x, _, _ in p_drivers]
            parks_with_drivers[p.name] = p_drivers_names

    for park_name, drivers_list in parks_with_drivers.items():
        print(f"  {park_name}: {', '.join(drivers_list)}")

if __name__ == '__main__':
    main()
