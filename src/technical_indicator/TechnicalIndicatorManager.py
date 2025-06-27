from .RSIIndicator import RSIIndicator
from .MACDIndicator import MACDIndicator
import pandas as pd

class TechnicalIndicatorManager:
    def __init__(self, indicators_config: dict, kline_data_by_tf: dict[str, pd.DataFrame]):
        self.indicators_config = indicators_config
        self.kline_data_by_tf = kline_data_by_tf
        self.available_classes = {
            'rsi': RSIIndicator,
            'macd': MACDIndicator
        }

    def load_indicators(self):
        indicators = []
        for name, config in self.indicators_config.items():
            if config.get('enabled', False) and name in self.available_classes:
                indicator_class = self.available_classes[name]
                timeframes = config.get('timeframes', [])
                for tf in timeframes:
                    kline_data = self.kline_data_by_tf.get(tf)
                    if kline_data is not None:
                        params = config.get('params', {})
                        indicator = indicator_class(name, tf, params, kline_data)
                        indicators.append(indicator)
        return indicators

    def evaluate_all(self):
        results = {}
        for indicator in self.load_indicators():
            result = indicator.validate()
            results[f"{indicator.name}_{indicator.timeframe}"] = result
        return results

    def compute_score(self, results: dict) -> float:
        score = 0.0
        for key, valid in results.items():
            indicator_base = key.split("_")[0]
            if valid and indicator_base in self.indicators_config:
                score += self.indicators_config[indicator_base].get('score', 1.0)
        return score
