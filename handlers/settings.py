from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu

async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Notification interval", callback_data="set_notification_interval")],
        [InlineKeyboardButton("Notification type", callback_data="set_notification_type")],
        [InlineKeyboardButton("Back", callback_data="settings_back")]
        ]
    )
    await query.message.reply_text(text=BotResponses.CHOSE, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "set_notification_interval":
        await query.edit_message_text("🔔 Вы выбрали настройку интервала уведомлений")
        await context.bot.send_message(update.effective_user.id, text=BotResponses.CHOSE, reply_markup=await get_main_menu())
    elif query.data == "set_notification_type":
        await query.edit_message_text("📩 Вы выбрали тип уведомлений")
        await query.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())
    elif query.data == "settings_back":
        await query.edit_message_text("⬅️ Back to main menu")
        await query.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())
