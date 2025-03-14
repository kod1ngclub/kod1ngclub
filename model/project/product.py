from model.member.member import MemberUid
from model.shared.uid import Uid
from model.shared.href import Href

from dataclasses import dataclass

@dataclass
class ProductUid:
    data: Uid

@dataclass
class Product:
    uid: ProductUid

    name: str
    description: str
    deprecated: bool

    install: Href
    homepage: Href
    repository: Href

    manager: MemberUid
    contributors: list[MemberUid]
