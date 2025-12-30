class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.env = "prod"
        return cls._instance


config1 = AppConfig()
config2 = AppConfig()

print(config1 is config2)
print(config1.env)
