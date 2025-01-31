from telegram import Bot
import asyncio

class TelegramNotifier:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
    
    async def send_message(self, message):
        """Send summary to Telegram."""
        bot = Bot(token=self.bot_token)
        await bot.send_message(chat_id=self.chat_id, text=message)
