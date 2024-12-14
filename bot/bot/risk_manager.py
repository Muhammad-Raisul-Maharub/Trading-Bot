class RiskManager:
    def __init__(self, take_profit_roi, stop_loss_roi):
        self.take_profit_roi = take_profit_roi
        self.stop_loss_roi = stop_loss_roi

    def evaluate_trade(self, trade_data):
        current_roi = trade_data["roi"]

        if current_roi >= self.take_profit_roi:
            return "close_trade"
        elif current_roi <= self.stop_loss_roi:
            return "stop_loss"
        else:
            return "hold"
