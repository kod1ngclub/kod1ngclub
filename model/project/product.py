from model.profile.member import Member
from model.shared.uid import Uid
from model.shared.href import Href

from dataclasses import dataclass

@dataclass
class ProductUid:
    uid: Uid

@dataclass
class Product:
    uid: ProductUid

    name: str
    description: str
    deprecated: bool

    install: Href
    homepage: Href
    repository: Href

    manager: Member
    contributors: list[Member]
