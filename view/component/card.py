from view.component.shared.button import Button
from view.component.shared.icon import IconType
from view.component.shared.image import Image

from dataclasses import dataclass

@dataclass
class CardImage:
    data: None | Image | IconType

@dataclass
class CardRef:
    data: None | Button

@dataclass
class Card:
    image: CardImage

    head: str
    description: str
    tags: list[Button]

    ref: CardRef

@dataclass
class SetCard:
    image: CardImage

    head: str
    set: list[str]
    tags: list[Button]

    ref: CardRef

@dataclass
class HeadonlyCard:
    image: CardImage

    head: str
    tags: list[Button]

    ref: CardRef

@dataclass
class LinearCard:
    head: str
    description: str

    ref: CardRef
