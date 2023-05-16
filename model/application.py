from selene import browser

from model.components.left_panel import LeftPanel
from model.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.left_panel = LeftPanel()
        self.simple_registration_form = SimpleRegistrationPage()

    def open(self):
        browser.open("/forms")


app = Application()
