from model.project.product import Product
from model.profile.member import Member
from model.shared.uid import Uid

from dataclasses import dataclass

@dataclass
class ProjectUid:
    uid: Uid

@dataclass
class Project:
    uid: ProjectUid

    name: str
    description: str
    projects: list[Product]

    manager: Member
