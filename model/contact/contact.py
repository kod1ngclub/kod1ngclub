from model.shared.href import Href

from dataclasses import dataclass

@dataclass
class Contact:
    email: Href
    github: Href
    discord: Href
