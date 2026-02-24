import requests
from logger import logger


def get_currencies(currency_codes: list, url="https://www.cbr-xml-daily.ru/daily_json.js") -> dict:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as err:
        raise ConnectionError(f"Ошибка подключения к API: {err}")

    try:
        json_data = resp.json()
    except ValueError as err:
        raise ValueError(f"Ошибка парсинга JSON: {err}")

    if "Valute" not in json_data:
        raise KeyError("В ответе API отсутствует раздел 'Valute'")

    currencies = json_data["Valute"]
    output = {}

    for code in currency_codes:
        if code not in currencies:
            raise KeyError(f"Валюта '{code}' не найдена в ответе сервера")

        curr_data = currencies[code]

        if "Value" not in curr_data:
            raise KeyError(f"У валюты {code} отсутствует поле 'Value'")

        rate = curr_data["Value"]

        if not isinstance(rate, (int, float)):
            raise TypeError(f"Некорректный тип курса для {code}: {type(rate).__name__}")

        output[code] = float(rate)

    return output