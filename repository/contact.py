from model.contact.contact import Contact
from model.contact.family import Family

from abc import ABC, abstractmethod

class ContactRepository(ABC):
    @abstractmethod
    def ReadContact() -> Contact:
        pass

    @abstractmethod
    def ReadFamily() -> Family:
        pass

