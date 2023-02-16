from asyncio import events
import logging
from types import NoneType
import telegram
from telegram import Update
from telegram import Message
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from coins.management.commands.coins import CoinsConvApi
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="to convert currencies in real time send in this pattern:/convert USD-BRL",
    )

async def convert(update:Update,context:ContextTypes.DEFAULT_TYPE):
    currence = CoinsConvApi()
    if not context.args:
        await context.bot.send_message(chat_id=update.effective_chat.id,text="incorrect syntax please use the correct: /convert USD-BRL")
    else:
        coins = currence.get_coins(coins=str(context.args[0])) 
        await context.bot.send_message(chat_id=update.effective_chat.id, text=coins) 
if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("ur_token_here")
        .build()
    )

    start_handler = CommandHandler("start", start)
    convert_handler = CommandHandler("convert",convert)
    application.add_handler(start_handler)
    application.add_handler(convert_handler)
    application.run_polling()
