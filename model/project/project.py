from model.project.product import ProductUid
from model.member.member import MemberUid
from model.shared.uid import Uid

from dataclasses import dataclass

@dataclass
class ProjectUid:
    data: Uid

@dataclass
class Project:
    uid: ProjectUid

    name: str
    description: str
    projects: list[ProductUid]

    manager: MemberUid
