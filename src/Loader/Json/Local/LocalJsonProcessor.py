from src.Coordinator.DataSourceCoordinator import DataSourceProcessor
from src.Loader.EnumTypeData import EnumTypeData
from typing import Dict, Any

from src.configLoader import CONFIG


class LocalJsonProcessor(DataSourceProcessor):
    def can_handle(self) -> bool:
        return CONFIG.data["type_loader"] == EnumTypeData.LOCAL.value

    def handle(self, data: Dict[str, Any]) -> None:
        print(f"Récupération des données du fichier JSON local : {source_identifier}")
        # if not os.path.exists(source_identifier):
        #     raise FileNotFoundError(f"Le fichier JSON n'existe pas : {source_identifier}")
        # with open(source_identifier, 'r', encoding='utf-8') as f:
        #     data = json.load(f)
        # return {"source_type": "local_json", "data": data}

