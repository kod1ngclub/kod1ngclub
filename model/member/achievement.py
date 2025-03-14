from model.shared.uid import Uid

from dataclasses import dataclass
from enum import Enum

@dataclass
class AchievementUid:
    data: Uid

@dataclass
class Achievement:
    uid: AchievementUid

    name: str
    description: str
