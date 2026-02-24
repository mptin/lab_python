from typing import List, Optional


class User:
    """Модель пользователя."""

    _next_id = 1  # Счётчик для генерации ID

    def __init__(self, name: str):
        self._id = User._next_id
        User._next_id += 1
        self._name = name
        self._subscriptions: List[int] = []  # Список ID валют

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def subscriptions(self) -> List[int]:
        return self._subscriptions.copy()  # Возвращаем копию для безопасности

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой")
        self._name = value.strip()

    def subscribe(self, currency_id: int):
        """Подписать пользователя на валюту."""
        if not isinstance(currency_id, int) or currency_id < 0:
            raise ValueError("ID валюты должен быть положительным числом")
        if currency_id not in self._subscriptions:
            self._subscriptions.append(currency_id)

    def unsubscribe(self, currency_id: int):
        """Отписать пользователя от валюты."""
        if currency_id in self._subscriptions:
            self._subscriptions.remove(currency_id)

    def is_subscribed(self, currency_id: int) -> bool:
        """Проверить, подписан ли пользователь на валюту."""
        return currency_id in self._subscriptions