from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from database.dao.tracking_dao import TrackingDAO

async def edit_traсking_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    tracking = await TrackingDAO.get_user_tracking(chat_id=update.effective_user.id)
    keyboard = []
    for track in tracking:
        keyboard.append([InlineKeyboardButton(f"🗑️ Delete {track.symbol}", callback_data=f"delete_tracking_{track.id}")])
    keyboard.append([InlineKeyboardButton("➕ Add new", callback_data='add_tracking')])
    keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data='back')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Your traсking:", reply_markup=reply_markup)
    
    