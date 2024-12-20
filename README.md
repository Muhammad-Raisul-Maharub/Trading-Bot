# Universal Trading Bot

## Overview
This bot is a universal trading bot designed to work with platforms like Rollbit. It supports both API and web-scraping modes, making it adaptable to platforms with or without API support.

---

## Features
- **API Mode**: If a platform supports an API, the bot can interact using API credentials.
- **Scraper Mode**: For platforms without APIs, the bot uses Selenium to scrape and automate trades.
- **Multiple Crypto Pairs**: Supports trading across multiple cryptocurrency pairs.
- **Configurable RSI and ROI**: User-defined RSI thresholds, ROI targets, and stop-loss conditions.
- **Customizable Settings**: Configure trading pairs, amounts, and cooldown periods in `config.json`.

---

## Setup

### Prerequisites
1. **Python 3.8 or higher** installed on your system.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
