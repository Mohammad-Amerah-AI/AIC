import dataclasses
import collections
import json
import enum
from typing import List
from uuid import uuid4

class Country(enum.Enum):
    JORDAN = enum.auto()
    KSA = enum.auto()
    EGYPT = enum.auto()

class Gender(enum.Enum):
    MALE = enum.auto()
    FEMALE = enum.auto()

@dataclasses.dataclass
class Contact:
    contact_id : str = str(uuid4())
    name : str = " John Doe" #They use "John Doe" for nameless thing or person 
    contact_number : str = None 
    country : Country = Country.EGYPT
    gender : Gender = Gender.MALE

@dataclasses.dataclass
class Contacts:
    contacts = List[Contact]


class ContactDB:

    contacts: Contact = []
    
    def create_contact(self, name: str, contact_number: str, country: Country, gender: Gender):
        truncated_uuid = uuid4().hex
        truncated_uuid = truncated_uuid[::-1]
        truncated_uuid = truncated_uuid[4].upper()
        self.contacts.append(Contact(name=name, contact_number=contact_number, country=country, gender=gender))

    def read_contact(self , contact_id: str ):
        print(self.contacts)
        return self.contacts


