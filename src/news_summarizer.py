from openai import OpenAI

class NewsSummarizer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    
    def summarize_news(self, news_items):
        """Summarize news using GPT-4o-mini."""
        news_text = "\n".join([f"- {item['title']} ({item['link']})" for item in news_items])
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a financial news analyst. Summarize the following Alibaba stock news concisely."},
                {"role": "user", "content": f"Summarize these news items:\n{news_text}"}
            ]
        )
        
        return response.choices[0].message.content
