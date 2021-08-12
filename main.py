from bs4 import BeautifulSoup
import requests
import smtplib
import datetime
import random

# Mail credentials
my_email = 'your_email'
password = 'your_password'
reciever_mail = 'reciever_email'


response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

# there are two types of parsers HTML Parser, XML Parser.
soup = BeautifulSoup(yc_webpage, 'html.parser')

news_headlines = []
news_links = []
news_upvotes = []
all_news_link = soup.find_all(name='a',class_="storylink")
for link in all_news_link:
    news_headlines.append(link.text)
    news_links.append(link.get("href"))

upvotes = soup.find_all(name='span', class_='score')
for upvote in upvotes:
    news_upvotes.append(upvote.text)

# Mail

mail_text = ""

for i in range(len(news_upvotes)):
    news = f"{news_headlines[i]}\n {news_upvotes[i]} \t {news_links[i]}\n\n"
    mail_text += news


with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if True:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciever_mail,
            msg=f"Subject:Get Updated today with the Hacker news!\n\n{mail_text}"
        )
print("Sent")


