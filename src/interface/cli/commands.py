from src.application.analyser.Analyser import Analyser
from src.infrastructure.bitmart.ContractFetcher import ContractFetcher

def run_analyse(pair: str, interval: str):
    analyser = Analyser()
    analyser.loadKline(pair, interval)

def run_fetch(pair: str):
    fetcher = ContractFetcher()
    result = fetcher.fetch_and_store_if_missing(pair)
    print(result)

def run_fetch_contracts():
    fetcher = ContractFetcher()
    result = fetcher.fetch_all_and_store()

    print("✅ Contracts saved:")
    for s in result["saved"]:
        print(f" - {s}")

    print("\n⏸️ Already existing contracts:")
    for s in result["already_saved"]:
        print(f" - {s}")