from typing import List

from pandas import Interval

from src.Coordinator.DataSourceCoordinator import DataSourceProcessor
from src.Loader.Json.BitMart.BitmartApiProcessor import BitmartApiProcessor
from src.Loader.Json.Local.LocalJsonProcessor import LocalJsonProcessor


class DataLoader:
    def __init__(self):
        self.loaders = self.getLoaders()

    def getLoaders(self) -> List[DataSourceProcessor]:
        return [
            LocalJsonProcessor(),
            BitmartApiProcessor(),
        ]

    def load(self, pair: str, interval: Interval) -> None:
        for loader in self.loaders:
            if loader.can_handle():
                return loader.handle({'pair': pair, 'interval': interval})
        return None
