
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.command import Command
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class Browser:
    @classmethod
    def create(cls, url, proxy=None):
        self = cls()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--output=/dev/null")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-crash-reporter")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-in-process-stack-traces")
        
        if proxy:
            print(f'Start browser with proxy {proxy}')
            chrome_options.add_argument(f"--proxy-server={proxy}")
        self.browser = webdriver.Chrome(options=chrome_options)
        self.delay = 10
        self.is_available = True
        self.proxy = proxy
        self.discard = False
        self.dev_tools = None
        self.url = url
        return self
    
    def get_by(self, indetificator, locator):
        try:
            return WebDriverWait(self.browser, self.delay).until(EC.presence_of_element_located((locator, indetificator)))
        except TimeoutException:
            print(f"Timeout for {locator} {indetificator}")
        except Exception as e:
            print(e)
        return None
    
    def get_by_class(self, class_name):
        return self.get_by(class_name, By.CLASS_NAME)

    def get_by_id(self, id):
        return self.get_by(id, By.ID)
    
    def get_by_xpath(self, xpath):
        # try:
        return self.get_by(xpath, By.XPATH)
            # return self.browser.find_element(By.XPATH, xpath)
        # except Exception as e:
        #     print(e)
        #     return None
    
    def get_page(self, url):
        self.browser.execute(Command.GET, {'url': url})
        print(f'navigate to {url}')
    
    def force_click(self, element):
        ActionChains(self.browser).move_to_element(element).click(element).perform()
        self.browser.implicitly_wait(self.delay)
    
    def close(self):
        self.browser.quit()
