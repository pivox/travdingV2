class Kline:
    def __init__(self, timestamp: int, open: float, close: float, high: float, low: float, volume: float, contract_id: str):
        self.timestamp = timestamp
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.contract_id = contract_id

    def __repr__(self):
        return f"<Kline {self.timestamp} {self.open} {self.close} {self.contract_id}>"
