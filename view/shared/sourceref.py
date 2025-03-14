from enum import Enum
from typing import Union
from dataclasses import dataclass

@dataclass
class SourceRefType(Enum):
    Href            = 0

@dataclass
class SourceRefHrefQuery:
    to: str

@dataclass
class SourceRef:
    type: SourceRefType
    query: Union[
        None,
        SourceRefHrefQuery
    ]

# ==== Reference to source (image, video, etc)
# type      -> type of source you want to grep
# query     -> query data of the page
