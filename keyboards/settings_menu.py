from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from database.dao.users_dao import UsersDAO

async def get_settings_menu(update: Update):
    user = await UsersDAO.get_user(chat_id=update.effective_user.id)
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"Course update: {user.update_status}", callback_data=f"set_update_status_{user.update_status}")],
        [InlineKeyboardButton(f"⌛ Update interval: {user.update_interval} sec", callback_data="set_update_interval")],
        [InlineKeyboardButton(f"📋 Update type: {" ".join(user.update_type.split("_"))}", callback_data=f"set_update_type_{user.update_type}")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]
    )
    return reply_markup