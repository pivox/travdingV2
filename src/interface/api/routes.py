from fastapi import APIRouter, Query, Path
from src.application.analyser.Analyser import Analyser
from src.infrastructure.bitmart.ContractFetcher import ContractFetcher

router = APIRouter()

@router.get("/analyse")
def analyse(pair: str = Query(...), interval: str = Query(...)):
    analyser = Analyser()
    try:
        result = analyser.loadKline(pair, interval)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/fetch-pair/{symbol}")
def fetch(symbol: str = Path(...)):
    try:
        fetcher = ContractFetcher()
        contract_data = fetcher.fetch_and_store_if_missing(symbol)

        return {"status": "success", "data": contract_data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/fetch/all-contracts")
def fetch_all_contracts():
    print("🔥 REQUETE")
    try:
        fetcher = ContractFetcher()
        result = fetcher.fetch_all_and_store()

        return {
            "status": "success",
            "message": f"{len(result['saved'])} new contracts saved, {len(result['already_saved'])} already existed",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
