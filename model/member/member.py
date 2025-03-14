from model.member.achievement import AchievementUid
from model.shared.href import Href
from model.shared.uid import Uid

from dataclasses import dataclass
from enum import Enum

@dataclass
class MemberUid:
    data: Uid

@dataclass
class Member:
    uid: MemberUid

    name: str
    description: str
    achievements: list[AchievementUid]

    email: Href
    github: Href
    linkedin: Href

    homepage: Href
    blog: Href
    links: list[Href]
