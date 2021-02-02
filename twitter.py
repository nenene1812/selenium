from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

tweet = 'Cannot waiting, Hold my beer, bro'
driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

email_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'
username = 'bjhgjj'
password = 'K565OO65Z8DYNVL'
email = 'bjhgjj@hotmail.com'
time.sleep(1)

driver.find_element_by_xpath(email_xpath).send_keys(username)
time.sleep(0.5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(0.5)
driver.find_element_by_xpath(login_xpath).click()


time.sleep(4)

tweet_xpath = '/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span'
msg_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
tweet_btn_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span'

email_input_xpath ='//*[@id="challenge_response"]'
email_confirm_xpath = '//*[@id="email_challenge_submit"]'

driver.find_element_by_xpath(email_input_xpath).send_keys(email)
time.sleep(0.6)
driver.find_element_by_xpath(email_confirm_xpath).click()
time.sleep(0.7)


driver.find_element_by_xpath(tweet_xpath).click()
time.sleep(0.5)
driver.find_element_by_xpath(msg_xpath).send_keys(tweet)
time.sleep(0.7)
driver.find_element_by_xpath(tweet_btn_xpath).click()