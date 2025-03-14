from view.shared.remoteref import RemoteRef
from view.shared.localref import LocalRef

from dataclasses import dataclass
from enum import Enum

class IconType(Enum):
    Github      = 0,
    Email       = 1,
    Discord     = 2,
    Blog        = 4,
    PhoneCall   = 5

@dataclass
class Icon:
    type: IconType
    text: None | str

    to: None | RemoteRef | LocalRef

