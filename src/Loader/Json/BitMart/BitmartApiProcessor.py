from typing import Dict, Any  # <-- ADD THIS LINE
import os

from src.Coordinator.DataSourceCoordinator import DataSourceProcessor
from src.Loader.EnumTypeData import EnumTypeData
from src.configLoader import CONFIG



class BitmartApiProcessor(DataSourceProcessor):
    def can_handle(self) -> bool:
        return CONFIG.data["type_loader"]  == EnumTypeData.BITMART.value

    def handle(self, data: Dict[str, Any]) -> None:
        print(f"Récupération des données depuis l'API BitMart : ")
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.join(current_script_dir, '..', '..', '..', '..')
        data_path = os.path.join(project_root,'data')
        print(project_root)
        exit(0)


        # api_path = source_identifier.replace('bitmart://', '')
        # if api_path == 'spot/v1/symbols':
        #     return {
        #         "source_type": "bitmart_api",
        #         "endpoint": api_path,
        #         "data": {"symbols": [{"symbol": "BTC_USDT"}, {"symbol": "ETH_USDT"}]},
        #         "timestamp": "2025-06-23T11:00:00Z"
        #     }
        # else:
        #     raise ValueError(f"Endpoint BitMart non supporté dans la simulation : {api_path}")
