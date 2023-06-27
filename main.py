from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget
from post import Lol
class Bot:
    def __init__(self):
        self.login("username", "password")

    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com/")
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
        )
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        self.click_save_info_button()
        self.crawl_explore_page()

    def click_not_now_button(self):
        not_now_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button"))
        )
        not_now_button.click()

    def click_save_info_button(self):
        save_info_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))
        )
        save_info_button.click()

    def crawl_explore_page(self):
        self.driver.get('https://www.instagram.com/explore/')
        time.sleep(3)  # Wait for the page to load

        # Find and extract post metadata
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        keyword = "programming"
        self.driver.get("https://www.instagram.com/explore/tags/" + keyword + "/")

        # Wait for 5 seconds
        time.sleep(5)

        # Scroll down to scrape more images
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Target all images on the page
        images = self.driver.find_elements(By.TAG_NAME, 'img')
        images = [image.get_attribute('src') for image in images]
        images = images[:-2]

        print('Number of scraped images: ', len(images))
        path = os.getcwd()
        path = os.path.join(path, keyword + "s")
        
        path = "C:\instabot\pics"

        counter = 0
        for image in images[3:]:
            save_as = os.path.join(path, keyword + str(counter) + '.jpg')
            wget.download(image, save_as)
            counter += 1

       
def main():
    my_bot = Bot()

if __nam__ == '__main__':
    main()



class Bot(Lol):
    def _init_(self):
        super()._init_()

    def crawl_explore_page(self):
        super().crawl_explore_page()
        # Add additional code specific to Bot class

def main():
    my_bot = Bot()

if __name__ == '__main__':
    main()
