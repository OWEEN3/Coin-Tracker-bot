from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BotResponses.START)
    await update.message.reply_text(BotResponses.CHOSE, reply_markup=get_main_menu())

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BotResponses.CHOSE, reply_markup=get_main_menu())