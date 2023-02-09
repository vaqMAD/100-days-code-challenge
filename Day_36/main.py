import smtplib
from stock_data import StockData
from news import News, OneArticle
import credentials

my_email = credentials.my_email
my_password = credentials.my_password

stock_data = StockData()

if stock_data.check_difference_percentage_stock_value():
    news = News()
    articles_objects = []
    for article in news.articles_range:
        articles_objects.append(OneArticle(article))

if len(articles_objects) > 0:
    for object_article in articles_objects:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="nikola.letowska@gmail.com",
                                msg=f"Subject: {object_article.title}\n\n{object_article.description}\n{object_article.url}")


