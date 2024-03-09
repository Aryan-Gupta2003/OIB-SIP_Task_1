from selenium import webdriver
import text_to_speech as ts

class info():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_info(self, query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org')
        search = self.driver.find_element("xpath" ,'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath" ,'//*[@id="search-form"]/fieldset/button')
        enter.click()
        paragraphs = self.driver.find_elements("xpath", '//*[@id="mw-content-text"]/div[1]/p[2]')
        text = ""
        for paragraph in paragraphs[:1]:
            text += paragraph.text + "\n"
        ts.say(text)


    
    def keep_open_forever(self):
        input("Press Enter to close the browser...")
        
    def close(self):
        self.driver.quit()
