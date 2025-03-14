from view.shared.sourceref import SourceRef

from dataclasses import dataclass

@dataclass
class Image:
    src: SourceRef
    alt: str
