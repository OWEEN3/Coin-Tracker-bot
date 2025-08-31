from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config import settings
from handlers.navigation import start, cancel
from services.crypto_api import fetch_prices
from handlers.my_watchlist.my_watchlist import my_watchlist
from handlers.edit_watchlist.add_tracking import add_handler as add_tracking
from handlers.edit_watchlist.delete_tracking import delete_tracking
from handlers.edit_watchlist.edit_tracking import edit_traсking_menu
from handlers.settings.settings import settings_menu, button_handler as set_notification_type_and_status
from handlers.settings.notification_interval import conv_handler as edit_interval
from handlers.about import about
from handlers.my_watchlist.watchlist_updater import watchlist_exit

def main():
    app = Application.builder().token(settings.TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))
    app.add_handler(CallbackQueryHandler(cancel, pattern='^back$'))
    
    app.add_handler(CallbackQueryHandler(my_watchlist, pattern='^my_tracking$'))
    app.add_handler(CallbackQueryHandler(watchlist_exit, pattern='^back_watchlist'))
    
    app.add_handler(CallbackQueryHandler(edit_traсking_menu, pattern='^edit_tracking$'))
    app.add_handler(add_tracking)
    app.add_handler(CallbackQueryHandler(delete_tracking, pattern='^delete_tracking'))
    
    app.add_handler(CallbackQueryHandler(settings_menu, pattern='^settings$'))
    app.add_handler(CallbackQueryHandler(set_notification_type_and_status, pattern=r'^(set_notification_type_.+|set_notification_status_.+)$'))
    app.add_handler(edit_interval)
    
    app.add_handler(CallbackQueryHandler(about, pattern="^about$"))

    app.job_queue.run_repeating(fetch_prices, interval=60, first=4)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()