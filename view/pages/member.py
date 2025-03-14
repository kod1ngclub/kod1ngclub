from view.component.profile import Profile
from view.component.card import LinearCard

from dataclasses import dataclass

@dataclass
class MemberPage:
    profile: Profile

    manages: list[LinearCard]
    contributes: list[LinearCard]
