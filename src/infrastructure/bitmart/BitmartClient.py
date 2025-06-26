from datetime import datetime

import requests
from typing import Dict, Any


class BitmartClient:
    BASE_URL = "https://api-cloud-v2.bitmart.com"

    def get_klines(self, symbol: str, interval: str, start_time: datetime, end_time: datetime) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/contract/public/kline"
        params = {
            "symbol": symbol,
            "step": self.kline_step_value(interval),
            "start_time": int(start_time.timestamp()),
            "end_time": int(end_time.timestamp())
        }
        print(f"Requête vers BitMart : {url} avec {params}")
        response = requests.get(url, params=params)

        response.raise_for_status()
        return response.json()

    def fetch_contract_details(self, symbol: str) -> dict:
        url = f"{self.BASE_URL}/contract/public/details"
        params = {"symbol": symbol}
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def kline_step_value(self, label: str) -> int:
        mapping = {
            "1m": 1,
            "3m": 3,
            "5m": 5,
            "15m": 15,
            "30m": 30,
            "1h": 60,
            "2h": 120,
            "4h": 240,
            "6h": 360,
            "12h": 720,
            "1d": 1440,
            "3d": 4320,
            "1w": 10080
        }
        if label not in mapping:
            raise ValueError(f"Unknown label: {label}")
        return mapping[label]


