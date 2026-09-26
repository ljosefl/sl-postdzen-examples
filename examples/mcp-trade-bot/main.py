import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# MCP API endpoint
MCP_API_URL = 'https://mcp.tinvest.ru/api/v1'

# Telegram bot token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def get_portfolio(portfolio_id):
    response = requests.get(f'{MCP_API_URL}/portfolio/{portfolio_id}')
    return response.json()

def start(update, context):
    update.message.reply_text('Привет! Я торговый робот на MCP Т-Инвестиций.')

def get_high_float_stocks(portfolio_id):
    portfolio = get_portfolio(portfolio_id)
    high_float_stocks = [stock for stock in portfolio if stock['float'] > 10000000]
    return high_float_stocks

def handle_message(update, context):
    user_message = update.message.text.lower()
    if 'акции' in user_message:
        portfolio_id = '123456'  # Replace with actual portfolio ID
        stocks = get_high_float_stocks(portfolio_id)
        update.message.reply_text(f'Высокоплаваемые акции: {stocks}')
    else:
        update.message.reply_text('Пожалуйста, уточните запрос.')

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()