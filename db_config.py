# Мои параметры
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'QA-Testing',
    'user': 'postgres',
    'password': '12345'
}

CONNECTION_STRING = "postgresql://{}:{}@{}:{}/{}".format(
    DB_CONFIG['user'],
    DB_CONFIG['password'],
    DB_CONFIG['host'],
    DB_CONFIG['port'],
    DB_CONFIG['database']
)
