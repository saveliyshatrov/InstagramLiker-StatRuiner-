from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os



username = ''
password = ''
hashtags = ['eye', 'photo', 'macro', 'hazel']
urlTag = 'https://www.instagram.com/explore/tags/'

def Sleep(time: int, showStat: bool = False, now: int = 0, _all: int = 0) -> None:
    for i in range(time):
        if showStat == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} secs left of {}".format(i + 1, time))
            sleep(1)
        if showStat == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} secs left of {}".format(i + 1, time))
            print("#{} of #{}".format(now, _all))
            sleep(1)

driver = webdriver.Firefox()
driver.get("http://www.instagram.com")

Sleep(10)
os.system('cls' if os.name == 'nt' else 'clear')

Username = driver.find_element_by_name('username')
Password = driver.find_element_by_name('password')


Username.send_keys(username)
print("Username entered")
Password.send_keys(password)
print("Password entered")

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
Sleep(5)
#driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
#Sleep(5)
#driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

for hashtag in hashtags:
    HowManyToLike = 100
    HowManyLiked = 0
    driver.get(urlTag + hashtag + "/")
    Sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()
    Sleep(3)
    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]").click()
    driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
    HowManyLiked += 1
    Sleep(3, True, HowManyLiked, HowManyToLike)
    for i in range(HowManyToLike - 1):
        try:
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]").click()
            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
            HowManyLiked += 1
            Sleep(3, True, HowManyLiked, HowManyToLike)
        except Exception:
            pass
        #/html/body/div[4]/div[1]/div/div/a
    #/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]
