from .author import Author


class App:
    """Модель приложения."""

    def __init__(self, name: str, version: str, author: Author):
        self._name = name
        self._version = version
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def author(self) -> Author:
        return self._author

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Название приложения должно быть строкой")
        self._name = value.strip()

    @version.setter
    def version(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Версия должна быть строкой")
        self._version = value.strip()

    @author.setter
    def author(self, value: Author):
        if not isinstance(value, Author):
            raise ValueError("Автор должен быть объектом класса Author")
        self._author = value