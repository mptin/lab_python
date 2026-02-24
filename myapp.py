import http.server
import socketserver
import urllib.parse
from jinja2 import Environment, PackageLoader, select_autoescape

from models import Author, App, User, Currency
from utils import currencies_api

# === Инициализация Jinja2 (один раз при старте) ===
# Ищем шаблоны в папке templates внутри пакета myapp
env = Environment(
    loader=PackageLoader("myapp", "templates"),
    autoescape=select_autoescape()
)

# === Глобальные данные (вместо базы данных) ===
users_db = []
currencies_db = []


def init_demo_data():
    """Создать тестовых пользователей."""
    global users_db
    users_db = [User("Алексей"), User("Мария"), User("Дмитрий")]


# === HTTP Handler (Контроллер) ===
class MyAppHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Обработка GET-запросов и маршрутизация."""
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Маршрутизация
        if path == "/" or path == "/author":
            # /author открывает ту же страницу, что и / (index.html)
            self.handle_index()
        elif path == "/users":
            self.handle_users()
        elif path == "/user":
            user_id = int(query.get("id", [0])[0])
            self.handle_user(user_id)
        elif path == "/currencies":
            self.handle_currencies()
        else:
            self.send_error(404, "Страница не найдена")

    def handle_index(self):
        """Главная страница (index.html)."""
        template = env.get_template("index.html")
        html = template.render(
            app_name="CurrenciesListApp",
            app_version="1.0.0",
            author_name=main_author.name,
            group=main_author.group,
            navigation=[
                {"caption": "Главная", "href": "/"},
                {"caption": "Пользователи", "href": "/users"},
                {"caption": "Курсы валют", "href": "/currencies"}
            ]
        )
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def handle_users(self):
        """Страница пользователей (users.html)."""
        template = env.get_template("users.html")
        html = template.render(users=users_db)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def handle_user(self, user_id: int):
        """Страница конкретного пользователя."""
        user = next((u for u in users_db if u.id == user_id), None)
        if not user:
            self.send_error(404, "Пользователь не найден")
            return

        # Простой HTML без отдельного шаблона (чтобы не превысить лимит файлов)
        html = f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head><meta charset="UTF-8"><title>{user.name}</title></head>
        <body>
            <h1>Пользователь: {user.name}</h1>
            <p>ID: {user.id}</p>
            <p>Подписки: {user.subscriptions}</p>
            <a href="/users">← К списку пользователей</a>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def handle_currencies(self):
        """Страница валют (currencies.html)."""
        template = env.get_template("currencies.html")

        try:
            rates = get_currencies(["USD", "EUR", "GBP", "CNY"])
            global currencies_db
            currencies_db = []
            names = {"USD": "Доллар США", "EUR": "Евро", "GBP": "Фунт", "CNY": "Юань"}

            for code, value in rates.items():
                curr = Currency("", code, names.get(code, code), value, 1)
                currencies_db.append(curr)
            error_msg = None
        except Exception as e:
            currencies_db = []
            error_msg = str(e)

        html = template.render(currencies=currencies_db, error=error_msg)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        print(f"[LOG] {args[0]}")


# === Точка входа ===
if __name__ == "__main__":
    init_demo_data()
    # ЗАМЕНИ НА СВОИ ДАННЫЕ
    main_author = Author(name="Твоё Имя", group="Твоя Группа")
    main_app = App(name="CurrenciesListApp", version="1.0.0", author=main_author)

    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyAppHandler) as httpd:
        print(f"Сервер запущен: http://localhost:{PORT}")
        print("Маршруты: /, /author, /users, /currencies")
        httpd.serve_forever()