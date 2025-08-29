from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📊 My tracking", callback_data="my_tracking"),
        InlineKeyboardButton("✏️ Edit tracked", callback_data="edit_tracking")],
        [InlineKeyboardButton("⚙️ Set up notifications", callback_data="settings"),
        InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)