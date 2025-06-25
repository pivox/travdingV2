from src.application.loader.DataLoader import DataLoader
from src.configLoader import CONFIG


class Analyser:

    def loadKline(self, pair: str, interval: str):

        loader = DataLoader()
        loader.load(pair, interval)
        return {"message": f"Kline loaded for {pair} on {interval}"}


