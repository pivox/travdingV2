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

    def compute_score(setup_type: str, results: dict, config: dict) -> float:
        """
        setup_type: 'long' or 'short'
        results: dictionnaire avec les indicateurs validés => ex: {"rsi": True, "macd": False}
        config: configuration YAML chargée

        Retourne le score total validé
        """
        score = 0.0
        indicators = config['indicators'][setup_type]
        for name, is_valid in results.items():
            if is_valid and indicators.get(name, {}).get('enabled', False):
                score += indicators[name].get('score', 1.0)
        return score

    def is_valid_signal(score: float, config: dict) -> bool:
        return score >= config['strategy']['min_score_required']



