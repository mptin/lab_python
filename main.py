import logging
import io
from logger import logger
from get_currency import get_currencies


print("=== Тест 1: лог в консоль ===")

@logger()
def fetch_usd():
    return get_currencies(["USD"])

try:
    res = fetch_usd()
    print("Курс USD:", res)
except Exception as err:
    print("Ошибка:", err)


print("\n=== Тест 2: лог в StringIO ===")
buffer = io.StringIO()

@logger(handle=buffer)
def fetch_eur():
    return get_currencies(["EUR"])

try:
    res = fetch_eur()
    print("Курс EUR:", res)
    print("Содержимое лога:")
    print(buffer.getvalue())
except Exception as err:
    print("Ошибка:", err)


print("\n=== Тест 3: лог в файл currency.log ===")
log = logging.getLogger("currency_file")
log.setLevel(logging.INFO)

if not log.handlers:
    fh = logging.FileHandler("currency.log", encoding="utf-8")
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(fmt)
    log.addHandler(fh)

@logger(handle=log)
def fetch_currencies():
    return get_currencies(["USD", "EUR"])

try:
    res = fetch_currencies()
    print("Курсы:", res)
except Exception as err:
    print("Ошибка:", err)

print("\nГотово. Логи сохранены.")