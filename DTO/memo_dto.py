from dataclasses import dataclass

@dataclass
class MemoDTO:
    id: int
    title: str
    content: str