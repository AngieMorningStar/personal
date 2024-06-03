import smtplib
from LxmlSoup import LxmlSoup
import requests
import re

# Получаем HTML код сайта
html = requests.get('https://pitergsm.ru/catalog/audio/naushniki/samsung/13510/').text  # получаем html код сайта

soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

last_price = 0
price_pattern = re.compile(r'[\d., \s]+')
for p in soup.find_all("span", class_="main-detail-price"):
    price = price_pattern.search(p.text()).group()
    print(last_price)
    last_price = price

def send_price_email(price):
    # Отправка электронного письма
    sender_email = 'angelina.r.doronina@gmail.com'
    receiver_email = 'angelina.r.doronina@gmail.com'
    password = 'password'

    message = f"Цена наушников Samsung: {price}"

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

print(price)
send_price_email(price)