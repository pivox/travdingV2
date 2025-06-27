from abc import ABC, abstractmethod
import pandas as pd

class TechnicalIndicator(ABC):
    def __init__(self, name: str, timeframe: str, params: dict, kline_data: pd.DataFrame):
        self.name = name
        self.timeframe = timeframe
        self.params = params
        self.kline_data = kline_data

    @abstractmethod
    def validate(self) -> bool:
        pass
