from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📊 My tracking", callback_data="my_watchlist"),
        InlineKeyboardButton("➕ Edit tracked", callback_data="edit_watchlist")],
        [InlineKeyboardButton("⚙️ Set up update", callback_data="settings"),
        InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)