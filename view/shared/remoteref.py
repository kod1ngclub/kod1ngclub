from enum import Enum
from typing import Union
from dataclasses import dataclass

@dataclass
class RemoteRefType(Enum):
    Href            = 0

@dataclass
class RemoteRefHrefQuery:
    to: str

@dataclass
class RemoteRef:
    type: RemoteRefType
    query: Union[
        None,
        RemoteRefHrefQuery
    ]

# ==== Reference to remote target
# type      -> type of something you want to go
# query     -> query data of the page