# CELF
A python project that keeps tabs on codeforces contest page and auto registers for upcoming contests along with a confirmation mail .It also monitor codeforces rating changes and relays an email notifications upon detecting updates.

you need to change the header as per your system and you must have python installed on your system;<br/>
go to main.py and fill all your details in place of ______<br/>
go to http://myhttpheader.com/ to find your browser headers.<br/>
open rating_tracker.py, go to line 8 -> header, copy paste your ```"User-Agent"``` and ```"Accept-Language"``` from the above website.<br/><br/>
![image](https://user-images.githubusercontent.com/75138802/179690099-f013bbba-8349-4180-be80-eef2bd320de9.png)<br/>
![image](https://user-images.githubusercontent.com/75138802/179697908-85eac915-2ee5-42be-bfdd-b6ec6879a4b4.png)<br/>
**--------------------------------------------Your rating tracker is up and ready to run.--------------------------------------------<br/><br/>**

Now for web automation I'll be using chrome, you need to download selenium and chromedriver as follows:<br/>
check out your google chrome version here chrome://settings/help<br/><br/>
![image](https://user-images.githubusercontent.com/75138802/179691786-5a6a0b6c-1eaa-4ebe-ab49-e3ffd5a2da9f.png)<br/><br/>
go to https://chromedriver.chromium.org/downloads and download chrome driver **corresponding to your chrome version only**.<br/><br/>
![image](https://user-images.githubusercontent.com/75138802/179692220-210e3c2a-8ab7-4115-88ce-5cefa3e576f5.png)<br/><br/>
extract it in suitable location ,copy the path and paste it in line 9 of main.py CHROME_DRIVER_PATH="_________\chromedriver.exe"<br/><br/>
![image](https://user-images.githubusercontent.com/75138802/179694247-4a294854-30fc-43d6-b50f-dec2b048b4a7.png)<br/><br/>
now run this command in cmd -> ```pip install selenium``` <br/><br/>
**----------------------------------You are all set to use both auto registration and rating tracker.----------------------------------**<br/><br/>
Now I have used windows task scheduler to run this program every 3 hours.Ths article will help you set up the same <br/> https://medium.com/analytics-vidhya/scheduling-scripts-using-task-scheduler-ced4d98a5be5



