from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7458246005:AAE3DHYgO_iAhSD9BFmfjLjIrrAB4uW3HNs'
# Replace 'YOUR_USER_ID' with your actual Telegram user ID
USER_ID = @adarsh2626

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Send me a message and I'll forward it to the owner.")

def forward_message(update: Update, context: CallbackContext):
    message = update.message.text
    context.bot.send_message(chat_id=USER_ID, text=f"Message from {update.message.from_user.username}: {message}")
    update.message.reply_text("Message forwarded to the owner.")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
