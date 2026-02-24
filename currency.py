class Currency:
    """Модель валюты."""

    _next_id = 1

    def __init__(self, num_code: str, char_code: str, name: str,
                 value: float, nominal: int = 1):
        self._id = Currency._next_id
        Currency._next_id += 1
        self._num_code = num_code
        self._char_code = char_code
        self._name = name
        self._value = value
        self._nominal = nominal

    @property
    def id(self) -> int:
        return self._id

    @property
    def num_code(self) -> str:
        return self._num_code

    @property
    def char_code(self) -> str:
        return self._char_code

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> float:
        return self._value

    @property
    def nominal(self) -> int:
        return self._nominal

    @value.setter
    def value(self, new_value: float):
        """Обновить курс валюты."""
        if not isinstance(new_value, (int, float)) or new_value < 0:
            raise ValueError("Курс валюты должен быть неотрицательным числом")
        self._value = float(new_value)

    def get_value_per_unit(self) -> float:
        """Вернуть курс за 1 единицу валюты (с учётом номинала)."""
        return self._value / self._nominal