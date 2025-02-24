from model.shared.href import Href

from dataclasses import dataclass

@dataclass
class FamilySite:
    name: str
    to: Href

@dataclass
class Family:
    sites: list[FamilySite]
