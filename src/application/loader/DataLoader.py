from time import sleep
from typing import List

from src.application.coordinator.DataSourceCoordinator import DataSourceProcessor
from src.infrastructure.loader.bitmart.BitmartApiProcessor import BitmartApiProcessor
from src.infrastructure.loader.local.LocalJsonProcessor import LocalJsonProcessor
from src.infrastructure.repository.sqlite.ContractRepository import ContractRepository


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

    def load_all(self, interval):
        contractRepository = ContractRepository()
        symbols = contractRepository.get_all_to_launch(interval)
        list = []
        for symbol in symbols:
            list.append(self.load(symbol, interval))
            contractRepository.update_next_schedule(symbol, interval)
            sleep(1)
        return list
