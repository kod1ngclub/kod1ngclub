from view.component.card import SetCard

from dataclasses import dataclass

@dataclass
class AchievementPage:
    achievements: list[SetCard]