import requests
import json
from src.infrastructure.repository.sqlite.ContractRepository import ContractRepository
from src.domain.entity.Contract import Contract
from typing import List, Dict

class ContractFetcher:
    BASE_URL = "https://api-cloud-v2.bitmart.com"

    def __init__(self):
        self.api_url = "https://api-cloud-v2.bitmart.com/contract/public/details"
        self.repository = ContractRepository()

    def fetch_and_store_if_missing(self, symbol: str) -> dict:
        symbol = symbol.upper()
        response = requests.get(self.api_url)
        response.raise_for_status()
        result = response.json()

        if result.get("code") != 1000:
            raise ValueError(f"Erreur API Bitmart : {result.get('message')}")

        contracts = result["data"]["symbols"]
        contract_data = next(
            (contract for contract in contracts if contract.get("symbol") == symbol),
            None
        )
        if not contract_data:
            raise ValueError(f"No contract found for symbol: {symbol}")
        return {"status": "success", "data": contract_data}

        # Sauvegarde si non existant
        if not self.repository.get_by_symbol(symbol):
            contract = Contract(
                symbol=symbol,
                quote_currency=contract_data["quote_currency"],
                base_currency=contract_data["base_currency"],
                lot_size=float(contract_data["lot_size"]),
                contract_size=float(contract_data["contract_size"]),
                tick_size=float(contract_data["tick_size"]),
                open_type=contract_data["open_type"],
                mode=int(contract_data["contract_status"])
            )
            self.repository.save(contract)

        return contract_data

    def fetch_all_and_store(self) -> Dict[str, List[str]]:
        url = f"{self.BASE_URL}/contract/public/details"
        response = requests.get(url)

        response.raise_for_status()
        data = response.json()

        if data["code"] != 1000:
            raise ValueError(f"BitMart API error: {data.get('message', 'Unknown error')}")

        contracts_data = data["data"]["symbols"]
        all_symbols = self.repository.get_all_symbols()

        saved = []
        already_saved = []


        for contract_dict in contracts_data:
            if (contract_dict["symbol"] not in all_symbols):
                contract = Contract(contract_dict)
                self.repository.save(contract)
                saved.append(contract.symbol)
            else:
                already_saved.append(contract_dict["symbol"])

        return {
            "saved": saved,
            "already_saved": already_saved
        }