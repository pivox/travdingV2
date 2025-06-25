import sqlite3
import os
from get_project_root import root_path
from src.domain.entity.Kline import Kline

class KlineRepository:
    def __init__(self):
        root = root_path(ignore_cwd=False)
        self.db_path = os.path.join(root, "db", "db.sqlite")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)

    def save(self, kline: Kline):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO klines (timestamp, open, close, high, low, volume, contract_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (kline.timestamp, kline.open, kline.close, kline.high, kline.low, kline.volume, kline.contract_id))
        self.conn.commit()
        self.conn.close()

    def get_latest_timestamp(self, pair: str, interval: str) -> int:
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT MAX(timestamp) FROM klines WHERE contract_id = ?
        """, (contract_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result and result[0] is not None else None

    def get_last_kline(self):
        pass

    def save_klines(self, klines: list[Kline]):
        for kline in klines:
            self.save(kline)
