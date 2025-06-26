from src.application.loader.DataLoader import DataLoader

class Analyser:

    def load_kline(self, pair: str, interval: str):

        loader = DataLoader()
        loader.load(pair, interval)
        return {"message": f"Kline loaded for {pair} on {interval}"}

    def analyze_all(self, interval: str):
        loader = DataLoader()
        result = loader.load_all(interval)
        print(result)


