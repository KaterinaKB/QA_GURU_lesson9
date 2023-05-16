from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.container = browser.element(".left-pannel")

    def open_form(self, group, item):
        self.container.all(".header-text").element_by(have.exact_text(group)).click()
        self.container.all(".text").element_by(have.exact_text(item)).click()

    def open_simple_registration_form(self):
        self.open_form("Elements", "Text Box")
