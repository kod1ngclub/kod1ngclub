from model.shared.uid import Uid

from dataclasses import dataclass
from enum import Enum

@dataclass
class MemberUid:
    uid: Uid

@dataclass
class Member:
    uid: MemberUid

    name: str
    description: str
