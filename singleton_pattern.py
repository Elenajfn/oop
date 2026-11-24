import json
import os


# config.py
SAMPLE_CONFIG = {
    "app": {"name": "PaymentPlatform", "debug": True},
    "database": {"host": "localhost", "port": 5432},
    "email": {"smtp_host": "smtp.company.com", "sender": "no-reply@company.com"},
    "payment": {"api_key": "sk_test_123456", "environment": "sandbox"},
}


class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load()
        return cls._instance

    def _load(self):
        if not os.path.exists("config.json"):
            with open("config.json", "w") as f:
                json.dump(SAMPLE_CONFIG, f, indent=4)
        with open("config.json", "r") as f:
            self._config = json.load(f)

    @classmethod
    def get_instance(cls):
        return cls()

    def get(self, key, default=None):
        value = self._config
        for part in key.split("."):
            if not isinstance(value, dict) or part not in value:
                return default
            value = value[part]
        return value

    def set(self, key, new_value):
        parts = key.split(".")
        value = self._config
        for part in parts[:-1]:
            value = value.setdefault(part, {})
        value[parts[-1]] = new_value

    @classmethod
    def reset_instance(cls):
        cls._instance = None


# database.py
def connect_database():
    config = ConfigManager.get_instance()
    db_host = config.get("database.host")
    db_port = config.get("database.port")
    print(f"Connecting to database at {db_host}:{db_port}")


# email_service.py
def send_email(to: str, subject: str):
    config = ConfigManager.get_instance()
    smtp_host = config.get("email.smtp_host")
    sender = config.get("email.sender")
    print(f"Sending email from {sender} via {smtp_host}")


# payment_service.py
def process_payment(amount: float):
    config = ConfigManager.get_instance()
    api_key = config.get("payment.api_key")
    environment = config.get("payment.environment")
    print(f"Processing {amount}€ in {environment} mode")


# app.py
def start_application():
    config = ConfigManager.get_instance()
    app_name = config.get("app.name")
    debug = config.get("app.debug")
    print(f"Starting {app_name} (debug={debug})")


if __name__ == "__main__":
    start_application()
    connect_database()
    send_email("user@test.com", "Welcome")
    process_payment(99.99)
