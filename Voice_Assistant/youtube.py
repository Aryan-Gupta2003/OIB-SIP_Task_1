from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def play(self, query):
        self.query = query
        self.driver.get(url='https://www.youtube.com/results?search_query=' + query)
        video = self.driver.find_element("xpath" ,'//*[@id="video-title"]/yt-formatted-string')
        video.click()
    
    def keep_open_forever(self):
        input("Press Enter to close the browser...")

    def close(self):
        self.driver.quit()
