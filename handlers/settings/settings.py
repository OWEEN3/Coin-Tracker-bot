from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu
from database.dao.users_dao import UsersDAO
from keyboards.settings_menu import get_settings_menu

async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = await UsersDAO.get_user(chat_id=update.effective_user.id)
    await query.edit_message_text(text=BotResponses.CHOSE, reply_markup=await get_settings_menu(update))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data.startswith("set_notification_status"):
        current_status, changed_status = query.data.split("_")[3], ""
        if current_status == "off":
            await UsersDAO.edit_notification_status(chat_id=update.effective_user.id, notification_status="on")
            changed_status = "on"
        else:
            await UsersDAO.edit_notification_status(chat_id=update.effective_user.id, notification_status="off")
            changed_status = "off"
        await query.edit_message_text(f"Notification changed to {changed_status}", reply_markup=await get_settings_menu(update))
        
    elif query.data.startswith("set_notification_type"):
        current_type, changed_type = query.data.split("_")[3], ""
        if current_type == "new":
            await UsersDAO.edit_notification_type(chat_id=update.effective_user.id, notification_type="update_message")
            changed_type = "update message"
        else:
            await UsersDAO.edit_notification_type(chat_id=update.effective_user.id, notification_type="new_message")
            changed_type = "new message"
        await query.edit_message_text(f"Notification type changed to {changed_type}", reply_markup=await get_settings_menu(update))
    
    # elif query.data == "set_notification_interval":
    #     await query.edit_message_text("🔔 Вы выбрали настройку интервала уведомлений")
    #     await query.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())
    #     await query.edit_message_text(BotResponses.CHOSE, reply_markup=await get_settings_menu(update))
    
    elif query.data == "settings_back":
        await query.edit_message_text("⬅️ Back to main menu")
        await query.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())
