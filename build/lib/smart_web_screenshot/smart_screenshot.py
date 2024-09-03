import logging
import string
import time
import random

from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

import undetected_chromedriver as uc


class SmartWebScreenShot:

    def __init__(self, user_agent=None, proxy=None, screen_dimensions="1920,1080"):
        self.driver = None
        self.user_agent = self.get_random_user_agent(user_agent)
        self.proxy = proxy
        self.screen_dimensions = screen_dimensions

    def get_domain_name(self, url):

        name = random.choices(string.ascii_letters, k=7)

        try:
            parsed_url = urlparse(url)
            name = parsed_url.netloc
            name = name.split(".")[1]

        except Exception:
            logging.error("Failed to get name from")
        return name

    def get_random_user_agent(self, user_agent):
        if user_agent:
            return user_agent

        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
        ]
        return random.choice(user_agents)

    def solve_captcha(self, site_key, url):
        # Coming Soon!
        pass

    def setup_driver(self, headless=True):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"user-agent={self.user_agent}")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument(f"--window-size={self.screen_dimensions}")
        if self.proxy:
            chrome_options.add_argument(f"--proxy-server={self.proxy}")
        self.driver = uc.Chrome(options=chrome_options)

    def take_screenshot(self, url):
        """Initialize the screenshot"""

        if self.driver is None:
            raise ValueError("Driver is not initialized. Call setup_driver() first.")

        self.driver.get(url)
        name = self.get_domain_name(url)
        time.sleep(5)  # Wait for content to load
        self.driver.save_screenshot(f"{name}.png")
        logging.warning(f"Screenshot saved as {name}.png")

    def close_driver(self):
        if self.driver:
            self.driver.quit()
