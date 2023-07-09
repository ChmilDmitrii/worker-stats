from typing import List, Generator, Tuple


class Statistics:
    """
    Класс для формарования и форматирования статистики
    из введенных данных
    """

    def __init__(self, data: List[List[str | int]]):
        self.data = data
        self.statistics = dict()

    def _get_worker_info(self) -> Generator[Tuple[int, str], None, None]:
        """
        Метод отвечает за получение отработанных часов и имени работника
        :return: Generator[Tuple[int, str], None, None]
        """
        for worker_info in self.data:
            time_worked = worker_info.pop(-1)
            name = ' '.join(worker_info)
            yield time_worked, name

    def forming_statistics(self) -> None:
        """
        Формирует статистику на основе введенных данных
        :return: None
        """
        for time_worked, name in self._get_worker_info():
            if name in self.statistics.keys():
                self.statistics[name].append(time_worked)
                continue
            self.statistics[name] = [time_worked]

    def format_statistic(self) -> str:
        """
        Форматирует вывод статистики
        :return: Статистика по каждому работнику
        """
        format_stat = str()
        for key, value in self.statistics.items():
            row = f"{key}: {', '.join([str(v) for v in value])}; " \
                  f"sum: {sum(value)}\n"
            format_stat += row
        return format_stat
