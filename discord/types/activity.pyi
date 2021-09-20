from typing import List, TypedDict

class ActivityTimestamps(TypedDict):
    start: int
    end: int

class ActivityParty(TypedDict):
    id: str
    size: List[int]

class ActivityAssets(TypedDict):
    large_image: str
    large_text: str
    small_image: str
    small_text: str

class ActivityButton(TypedDict):
    label: str
    url: str
