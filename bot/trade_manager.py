import time
from bot.risk_manager import RiskManager
from config.indicators import calculate_rsi

class TradeManager:
    def __init__(self, config, logger):
        self.api_key = config["API_KEY"]
        self.secret_key = config["SECRET_KEY"]
        self.max_trades = config["MAX_TRADES"]
        self.rsi_threshold = config["RSI_THRESHOLD"]
        self.refresh_interval = config["REFRESH_INTERVAL"]
        self.logger = logger
        self.active_trades = {}

    def fetch_market_data(self, pair):
        # Simulate fetching market data (replace with actual API call)
        return {"price": 100, "rsi": 25}

    def start_trading(self):
        while True:
            self.logger.info("Refreshing market data...")
            self.execute_trades()
            time.sleep(self.refresh_interval)

    def execute_trades(self):
        # Fetch trading pairs (replace with actual API call)
        trading_pairs = ["SOL/USD", "BTC/USD", "ETH/USD"]

        for pair in trading_pairs:
            if len(self.active_trades) >= self.max_trades:
                self.logger.info("Maximum trades reached. Skipping new trades.")
                break

            if pair in self.active_trades:
                self.logger.info(f"Already trading {pair}. Skipping.")
                continue

            market_data = self.fetch_market_data(pair)
            rsi = calculate_rsi(market_data)

            if rsi < self.rsi_threshold:
                self.logger.info(f"Placing trade for {pair} (RSI: {rsi})")
                self.place_trade(pair, market_data)

    def place_trade(self, pair, market_data):
        trade_id = f"trade-{pair}"
        self.active_trades[pair] = trade_id
        self.logger.info(f"Trade placed: {pair} | Data: {market_data}")
