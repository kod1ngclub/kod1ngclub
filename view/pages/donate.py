from view.component.card import Card

from dataclasses import dataclass

@dataclass
class DonatePage:
    plans: list[Card]
