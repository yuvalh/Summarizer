import requests
from bs4 import BeautifulSoup

def fetch_baba_news():
    """Fetch recent news about Alibaba stock from multiple sources."""
    news_sources = [
        'https://finance.yahoo.com/quote/BABA/news/',
        'https://seekingalpha.com/symbol/BABA/news'
    ]
    
    all_news = []
    
    for source in news_sources:
        try:
            response = requests.get(source, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Implement specific scraping logic for each source
            # This is a placeholder and needs detailed implementation
            news_items = soup.find_all('article')
            
            for item in news_items:
                title = item.get_text()
                link = item.find('a')['href'] if item.find('a') else ''
                all_news.append({
                    'title': title,
                    'link': link
                })
        except Exception as e:
            print(f"Error fetching news from {source}: {e}")
    
    return all_news
