import sqlite3
from typing import Optional, List
from get_project_root import root_path
from src.domain.entity.Contract import Contract
import os


class ContractRepository:
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

    def __init__(self, db_name: str = "db.sqlite"):
        root = root_path(ignore_cwd=False)
        self.db_path = os.path.join(root, "db", "db.sqlite")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self._create_table()

    def _create_table(self):
        query = """
                CREATE TABLE IF NOT EXISTS contracts
                (
                    symbol         TEXT PRIMARY KEY,
                    quote_currency TEXT,
                    base_currency  TEXT,
                    lot_size       REAL,
                    contract_size  REAL,
                    tick_size      REAL,
                    open_type      TEXT,
                    mode           INTEGER
                ) \
                """
        self.conn.execute(query)
        self.conn.commit()

    def save(self, contract: Contract):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO contracts (
                symbol, product_type, open_timestamp, expire_timestamp, settle_timestamp,
                base_currency, quote_currency, last_price, volume_24h, turnover_24h,
                index_price, index_name, contract_size, min_leverage, max_leverage,
                price_precision, vol_precision, max_volume, min_volume, funding_rate,
                expected_funding_rate, open_interest, open_interest_value, high_24h,
                low_24h, change_24h, funding_time, market_max_volume,
                funding_interval_hours, status, delist_time
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            contract.symbol,
            contract.product_type,
            contract.open_timestamp,
            contract.expire_timestamp,
            contract.settle_timestamp,
            contract.base_currency,
            contract.quote_currency,
            contract.last_price,
            contract.volume_24h,
            contract.turnover_24h,
            contract.index_price,
            contract.index_name,
            contract.contract_size,
            contract.min_leverage,
            contract.max_leverage,
            contract.price_precision,
            contract.vol_precision,
            contract.max_volume,
            contract.min_volume,
            contract.funding_rate,
            contract.expected_funding_rate,
            contract.open_interest,
            contract.open_interest_value,
            contract.high_24h,
            contract.low_24h,
            contract.change_24h,
            contract.funding_time,
            contract.market_max_volume,
            contract.funding_interval_hours,
            contract.status,
            contract.delist_time
        ))

        conn.commit()
        conn.close()

    def get_by_symbol(self, symbol: str) -> Optional[Contract]:
        query = "SELECT * FROM contracts WHERE symbol = ?"
        cursor = self.conn.execute(query, (symbol,))
        row = cursor.fetchone()
        if row:
            return Contract.from_row(row)
        return None

    def get_all(self) -> List[Contract]:
        query = "SELECT * FROM contracts"
        cursor = self.conn.execute(query)
        return [Contract.from_row(row) for row in cursor.fetchall()]

    def get_all_symbols(self) -> List[str]:
        query = "SELECT symbol FROM contracts"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def get_all_to_launch(self, interval: str) -> List[str]:
        interval_str = self.INTERVAL_SQL_MAP.get(interval)
        if not interval_str:
            raise ValueError(f"Unknown label: {interval}")
        query = f"""
                select symbol
                from contracts
                where (contracts.delist_time = 0 or contracts.delist_time > unixepoch())
                  and (contracts.nextSchedule is null or contracts.nextSchedule >= strftime('%s', 'now', '{interval_str}'))
                """
        cursor = self.conn.execute(query)

        return [row[0] for row in cursor.fetchall()]

    def update_next_schedule(self, symbol, interval):
        interval_str = self.INTERVAL_SQL_MAP.get(interval)
        if not interval_str:
            raise ValueError(f"Unknown label: {interval}")


        query = f"""
                UPDATE contracts
                SET nextSchedule = strftime('%s', 'now', '{interval_str}')
                WHERE symbol = ?
            """

        self.conn.execute(query, (symbol,))
        self.conn.commit()

