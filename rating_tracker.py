import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

def track(SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD, CODEFORCES_PROFILE_URL):
    url = CODEFORCES_PROFILE_URL
    header = {
        #just an example
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)_________________",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.content, "lxml")
    # print(soup.prettify())

    parent = soup.find(class_="info")
    current_rank = list(parent.find(class_="user-rank").descendants)[1].getText()
    current_rating = int(list(parent.find("li").descendants)[3].getText())
    file = open("rating.txt", "r")
    prev_rating=file.readline()
    if(prev_rating==""):
        prev_rating=0

    if current_rating != int(prev_rating):
        message = f"Hola!\nYour rating has changed by {current_rating - int(prev_rating)} \nNow your rating is {current_rank} {current_rating}\nCheck out your new achievement"
        file.close()
        file=open("rating.txt","w")
        file.write(str(current_rating))
        file.close()
        with smtplib.SMTP("outlook.office365.com", port=587) as connection:
            # connection.set_debuglevel(1)
            connection.starttls()
            result = connection.login(SENDER_EMAIL, SENDER_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Ratings Changed!\n\n{message}\n{url}"
            )
            print("Sent")

#            raise SMTPDataError(code, resp)
# smtplib.SMTPDataError: (554, b'5.2.0 STOREDRV.Submission.Exception:OutboundSpamException; Failed to process message due to a permanent exception with message
# [BeginDiagnosticData]WASCL UserAction verdict is not None. Actual verdict is Suspend, ShowTierUpgrade. OutboundSpamException: WASCL UserAction verdict is not
# None. Actual verdict is Suspend, ShowTierUpgrade.[EndDiagnosticData] [Hostname=AM0P193MB0417.EURP193.PROD.OUTLOOK.COM]')
