import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subject: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(
    first_name='Пользователь',
    last_name='Тестовый',
    email='Test@gmail.com',
    gender='Male',
    phone='8005553535',
    day_of_birth='13',
    month_of_birth='June',
    year_of_birth='1995',
    subject='Maths',
    picture='mem.jpg',
    hobby='Sports',
    address='Russia, Moscow',
    state='Uttar Pradesh',
    city='Agra'
)
