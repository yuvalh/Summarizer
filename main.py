import os
from src.news_fetcher import fetch_baba_news
from src.news_summarizer import NewsSummarizer
from src.telegram_sender import TelegramNotifier
import asyncio

def main():
    # Retrieve API keys from environment variables
    xapi_key = os.environ.get('XAI_API_KEY')
    telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    # Fetch news
    news_items = fetch_baba_news()
    
    # Summarize news
    summarizer = NewsSummarizer(xapi_key)
    news_summary = summarizer.summarize_news(news_items)
    
    # Send to Telegram
    notifier = TelegramNotifier(telegram_token, telegram_chat_id)
    asyncio.run(notifier.send_message(news_summary))

if __name__ == "__main__":
    main()
