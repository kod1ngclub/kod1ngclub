from model.shared.uid import Uid

from dataclasses import dataclass
from enum import Enum

@dataclass
class Member:
    uid: Uid

    name: str
    description: str
