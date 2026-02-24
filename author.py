class Author:
    """Модель автора приложения."""

    def __init__(self, name: str, group: str):
        self._name = name
        self._group = group

    # Геттеры
    @property
    def name(self) -> str:
        return self._name

    @property
    def group(self) -> str:
        return self._group

    # Сеттеры с проверкой
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя автора должно быть непустой строкой")
        self._name = value.strip()

    @group.setter
    def group(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Группа должна быть непустой строкой")
        self._group = value.strip()