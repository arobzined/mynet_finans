from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class Scraping():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.mynet_dict = dict()
        self.url = "https://finans.mynet.com/borsa/hisseler/"
    def open_page(self):
        self.driver.get(self.url)
        self.wait(By.XPATH, '/html/body/section/div[1]/div[1]/div[3]/div/div/div[1]/h1')
        self.run()
        self.driver.close()

    def wait(self, selector, value, time: int = 20):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located((selector, value)))

    def run(self):

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        rows = soup.find_all(class_ = 'mr-4')

        for elm in rows:

            link = (elm.find('a').attrs)["href"]
            self.driver.get(link)
            self.wait(By.XPATH, '/html/body/section/div[1]/div[1]/div[3]/div/div[1]/div[3]/div[2]')

            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            box = soup.find_all(class_ = "flex align-items-center justify-content-between")
            current_url = self.driver.current_url

            key, that_dict = self.get_attributes(box, current_url)

            self.mynet_dict[key] = that_dict
            print(current_url)

        print(self.mynet_dict)

        return
    def get_attributes(self, box_, current_url):
        that_dict = dict()
        i = 0
        for elm in box_:
            if i == 0:
                i += 1
                continue
            spans = elm.find_all("span")
            that_dict[spans[0].text] = spans[1].text
        current_url = self.driver.current_url
        url_ = self.url
        key = current_url.replace(url_, "")
        return key, that_dict




