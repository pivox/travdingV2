from src.configLoader import CONFIG
from src.application.loader.DataLoader import DataLoader
from src.technical_indicator.TechnicalIndicatorManager import TechnicalIndicatorManager
import pandas as pd

class Analyser:
    def __init__(self):
        pass

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

    def analyze(self, pair: str):
        print(f"Analyse technique pour {pair}")

        # Étape 1 : Charger les données de marché
        interval = "5m"  # tu peux le passer dynamiquement aussi
        kline_data = self.load_kline(pair, interval)

        # Étape 2 : Charger la configuration YAML
        config = CONFIG.data
        strategy = config.get("strategy", {})
        indicators_config = config.get("indicators", {})

        for setup_type in ["long", "short"]:
            if not strategy.get(f"{setup_type}_enabled", False):
                continue

            setup_config = indicators_config.get(setup_type, {})

            print(f"  ➤ Setup {setup_type.upper()} :")
            manager = TechnicalIndicatorManager(setup_config, kline_data)
            results = manager.evaluate_all()
            score = manager.compute_score(results)
            min_score = strategy.get("min_score_required", 0)

            print(f"    Résultats : {results}")
            print(f"    Score total : {score} / Min requis : {min_score}")
            if score >= min_score:
                print(f"    ✅ Signal {setup_type.upper()} détecté avec score suffisant")
            else:
                print(f"    ❌ Pas de signal {setup_type.upper()} valide")



