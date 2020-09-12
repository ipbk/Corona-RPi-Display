from abc import ABC, abstractmethod
from typing import Optional

from .Stats import Stats


class StatsGetter(ABC):
    @classmethod
    @abstractmethod
    def get_stats(cls) -> Optional[Stats]:
        pass
