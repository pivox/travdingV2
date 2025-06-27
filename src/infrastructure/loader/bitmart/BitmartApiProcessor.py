from typing import Dict, Any
import os
from datetime import datetime, timedelta, timezone

from src.application.coordinator.DataSourceCoordinator import DataSourceProcessor
from src.application.loader.EnumTypeData import EnumTypeData
from src.configLoader import CONFIG
from src.infrastructure.repository.sqlite.KlineRepository import KlineRepository
from src.infrastructure.bitmart.BitmartClient import BitmartClient
from src.domain.entity.Kline import Kline
from src.timezoneService import P_DATETIME


class BitmartApiProcessor(DataSourceProcessor):
    def can_handle(self) -> bool:
        return CONFIG.data["type_loader"] == EnumTypeData.BITMART.value

    def handle(self, data: Dict[str, Any]) -> None:
        print("Récupération des données depuis l'API BitMart :")

        pair = data["pair"]
        interval = data["interval"]

        klineRepository = KlineRepository()
        client = BitmartClient()

        last_kline = klineRepository.get_latest_timestamp(pair, interval)
        from_time = None
        # si la date récupéré + 4h est < date cuorante -alors je sors
        # si la date récupéré + 4h est > date cuorante  je la récupère


        if last_kline is None:
            from_time = self.align_to_minute(
                datetime.utcnow() - timedelta(minutes=client.kline_step_value(interval) * 100)
            )
        elif  P_DATETIME.add_interval(last_kline.timestamp, interval) <= P_DATETIME.get_current_datetime() :
            from_time = datetime.fromtimestamp(int(last_kline.timestamp))
        else:
            print(f"kline de {pair} sur l'interval : {interval} est à jours")
            return None

        to_time = self.align_to_minute(datetime.utcnow())

        from_time_str = from_time.strftime('%Y-%m-%d %H:%M:%S')
        to_time_str = to_time.strftime('%Y-%m-%d %H:%M:%S')  # direct, car déjà datetime

        print(f"Fetching klines from {from_time_str} to {to_time_str}...")

        print(f"Fetching klines from {from_time_str} to {to_time_str}...")
        klines = client.get_klines(pair, interval, from_time, to_time)
        if klines["code"] != 1000:
            raise Exception(f"Erreur lors de la récupération des klines : {klines['message']}")
        kline_objs = [
            Kline(
                timestamp=int(k['timestamp']),
                open=float(k['open_price']),
                close=float(k['close_price']),
                high=float(k['high_price']),
                low=float(k['low_price']),
                volume=float(k['volume']),
                interval=interval,
                symbol=pair
            )
            for k in klines['data']
        ]

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
