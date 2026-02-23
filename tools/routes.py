from enum import Enum


base_url = "https://qa-scooter.praktikum-services.ru"

class AppRoute(str, Enum):
    HOME_PAGE = f"{base_url}/"
