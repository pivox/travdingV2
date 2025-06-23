from src.Loader.DataLoader import DataLoader
from src.configLoader import CONFIG


class Analyser:
    def __init__(self):
        print("hello")

    def loadKline(self, pair: str, intervals: list[str]):
        pairs_dict = CONFIG.get_active_pairs()
        if pair not in list(pairs_dict.keys()):
            raise Exception("Pair not found in config file")
        if not intervals in list(pairs_dict[pair]['intervals']):
            raise Exception(f"interval not found in config file of {pair}")

        loader = DataLoader()
        for interval in intervals:
            loader.load(pair, interval)

