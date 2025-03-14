from view.shared.remoteref import RemoteRef
from view.shared.localref import LocalRef

from dataclasses import dataclass

@dataclass
class Button:
    to: RemoteRef | LocalRef
    text: str
