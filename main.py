from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config import settings
from handlers.navigation import start, cancel
from services.crypto_api import fetch_prices
from handlers.my_watchlist import my_watchlist
from handlers.add_tracking import add_handler as add_tracking
from handlers.delete_tracking import delete_tracking
from handlers.edit_tracking import edit_traсking_menu
from handlers.settings import settings_menu, button_handler as settings_button_handler

def main():
    app = Application.builder().token(settings.TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CallbackQueryHandler(cancel, pattern='^back$'))
    
    app.add_handler(CallbackQueryHandler(my_watchlist, pattern='^my_tracking$'))
    
    app.add_handler(CallbackQueryHandler(edit_traсking_menu, pattern='^edit_tracking$'))
    app.add_handler(add_tracking)
    app.add_handler(CallbackQueryHandler(delete_tracking, pattern='^delete_tracking'))
    
    app.add_handler(CallbackQueryHandler(settings_menu, pattern='^settings$'))
    app.add_handler(CallbackQueryHandler(settings_button_handler, pattern=r'^(set_notification_interval|set_notification_type_.+|set_notification_status_.+)$'))

    app.job_queue.run_repeating(fetch_prices, interval=60, first=4)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()