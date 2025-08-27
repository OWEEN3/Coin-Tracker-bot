from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config import settings
from handlers.navigation import start, cancel
from services.crypto_api import fetch_prices
from handlers.my_watchlist_handler import my_watchlist
from handlers.edit_watchlist_handler import conv_handler as edit_tracked

def main():
    app = Application.builder().token(settings.get_token).build()

    # Хендлеры
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CallbackQueryHandler(my_watchlist, pattern='^my_watchlist$'))
    app.add_handler(edit_tracked)

    app.job_queue.run_repeating(fetch_prices, interval=60, first=2)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()