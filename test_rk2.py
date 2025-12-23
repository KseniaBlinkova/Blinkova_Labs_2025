import pytest
from refactored_rk1 import DataService, DriverParkService


class TestDriverParkService:

    @pytest.fixture
    def service(self):
        return DriverParkService(DataService())

    def test_task_a1(self, service):
        result = service.task_a1()

        assert len(result) == 7

        park_names = [park_name for _, _, park_name in result]
        assert park_names == sorted(park_names)

        assert result[0][2] == 'Восточный автопарк'
        assert result[0][0] == 'Алексеев'
        assert result[0][1] == 25000

        northern_park_items = [item for item in result if item[2] == 'Северный автопарк']
        northern_drivers = [driver for driver, _, _ in northern_park_items]
        assert northern_drivers == ['Иванов', 'Кузнецов', 'Петров']

    def test_task_a2(self, service):
        result = service.task_a2()

        assert len(result) == 5

        salaries = [salary for _, salary in result]
        assert salaries == sorted(salaries, reverse=True)

        result_dict = dict(result)
        assert result_dict['Северный автопарк'] == 105000
        assert result_dict['Восточный отдел логистики'] == 40000
        assert result_dict['Западный автопарк'] == 35000
        assert result_dict['Западный отдел транспорта'] == 30000
        assert result_dict['Восточный автопарк'] == 25000

    def test_task_a3(self, service):
        result = service.task_a3()

        assert isinstance(result, dict)
        assert len(result) == 3

        assert 'Восточный отдел логистики' in result
        assert 'Западный отдел транспорта' in result
        assert 'Центральный отдел грузоперевозок' in result

        assert result['Восточный отдел логистики'] == ['Сидоров']
        assert result['Западный отдел транспорта'] == ['Никитин']

        central_drivers = result['Центральный отдел грузоперевозок']
        assert len(central_drivers) == 2
        assert 'Алексеев' in central_drivers
        assert 'Кузнецов' in central_drivers


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
