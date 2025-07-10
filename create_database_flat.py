from aparts.database import Session, create_db

from faker import Faker
from aparts.flat import Flat


def create_database(load_faker_data=True):
    create_db()
    if load_faker_data:
        _load_faker_data(Session())


def _load_faker_data(session):
    street_name = ['Ленина', 'Куйбышева', 'Маяковского', 'Чехова', 'Шукшина', 'Бажова', 'Пушкина', 'Герцена', 'Кюи', 'Бородина']

    faker = Faker('ru_RU')
    session.commit()

    for _ in range(10):
        street = street_name[_]
        house = faker.random.randint(1, 100)
        floor = faker.random.randint(1, 10)
        square = faker.random.randint(15, 35)
        flat = Flat(street, house, floor, square)
        session.add(flat)

    session.commit()
    session.close()