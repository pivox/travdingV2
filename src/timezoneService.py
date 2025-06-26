from datetime import datetime, timedelta
import pytz
from src.configLoader import CONFIG


class TimezoneService:
    INTERVAL_TO_TIMEDELTA = {
        "1m": timedelta(minutes=1),
        "3m": timedelta(minutes=3),
        "5m": timedelta(minutes=5),
        "15m": timedelta(minutes=15),
        "30m": timedelta(minutes=30),
        "1h": timedelta(hours=1),
        "2h": timedelta(hours=2),
        "4h": timedelta(hours=4),
        "6h": timedelta(hours=6),
        "12h": timedelta(hours=12),
        "1d": timedelta(days=1),
        "3d": timedelta(days=3),
        "1w": timedelta(weeks=1),
    }


    def __init__(self):
        self.timezone_str = CONFIG.data['timezone']
        self.fixed_date_str = CONFIG.data['fixed_date'] if CONFIG.data['is_fixed'] else None
        self.timezone = pytz.timezone(self.timezone_str)

    def get_current_datetime(self) -> datetime:
        # Si fixed_date est une date valide, on l'utilise
        if self.fixed_date_str is not None:
            try:
                naive_dt = datetime.strptime(self.fixed_date_str, "%Y-%m-%d %H:%M:%S")
                dt = self.timezone_str.localize(naive_dt)
                return dt
            except ValueError:
                print("⚠️ Format de date invalide dans fixed_date. Utilisation de la date actuelle.")
        # Sinon date normale
        return datetime.now(self.timezone)

    def get_current_timestamp(self) -> int:
        return int(self.get_current_datetime().timestamp())

    def from_timestamp(self, timestamp: int) -> datetime:
        return datetime.fromtimestamp(timestamp, self.timezone)

    def add_interval(self, timestamp: int, interval: str) -> datetime:

        return datetime.fromtimestamp(timestamp, self.timezone) + self.INTERVAL_TO_TIMEDELTA[interval]

P_DATETIME = TimezoneService()