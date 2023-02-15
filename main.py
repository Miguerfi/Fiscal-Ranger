import logging
import telegram
from telegram import Update
from telegram import Message
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

get_user = telegram.Bot("6141322753:AAEbBj4is3bEXtggY5UzPkb_L1cA6lAuvCo")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"hi {update.effective_chat.first_name},I'm at an experimental level, so don't expect too much.",
    )
    print(update.effective_chat)
    with open('output.txt','w') as f:
        f.write(f'''
nome={update.effective_chat.first_name},
chat_id={update.effective_chat.id},
type={update.effective_chat.type}
    ''')

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update._bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.effective_message.message_id,
    )


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("6141322753:AAEbBj4is3bEXtggY5UzPkb_L1cA6lAuvCo")
        .build()
    )

    start_handler = CommandHandler("start", start)
    clear_handler = CommandHandler("clear", clear)
    application.add_handler(clear_handler)

    application.add_handler(start_handler)

    application.run_polling()
