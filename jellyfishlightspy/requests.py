from typing import List, Optional
from types import SimpleNamespace
from .model import State, PatternConfig

class GetRequest:
    def __init__(self, *args) -> None:
        self.cmd = 'toCtlrGet'
        self.get = [[*args]]

class SetRequest:
    def __init__(self, state: int, zoneName: List[str], file: str = "", id: str = "", data: Optional[PatternConfig] = None):
        self.cmd = 'toCtlrSet'
        self.runPattern = State(state = state, zoneName = zoneName, file = file, id = id, data = data)