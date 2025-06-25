from abc import ABC, abstractmethod
from typing import List
from src.domain.entity.Kline import Kline

class KlineRepositoryInterface(ABC):

    @abstractmethod
    def save_all(self, klines: List[Kline]) -> None:
        pass

    @abstractmethod
    def get_latest_close_time(self, symbol: str, interval: str) -> int:
        pass
