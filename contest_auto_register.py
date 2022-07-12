from selenium import webdriver
import smtplib  # for sending mails
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# these imports help for program to wait until page loads
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def register(CHROME_DRIVER_PATH,CODEFORCES_USERNAME,CODEFORCES_PASSWORD,SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD):

    chrome_driver_path = CHROME_DRIVER_PATH
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver.get("https://codeforces.com/enter?back=%2Fcontests")
    handle = driver.find_element(By.ID, "handleOrEmail")

    password = driver.find_element(By.ID, "password")

    handle.send_keys(CODEFORCES_USERNAME)
    password.send_keys(CODEFORCES_PASSWORD)
    driver.find_element(By.CLASS_NAME, "submit").click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))
        )
        print("Successfully logged in")
        while True:
            try:
                register_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Register")
                register_button.click()

                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.NAME, "takePartAs"))
                    )
                    print("Registration page loaded")

                    contest_name = driver.find_element(By.TAG_NAME, "h2").text
                    driver.find_element(By.NAME, "takePartAs").click()
                    driver.find_element(By.CLASS_NAME, "submit").click()
                    try:
                        element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))
                        )
                        print("Back to contest page after accepting terms")
                        try:
                            driver.find_element(By.CLASS_NAME, "welldone")
                            with smtplib.SMTP("outlook.office365.com", port=587) as connection:
                                connection.starttls()
                                result = connection.login(SENDER_EMAIL, SENDER_PASSWORD)
                                connection.sendmail(from_addr=SENDER_EMAIL,
                                                    to_addrs=RECEIVER_EMAIL,
                                                    msg=f"Subject:Registered for contest \n\nHey! CELF this side. \nI've "
                                                        f"auto registered you for:\n\n "
                                                        f"{contest_name} \n\nHave a good time buddy :)")
                        except NoSuchElementException:
                            print("Failed registration")
                            break
                    except TimeoutException:
                        print("Updated contest page loading took too much time!")
                        break
                except TimeoutException:
                    print("Registration page loading took too much time!")
                    break
            except NoSuchElementException:
                print("No new contest")
                break

    except TimeoutException:
        print("Contest Page loading took too much time!")

    driver.close()
