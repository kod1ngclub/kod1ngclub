from model.project.product import Product
from model.profile.member import Member
from model.shared.uid import Uid

from dataclasses import dataclass

@dataclass
class Project:
    uid: Uid

    name: str
    description: str
    projects: list[Product]

    manager: Member
