import dataclasses
import datetime
from enum import Enum


class UserGender(Enum):
    Male = 1
    Female = 2
    Other = 3


class UserHobby(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: UserGender
    phone: str
    date_of_birth: datetime.date
    subject: str
    hobby: UserHobby
    picture: str
    address: str
    state: str
    city: str


student = Users(
    first_name="Kate",
    last_name="Voronova",
    email="test@ya.ru",
    gender=UserGender.Female,
    phone='1234567890',
    date_of_birth=datetime.date(2001, 9, 15),
    subject="Computer Science",
    hobby=UserHobby.Reading,
    picture="Grogu.jpg",
    address="Sadovaya street",
    state="NCR",
    city="Delhi",
)
