import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://codeforces.com/profile/shrey1002"
header = {
    "User-Agent": "********************",
    "Accept-Language":"*************"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

parent = soup.find(class_="info")
current_rank=list(parent.find(class_="user-rank").descendants)[1].getText()
current_rating=int(list(parent.find("li").descendants)[3].getText())
prev_rating = 1273

if current_rating != prev_rating:
    message = f"Hola!\nYour rating has changed by {current_rating-prev_rating} \nNow your rating is {current_rank} {current_rating}\nCheck out your new achievement"
    prev_rating=current_rating
    with smtplib.SMTP("outlook.office365.com",port=587) as connection:
        # connection.set_debuglevel(1)
        # connection.ehlo()
        connection.starttls()
        # connection.ehlo()
        result = connection.login("*******", "****")
        connection.sendmail(
            from_addr="*****",
            to_addrs="*****",
            msg=f"Subject:Ratings Changed!\n\n{message}\n{url}"
        )