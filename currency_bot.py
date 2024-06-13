import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and context.
async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am your calculator bot. Send me a calculation!')

async def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text('You can send me a calculation like "2 + 2" or "5 * 3"')

async def calculate(update: Update, context: CallbackContext) -> None:
    """Handle the calculation."""
    try:
        expression = update.message.text
        result = eval(expression)
        await update.message.reply_text(f'The result is: {result}')
    except Exception as e:
        await update.message.reply_text('Sorry, I could not understand that. Please send a valid calculation.')

def main() -> None:
    """Start the bot."""
    # Replace 'YOUR TOKEN HERE' with your bot's token
    application = ApplicationBuilder().token("BOT_TOKEN").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
