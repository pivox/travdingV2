class Contract:
    def __init__(self, data: dict) -> None:
        self.symbol = data.get("symbol")
        self.product_type = data.get("product_type")
        self.open_timestamp = data.get("open_timestamp")
        self.expire_timestamp = data.get("expire_timestamp")
        self.settle_timestamp = data.get("settle_timestamp")
        self.base_currency = data.get("base_currency")
        self.quote_currency = data.get("quote_currency")
        self.last_price = float(data.get("last_price", 0))
        self.volume_24h = int(data.get("volume_24h", 0))
        self.turnover_24h = float(data.get("turnover_24h", 0))
        self.index_price = float(data.get("index_price", 0))
        self.index_name = data.get("index_name")
        self.contract_size = float(data.get("contract_size", 0))
        self.min_leverage = int(data.get("min_leverage", 0))
        self.max_leverage = int(data.get("max_leverage", 0))
        self.price_precision = float(data.get("price_precision", 0))
        self.vol_precision = float(data.get("vol_precision", 0))
        self.max_volume = int(data.get("max_volume", 0))
        self.min_volume = int(data.get("min_volume", 0))
        self.funding_rate = float(data.get("funding_rate", 0))
        self.expected_funding_rate = float(data.get("expected_funding_rate", 0))
        self.open_interest = int(data.get("open_interest", 0))
        self.open_interest_value = float(data.get("open_interest_value", 0))
        self.high_24h = float(data.get("high_24h", 0))
        self.low_24h = float(data.get("low_24h", 0))
        self.change_24h = float(data.get("change_24h", 0))
        self.funding_time = int(data.get("funding_time", 0))
        self.market_max_volume = int(data.get("market_max_volume", 0))
        self.funding_interval_hours = int(data.get("funding_interval_hours", 0))
        self.status = data.get("status")
        self.delist_time = int(data.get("delist_time", 0))
        self.nextSchedule = int(data.get("nextSchedule", 0))

    @classmethod
    def from_row(cls, row: tuple) -> "Contract":
        keys = [
            "symbol", "product_type", "open_timestamp", "expire_timestamp", "settle_timestamp",
            "base_currency", "quote_currency", "last_price", "volume_24h", "turnover_24h",
            "index_price", "index_name", "contract_size", "min_leverage", "max_leverage",
            "price_precision", "vol_precision", "max_volume", "min_volume", "funding_rate",
            "expected_funding_rate", "open_interest", "open_interest_value", "high_24h", "low_24h",
            "change_24h", "funding_time", "market_max_volume", "funding_interval_hours", "status",
            "delist_time", "nextSchedule"
        ]
        data = dict(zip(keys, row))
        return cls(data)

    def __repr__(self):
        return f"<Contract {self.symbol}>"
