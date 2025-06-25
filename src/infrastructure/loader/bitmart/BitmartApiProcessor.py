from typing import Dict, Any
import os
from datetime import datetime, timedelta

from src.application.coordinator.DataSourceCoordinator import DataSourceProcessor
from src.application.loader.EnumTypeData import EnumTypeData
from src.configLoader import CONFIG
from src.infrastructure.repository.sqlite.KlineRepository import KlineRepository
from src.infrastructure.bitmart.BitmartClient import BitmartClient
from src.domain.entity.Kline import Kline


class BitmartApiProcessor(DataSourceProcessor):
    def can_handle(self) -> bool:
        return CONFIG.data["type_loader"] == EnumTypeData.BITMART.value

    def handle(self, data: Dict[str, Any]) -> None:
        print("Récupération des données depuis l'API BitMart :")

        pair = data["pair"]
        interval = data["interval"]

        klineRepository = KlineRepository()
        client = BitmartClient()

        last_kline = klineRepository.get_last_kline()
        if last_kline:
            from_time = last_kline.close_time
        else:
            from_time = self.align_to_minute(datetime.utcnow() - timedelta(hours=4))

        to_time = self.align_to_minute(datetime.utcnow())

        print(f"Fetching klines from {from_time} to {to_time}...")

        klines = client.get_klines(pair, interval, from_time, to_time)
        kline_objs = [Kline.from_api_response(pair, interval, k) for k in klines]

        if kline_objs:
            klineRepository.save_klines(kline_objs)
            print(f"{len(kline_objs)} klines sauvegardées.")
        else:
            print("Aucune donnée de Kline récupérée.")

    @staticmethod
    def align_to_minute(dt: datetime) -> datetime:
        """
        Aligne la date sur une minute exacte (secondes = 0).
        """
        return dt.replace(second=0, microsecond=0)

    @staticmethod
    def folder_contains_files_listdir(folder_path: str) -> bool:
        if not os.path.isdir(folder_path):
            print(f"Erreur : '{folder_path}' n'est pas un répertoire valide ou n'existe pas.")
            return False
        return any(os.path.isfile(os.path.join(folder_path, entry)) for entry in os.listdir(folder_path))
