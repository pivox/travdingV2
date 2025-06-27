from .TechnicalIndicator import TechnicalIndicator
import pandas as pd

class RSIIndicator(TechnicalIndicator):
    def compute_rsi(self, period: int) -> pd.Series:
        delta = self.kline_data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def validate(self) -> bool:
        period = self.params.get('period', 14)
        threshold = self.params.get('threshold', 70)
        rsi_series = self.compute_rsi(period)
        latest_rsi = rsi_series.iloc[-1]
        return latest_rsi > threshold
