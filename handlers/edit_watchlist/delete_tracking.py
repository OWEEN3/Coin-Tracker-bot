from telegram import Update
from telegram.ext import ContextTypes

from database.dao.tracking_dao import TrackingDAO
from responses.response import BotResponses
from keyboards.main_menu import get_main_menu

async def delete_tracking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    tracking_id = int(query.data.split('_')[2])
    await TrackingDAO.delete(id=tracking_id)
    await query.edit_message_text("Deleted successfully")
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text=BotResponses.CHOSE, 
        reply_markup=await get_main_menu()
    )