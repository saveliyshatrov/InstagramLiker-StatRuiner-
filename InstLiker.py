from selenium import webdriver
from time import sleep
import os
import random

class Liker:
    def __init__(self) -> None:
        self.username = 'username'
        self.password = 'password'
        self.hashtags = []
        self.numberOfLikes = 0
        self.userToLike = 'username'
        self.urlForTags = 'https://www.instagram.com/explore/tags/'
        self.urlForUsers = 'https://www.instagram.com/'
        self.XPath_username = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input'
        self.XPath_password = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input'
        self.LoginButton = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button'
        self.XPath_post = ''
        self.Top = '/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]'
        self.Recent = '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]'

        self.XPath_forUsersPage = '/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]'
        self.XPath_forUsersLike = '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button'
        self.XPath_forUsersNextPhoto_1 = '/html/body/div[4]/div[1]/div/div/a'
        self.XPath_forUsersNextPhoto = '/html/body/div[4]/div[1]/div/div/a[2]'
        self.driver = webdriver.Firefox()

        #__._sakura___._

    def checkPrevWork(self):
        if True:
            pass
        else:
            pass

    def SetInfo(self, username:str = 'username', password:str = 'password', hashtags:list = [], numberOfLikes:int = 100, userToLike: str = 'userToLike', Top: bool = False) -> None:
        self.username = username
        self.password = password
        self.hashtags = hashtags
        self.numberOfLikes = numberOfLikes
        self.userToLike = userToLike
        if Top == False:
            self.XPath_post = self.Recent
        if Top == True:
            self.XPath_post = self.Top

    def Sleep(self, time: int, showStatistics: bool, nowLikes: int = 0, allLikes: int = 0, hashtag: str = ''):
        time = random.randrange(int(time/3), time*2)
        for i in range(time):
            if showStatistics == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("{} secs left of {}".format(i + 1, time))
                sleep(1)
            if showStatistics == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("{} secs left of {}".format(i + 1, time))
                print("#{} of #{}".format(nowLikes, allLikes))
                print('#{}'.format(hashtag))
                sleep(1)

    def Login(self):
        self.driver.get("http://www.instagram.com")
        self.Sleep(10, False)
        self.driver.find_element_by_xpath(self.XPath_username).send_keys(self.username)
        print("Username was entered")
        self.driver.find_element_by_xpath(self.XPath_password).send_keys(self.password)
        print("Password was entered")
        self.driver.find_element_by_xpath(self.LoginButton).click()
        self.Sleep(5, False)

    def UserLiker(self):
        pass
    #

    def HashtagLiker(self):
        for hashtag in self.hashtags:
            self.driver.get(self.urlForTags + hashtag + '/')
            self.Sleep(5, False)
            self.driver.find_element_by_xpath(self.XPath_post).click()
            iterations = 0
            for HowManyLiked in range(self.numberOfLikes):
                try:
                    if HowManyLiked == 0:
                        self.Sleep(3, False)
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]').click()
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
                        self.Sleep(3, True, HowManyLiked+1, self.numberOfLikes, hashtag)
                        iterations += 1
                    if HowManyLiked > 0:
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]').click()
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                        self.Sleep(3, True, HowManyLiked+1, self.numberOfLikes, hashtag)
                        iterations += 1
                except Exception:#Если тут ломается то просто пропускает пост
                    try:
                        self.Sleep(5, True, HowManyLiked+1, self.numberOfLikes, hashtag)
                        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
                        self.Sleep(3, True, HowManyLiked+1, self.numberOfLikes, hashtag)
                        iterations += 1
                    except Exception:#если на этом этапе ломатся, то он открывает заново ссылку и переходит к тому моменту где остановился
                        self.driver.get(self.urlForTags + hashtag + "/")
                        self.Sleep(5, True, HowManyLiked+1, self.numberOfLikes, hashtag)
                        for i in range(iterations):
                            self.driver.find_element_by_xpath(self.XPath_post).click()
                            if i == 0:
                                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]').click()
                                self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
                            else:
                                self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()

    def run(self, userLiking: bool = False):
        self.Login()
        if userLiking == False:
            self.HashtagLiker()
        if userLiking == True:
            self.UserLiker()


String = "photographyart #photographyoftheday #photographyy #photographylove #photographyaddict #photographyskills #photographybook #photographyprops #photographydaily #photographyisart #photographyaccount #photographystudio #photographyday #photographynature #photographysoul #photographystudent #photographyworkshop #photographyindonesia #photographyblog #photographyig #photographybusiness #photography101"
string = String.replace(" ", "")
array = string.split("#")


Liker = Liker()
Liker.SetInfo(username='username', password='password', hashtags=array, numberOfLikes=100)
Liker.run()
