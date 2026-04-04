import os

DB_CONFIG = {
    "host": os.getenv("LIB_DB_HOST", "localhost"),
    "port": int(os.getenv("LIB_DB_PORT", "5432")),
    "database": os.getenv("LIB_DB_NAME", "baicuoikyPYTHON"),
    "user": os.getenv("LIB_DB_USER", "postgres"),
    "password": os.getenv("LIB_DB_PASSWORD", "2006"),
}
