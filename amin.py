import os
from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder,CommandHandler,CallbackQuaryHandler,ContextType,filters

TOKEN=os.getenv("xxx")
ADMIN_ID=os.getenv("xxx")

async def start(update:Update,context:ContextType.DefoultType):
  await update.message.reply_text("welcome! give me the photo")
  
async def photo_handler(Update:update,context:ContextType.DefoultType):
  user= update.message.from_user
  photo= update.message.photo[-1].file_id
  
  bu=[
    [ InlineKeyboardButton("accept",callback data = f"accept_{user.id}"),
    InlineKeyboardButton("decline", callback_data = f"decline_{user.id}")
  ]
  ]
  
  reply_markup=InlineKeyboardMarkup(bu)
  
  caption=f"new photo \n user_id:{user.id} \n user_name:{user.first_name}"
  
  await context.bot.send_message(
    chat_id=ADMIN_ID,
    photo=photo,
    caption=caption.
    reply_markup=reply_markup}
  
  await update.message.reply_text("tanks the photo was sent")



async def button(update:Update,context:ContextType.DefoultType):
  query=update.query
  await query.answar()
  data=query.data.split("_")
  action=data[0]
  user_id=int(data[1])
  if action == "accept":
    await context.bot.send_message(chat_id=user_id,text="admin accept your request")
    await query.update_message_caption(caption="accepted")
  else:
    await context.bot.send_message(chat_id=user_id,text="admin decline your request")
    await query.update_message_caption(caption="declined")
  
def main():
  
  app=ApplicationBuilder().token(TOKEN).build()
  
  app.add_handler(CommandHandler("start",start))
  app.add_handler(CommandHandle(filter.photo,photo_handler))
  app.add_handler(Callbackhandler(button))
  
  app.run_polling()
  
if "_name_" == "_main_":
  main()
  
