from .TechnicalIndicator import TechnicalIndicator
import pandas as pd

class MACDIndicator(TechnicalIndicator):
    def compute_macd(self):
        short_ema = self.kline_data['close'].ewm(span=12, adjust=False).mean()
        long_ema = self.kline_data['close'].ewm(span=26, adjust=False).mean()
        macd = short_ema - long_ema
        signal = macd.ewm(span=9, adjust=False).mean()
        return macd, signal

    def validate(self) -> bool:
        macd, signal = self.compute_macd()
        return macd.iloc[-1] > signal.iloc[-1]
