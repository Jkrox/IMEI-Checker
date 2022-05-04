# Selenium module imports

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException as TE

# Python default modules.
import sys,os

# Colorama module: pip install colorama
from colorama import init, Fore, Style


"""Colorama module constants."""
init(convert=True)  # Init colorama module.
red = Fore.RED  # Red color.
green = Fore.GREEN  # Green color.
yellow = Fore.YELLOW  # Yellow color.
reset = Style.RESET_ALL  # Reset color attribute.

class hCaptcha:
    '''Main class of the captcha Solver'''

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.extension_path = 'assets/Tampermonkey.crx'
        self.driver = self.webdriver()
        

    def webdriver(self):
        options = webdriver.ChromeOptions()
        options.add_extension(self.extension_path)
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        options.add_argument('log-level=3')
        options.add_argument('--mute-audio')
        options.add_argument('--ignore-certificate-error')
        options.add_argument('--ignore-ssl-error')
        options.add_argument('--start-maximized')
        options.add_argument("--enable-webgl-draft-extensions")
        driver = webdriver.Chrome(service=self.service, options=options)
        return driver

    def element_clickable(self, element: str) -> None:
        '''Click on element if it's clickable using Selenium'''
        WDW(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    def element_visible(self, element: str):
        """Check if element is visible using Selenium."""
        return WDW(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, element)))

    def window_handles(self, window_number: int):
        """Check for window handles and wait until a specific tab is opened."""
        WDW(self.driver, 30).until(lambda _: len(self.driver.window_handles) == window_number + 1)
        # Switch to asked tab.
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def download_usercript(self) -> None:
        """Download the hCaptcha solver userscript."""
        try:
            print('Installing the hCaptcha solver userscript.', end=' ')
            #self.window_handles(1)  # Wait that Tampermonkey tab loads.
            self.driver.get('https://greasyfork.org/en/scripts/425854-hcaptcha'
                            '-solver-automatically-solves-hcaptcha-in-browser')
            # Click on "Install" Greasy Fork button.
            self.element_clickable('//*[@id="install-area"]/a[1]')
            # Click on "Install" Tampermonkey button.
            self.window_handles(2)  # Switch on Tampermonkey install tab.
            self.element_clickable('//*[@id="input_SW5zdGFsYXJfdW5kZWZpbmVk_bu"]')
            self.window_handles(1)  # Switch to Greasy Fork tab.
            self.driver.close()  # Close this tab.
            self.window_handles(0)  # Switch to main tab.
            print(f'{green}Installed.{reset}')
        except TE:
            sys.exit(f'{red}Failed.{reset}')

    def __str__(self):
        return '''\thCaptcha Solver
{green}Made by Jkrox'''

if __name__ == '__main__':
    os.system('cls') #
    print('hCaptcha Solver'
          f'\n{green}Made by Jeikrox.')
