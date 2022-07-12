from rating_tracker import track
from contest_auto_register import register

SENDER_EMAIL = "____________"
SENDER_PASSWORD = "____________"
RECEIVER_EMAIL = "____________"
CODEFORCES_PROFILE_URL = "https://codeforces.com/profile/____________"

CHROME_DRIVER_PATH = "____________"
CODEFORCES_USERNAME = "____________"
CODEFORCES_PASSWORD = "____________"

track(SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD, CODEFORCES_PROFILE_URL)
register(CHROME_DRIVER_PATH, CODEFORCES_USERNAME, CODEFORCES_PASSWORD,SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD)
