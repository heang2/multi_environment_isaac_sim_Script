from dataclasses import dataclass
from typing import List

@dataclass
class TaskDescription:
    name: str
    goals: List[str]
    success_criteria: List[str]
