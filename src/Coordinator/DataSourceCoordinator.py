import os
import json
from typing import Dict, Any, List
from abc import ABC, abstractmethod


class DataSourceProcessor(ABC):
    @abstractmethod
    def can_handle(self) -> bool:
        ...

    @abstractmethod
    def handle(self, data: Dict[str, Any]) -> None:
        ...
