from typing import List


def check_input_data(input_data: str) -> List[str | int]:
    """
    Проверяет формат введенных данных
    :param input_data: Введенные данные
    :return: Проверенные данные
    """
    input_data: List[str | int] = input_data.split(" ")
    try:
        time_worked = int(input_data.pop(-1))
        if time_worked < 0:
            raise ValueError
        if not input_data:
            raise ValueError
        input_data.append(time_worked)
        return input_data
    except ValueError:
        raise ValueError
