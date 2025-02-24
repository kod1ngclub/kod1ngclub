from model.shared.href import Href

from dataclasses import dataclass

@dataclass
class DonatePlan:
    name: str
    description: str

    to: Href
