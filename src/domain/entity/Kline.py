class Kline:
    def __init__(self, timestamp: int, open: float, close: float, high: float, low: float, volume: float, symbol: str, interval: str):
        self.timestamp = timestamp
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.symbol = symbol
        self.interval = interval

    def __repr__(self):
        return f"<Kline {self.timestamp} {self.open} {self.close} {self.contract_id}>"

    @classmethod
    def from_row(cls, row: tuple) -> "Kline":
        return cls(
            timestamp=int(row[0]),
            open=float(row[1]),
            close=float(row[2]),
            high=float(row[3]),
            low=float(row[4]),
            volume=float(row[5]),
            symbol=str(row[6]),
            interval=str(row[7])
        )
