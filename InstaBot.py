from selenium import webdriver
from time import sleep
#from secrets import pw

#class for instagram bot
class InstaBot: 
    def __init__(self, username, pw):#parameters to take
        self.driver = webdriver.Chrome(r'C:\Users\Python\Chromium\chromedriver85.exe')#path where chromium is executed
        self.username = username #saving a ref to username incase it's needed in other methods
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")#url web address https://www.instagram.com/
        sleep(5)
        #get a-link that contains text login
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(5)
        #get input form that contains username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(5)
        #get input form that contains password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        #get abutton that contains submit
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")\
            .click()
        sleep(5)

    #function to get unfollowers
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(5)
        #get people following you
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names() #here
        #get people you are following
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\
            .click()
        followers = self._get_names()
        #compare users in following with users in followers
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(5)
        sugs = self.driver.find_element_by_xpath("//h4[contains(text(), Suggestions)]")
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)#javascript
        sleep(5)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script('''
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                ''', scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button")\
            .click()
        return names

#instant of the class bot
my_bot = InstaBot('id', 'pwd') #saving in a variable
my_bot.get_unfollowers()