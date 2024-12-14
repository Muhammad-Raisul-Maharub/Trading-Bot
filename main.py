from config.config import load_config
from bot.trade_manager import TradeManager
from bot.logger import setup_logger

if __name__ == "__main__":
    config = load_config()
    logger = setup_logger()

    trade_manager = TradeManager(config, logger)
    trade_manager.start_trading()
