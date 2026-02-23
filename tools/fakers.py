from faker import Faker
import random


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def name(self) -> str:
        return self.faker.first_name()
    
    def last_name(self) -> str:
        return self.faker.last_name()
    
    def address(self) -> str:
        return f"г. {self.faker.city_name()}"
    
    def phone_nubmer(self) -> str:
        return f"8987{random.randint(1000000, 9999999)}"
    
    def date(self) -> str:
        return self.faker.future_date().strftime("%d.%m.%Y")
    
    def sentence(self) -> str:
        return self.faker.sentence()
    
faker = Fake(faker=Faker("ru_Ru"))
