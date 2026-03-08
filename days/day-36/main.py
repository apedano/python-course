import subprocess
import stock_model as sm
import datetime as dt

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_ULR="https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY= subprocess.check_output(
    [
        "gopass",
        "show",
        "-o",
        "websites/alphavantage.co", #secret path
    ],
    text=True
).strip()
NEWSAPI_URL="https://newsapi.org/v2/everything"
NEWSAPI_API_KEY= subprocess.check_output(
    [
        "gopass",
        "show",
        "-o",
        "websites/newsapi.org", #secret path
    ],
    text=True
).strip()



print(ALPHAVANTAGE_API_KEY)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_info()-> sm.StockInfo:
    parameters = {
        "function": "GLOBAL_QUOTE",
        "symbol": STOCK,
        "apikey" : ALPHAVANTAGE_API_KEY
    }
    req = requests.get(ALPHAVANTAGE_ULR, params=parameters)
    req.raise_for_status()
    stock_info = req.json()["Global Quote"]
    return sm.StockInfo(stock_info["05. price"], stock_info["08. previous close"], float(stock_info["10. change percent"][:-1]))


def get_news_last_three_days() -> list[sm.CompanyNews]:
    three_days_ago = dt.date.today() - dt.timedelta(days=3)
    parameters = {
        "q": COMPANY_NAME,
        "from": three_days_ago,
        "sortBy": "publishedAt",
        "apiKey": NEWSAPI_API_KEY
    }
    req = requests.get(NEWSAPI_URL, params=parameters)
    req.raise_for_status()
    last_news = []
    for i in range(3):
        news_dict = req.json()["articles"]
        current_news = news_dict[i]
        source = current_news["source"]["name"]
        author = current_news["author"]
        title = current_news["title"]
        description = current_news["description"]
        last_news.append(sm.CompanyNews(source, author, title, description))
    return last_news

def build_message(change_percentage:float, news_list:list[sm.CompanyNews]) -> str:
    message = "TSLA: "
    if change_percentage > 0:
        message += "🔺"
    else:
        message += "🔺"
    message = "🔻"
    message+=f"{change_percentage}%\n"
    for news in news_list:
        message += news.print_for_message()
    return message



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def main():
    stock_info = get_stock_info()
    change = stock_info.change_percentage
    if abs(change) > 1:
        print("Get News")
        print(build_message(stock_info.change_percentage, get_news_last_three_days()))
    else:
        print("Percentage change within the limits. No news will be sent")


if __name__ == "__main__":
    main()
