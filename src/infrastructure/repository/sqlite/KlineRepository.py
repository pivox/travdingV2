import sqlite3
import os
from typing import Optional

from get_project_root import root_path
from src.domain.entity.Kline import Kline

class KlineRepository:
    INTERVAL_SQL_MAP = {
        "1m": "+1 minutes",
        "3m": "+3 minutes",
        "5m": "+5 minutes",
        "15m": "+15 minutes",
        "30m": "+30 minutes",
        "1h": "+1 hours",
        "2h": "+2 hours",
        "4h": "+4 hours",
        "6h": "+6 hours",
        "12h": "+12 hours",
        "1d": "+1 days",
        "3d": "+3 days",
        "1w": "+7 days"
    }

    def __init__(self):
        root = root_path(ignore_cwd=False)
        self.db_path = os.path.join(root, "db", "db.sqlite")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)

    def save(self, kline: Kline):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        query = """
                INSERT OR REPLACE INTO klines (timestamp, "open", close, high, low, volume, symbol, interval)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
        values = (
            kline.timestamp, kline.open, kline.close,
            kline.high, kline.low, kline.volume,
            kline.symbol, kline.interval
        )
        try:
            cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print(f"❌ Une erreur est survenue : {e}")
            print(f"🔎 Requête : {query}")
            print(f"📦 Valeurs : {values}")

        self.conn.close()

    def get_latest_timestamp(self, pair: str, interval: str) -> Optional[Kline]:
        interval_str = self.INTERVAL_SQL_MAP.get(interval)
        if not interval_str:
            raise ValueError(f"Unknown label: {interval}")
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT k.* 
            FROM klines k 
            JOIN contracts c ON c.symbol = k.symbol 
            WHERE c.symbol = ? and k.interval = ?
            order by k.timestamp desc limit 1
        """, (pair, interval))
        row = cursor.fetchone()
        self.conn.close()
        if row:
            return Kline.from_row(row)
        return None

    def get_last_kline(self, pair: str, interval: str) -> Kline:
        pass

    def save_klines(self, klines: list[Kline]):
        for kline in klines:
            self.save(kline)
