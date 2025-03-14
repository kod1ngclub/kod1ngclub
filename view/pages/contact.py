from view.component.card import HeadonlyCard

from dataclasses import dataclass

@dataclass
class ContactPage:
    familys: list[HeadonlyCard]
    contacts: list[HeadonlyCard]