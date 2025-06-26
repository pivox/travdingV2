import requests
from src.domain.entity.Kline import Kline
from src.infrastructure.repository.sqlite.KlineRepository import KlineRepository
from src.timezoneService import P_DATETIME

class KlineFetcher:
    BASE_URL = "https://api-cloud-v2.bitmart.com"

    def __init__(self):
        self.repository = KlineRepository()

    def fetch_and_persist(self, symbol: str, interval: str = "1m", duration_minutes: int = 240):
        endpoint = "/contract/public/kline"
        step = interval.replace("m", "")  # "15m" → "15", "1h" → "60"
        symbol = symbol.upper().replace("_", "")
        contract_id = symbol

        now = P_DATETIME.get_current_timestamp()
        latest_timestamp = self.repository.get_latest_timestamp(contract_id)

        if latest_timestamp:
            # On commence à la minute suivante
            start_time = latest_timestamp + 60
        else:
            # Si aucune donnée, on prend 4h en arrière
            start_time = DATETIME - (duration_minutes * 60)

        # On arrondit à la minute (secondes = 0)
        start_time -= start_time % 60
        end_time = now - (now % 60)

        params = {
            "symbol": symbol,
            "step": step,
            "start_time": start_time,
            "end_time": end_time
        }

        url = self.BASE_URL + endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["code"] != 1000 or "data" not in data:
            raise ValueError(f"Erreur Bitmart: {data.get('message')}")

        for entry in data["data"]:
            kline = Kline(
                timestamp=int(entry["timestamp"]),
                open=float(entry["open_price"]),
                close=float(entry["close_price"]),
                high=float(entry["high_price"]),
                low=float(entry["low_price"]),
                volume=float(entry["volume"]),
                symbol=symbol
            )
            self.repository.save(kline)
