def calculate_rsi(data, period=14):
    # Simplified RSI calculation
    gains = [max(0, data[i] - data[i - 1]) for i in range(1, len(data))]
    losses = [max(0, data[i - 1] - data[i]) for i in range(1, len(data))]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    return rsi
