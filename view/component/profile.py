from view.component.shared.button import Button
from view.component.shared.icon import Icon
from view.component.shared.image import Image

from dataclasses import dataclass

@dataclass
class Profile:
    image: Image

    name: str
    bio: str
    achievements: list[Icon]

    contacts: list[Icon]
