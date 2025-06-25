from typing import List

from pandas import Interval

from src.application.coordinator.DataSourceCoordinator import DataSourceProcessor
from src.infrastructure.loader.bitmart.BitmartApiProcessor import BitmartApiProcessor
from src.infrastructure.loader.local.LocalJsonProcessor import LocalJsonProcessor


class DataLoader:
    def __init__(self):
        self.loaders = self.getLoaders()

    def getLoaders(self) -> List[DataSourceProcessor]:
        return [
            LocalJsonProcessor(),
            BitmartApiProcessor(),
        ]

    def load(self, pair: str, interval: str) -> None:
        for loader in self.loaders:
            if loader.can_handle():
                return loader.handle({'pair': pair, 'interval': interval})
        return None
