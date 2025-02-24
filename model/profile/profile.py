from model.profile.member import Member
from model.shared.href import Href

from dataclasses import dataclass

@dataclass
class Profile:
    member: Member

    email: Href
    github: Href
    linkedin: Href

    homepage: Href
    blog: Href
    links: list[Href]
