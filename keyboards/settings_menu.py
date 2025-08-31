from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from database.dao.users_dao import UsersDAO

async def get_settings_menu(update: Update):
    user = await UsersDAO.get_user(chat_id=update.effective_user.id)
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"Notification: {user.notification_status}", callback_data=f"set_notification_status_{user.notification_status}")],
        [InlineKeyboardButton(f"⌛ Notification interval: {user.notification_interval} sec", callback_data="set_notification_interval")],
        [InlineKeyboardButton(f"📋 Notification type: {" ".join(user.notification_type.split("_"))}", callback_data=f"set_notification_type_{user.notification_type}")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]
    )
    return reply_markup