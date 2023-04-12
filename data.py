import twilio.rest
import requests
import datetime
import os

class Stock:
    
    def send_not(self):
        self.msg = twilio.rest.Client("AC71eed1defc7c419ddb7c46fe116d3e08", "f9109b25d146bd84a502bbe103fa0487")
        self.msg.messages.create(from_ = 'whatsapp:+14155238886', to = 'whatsapp:+905528607650',
        body = f"Tesla share price for today is {self.today_open} and its {self.dif()} than last time by {self.per}%\n\n\n{self.news_title}\n\n{self.news_description}")
        
    def days(self):
        self.today = datetime.date.today()
        self.yesterday = self.today - datetime.timedelta(days = 1)
        if self.yesterday.weekday() == 6:
            self.yesterday = self.today - datetime.timedelta(days = 3)
        
    def dif(self):
        if self.today_open > self.yesterday_open:
            self.per = round(self.yesterday_open / self.today_open, 2)
            return "higher"
        self.per = round(self.today_open / self.yesterday_open, 2)    
        return "lower"
        
    def get_info(self):
        self.today_open = float(requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=Tsla&apikey={os.environ.get('api_key_stock')}").json()["Time Series (Daily)"][f"{self.today}"]["1. open"])
        self.yesterday_open = float(requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=Tsla&apikey={os.environ.get('api_key_stock')}").json()["Time Series (Daily)"][f"{self.yesterday}"]["1. open"])

    def get_news(self):
        self.news_title = requests.get("https://newsapi.org/v2/everything?q=tesla&apiKey=1eee777823ca4e66abcf91e63fedeaf6").json()["articles"][0]["title"]
        self.news_description = requests.get("https://newsapi.org/v2/everything?q=tesla&apiKey=1eee777823ca4e66abcf91e63fedeaf6").json()["articles"][0]["description"]

