import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder,ContextTypes,CommandHandler, filters,MessageHandler
TOKEN='6809401306:AAEKjbfN6IV70XGRryeI5m5bB7sT8-NMzAY'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s %(message)s',
    level=logging.INFO
)

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="I am a bot")
    
async def quote(update:Update,context:ContextTypes.DEFAULT_TYPE):
    
    response=requests.get('http://127.0.0.1:5000/quotes/random')
    if response.status_code==200:
        data=response.json()['quote']
        quote=str(data)
        print(quit)
        await context.bot.send_message(chat_id=update.effective_chat.id,text=quote)
        return True
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,text="Im sorry we could not retive a quote at this time")
        

async def echo(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)
    
if __name__=='__main__':
    application=ApplicationBuilder().token(TOKEN).build()
    start_handler=CommandHandler('start',start)
    quote_handler=CommandHandler('quote',quote)
    application.add_handler(start_handler)
    application.add_handler(quote_handler)
    application.run_polling()