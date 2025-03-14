from model.shared.uid import Uid

from enum import Enum
from typing import Union
from dataclasses import dataclass

@dataclass
class LocalRefProfileQuery:
    uid: Uid

@dataclass
class LocalRefProductQuery:
    uid: Uid

@dataclass
class LocalRefProjectQuery:
    uid: Uid

class LocalRefType(Enum):
    IndexPage       = 0,
    DonatePage      = 1,
    ContactPage     = 2,
    ProfilePage     = 3,
    ProductPage     = 4,
    ProjectPage     = 5

@dataclass
class LocalRef:
    type: LocalRefType
    query: Union[
        None,
        LocalRefProfileQuery,
        LocalRefProductQuery,
        LocalRefProjectQuery
    ]

# ==== Reference to local target
# type      -> type of the page you want to go
# query     -> query data of the page
