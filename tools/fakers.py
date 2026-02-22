from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def name(self) -> str:
        return self.faker.name()
    
    def last_name(self) -> str:
        return self.faker.last_name()
    
    def address(self) -> str:
        return self.faker.address()
    
    def phone_nubmer(self) -> str:
        return self.faker.phone_number()

faker = Fake(faker=Faker("ru_Ru"))
