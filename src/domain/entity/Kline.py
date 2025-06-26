from typing import Optional


class Kline:
    def __init__(self, timestamp: int, open: float, close: float, high: float, low: float, volume: float, symbol: str, interval: str, id: Optional[int] = None):
        self.id = id
        self.timestamp = timestamp
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.symbol = symbol
        self.interval = interval

    def __repr__(self):
        return f"<Kline #{self.id or 'NA'} {self.timestamp} {self.open} {self.close} {self.symbol}>"

    @classmethod
    def from_row(cls, row: tuple) -> "Kline":
        return cls(
            id=int(row[0]),
            timestamp=int(row[1]),
            open=float(row[2]),
            close=float(row[3]),
            high=float(row[4]),
            low=float(row[5]),
            volume=float(row[6]),
            symbol=str(row[7]),
            interval=str(row[8])
        )

    def __repr__(self):
        return f"<Kline {self.timestamp} {self.open} {self.close} {self.symbol}>"
