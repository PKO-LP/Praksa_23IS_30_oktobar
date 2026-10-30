# Подключение к серверу PostgreSQL, а не к программе pgAdmin.
DB = {
    "dbname": "mobile_apps_auth_lesson",  # Имя нашей базы.
    "user": "postgres",                  # Пользователь сервера PostgreSQL.
    "password": "ВАШ_ПАРОЛЬ",             # Пароль сервера, не пароль входа в магазин.
    "host": "localhost",                 # Сервер на этом компьютере.
    "port": 5432,                        # Порт сервера.
    "connect_timeout": 5,                # Сколько секунд ждать подключения.
    "options": "-c statement_timeout=5000"  # Ограничение выполнения SQL: 5 секунд.
}
