import requests
from typing import Dict, Any


class BitmartClient:
    BASE_URL = "https://api-cloud-v2.bitmart.com"

    def fetch_kline(self, symbol: str, interval: str, start_time: int, end_time: int) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/contract/public/kline"
        params = {
            "symbol": symbol,
            "interval": interval,
            "start_time": start_time,
            "end_time": end_time
        }
        print(params)
        response = requests.get(url, params=params)
        return response.json()
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def fetch_contract_details(self, symbol: str) -> dict:
        url = f"{self.BASE_URL}/contract/public/details"
        params = {"symbol": symbol}
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        return resp.json()
