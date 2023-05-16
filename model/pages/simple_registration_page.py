from selene import browser, have
from data.users import Users


class SimpleRegistrationPage:
    def __init__(self):
        self.full_name = browser.element("#userName")
        self.email = browser.element("#userEmail")
        self.current_address = browser.element("#currentAddress")
        self.permanent_address = browser.element("#permanentAddress")
        self.submit = browser.element("#submit")
        self.output_name = browser.element("[id=output] [id=name]")
        self.output_email = browser.element("[id=output] [id=email]")
        self.output_current_address = browser.element("[id=output] [id=currentAddress]")
        self.output_permanent_address = browser.element(
            "[id=output] [id=permanentAddress]"
        )

    def register(self, user: Users):
        self.full_name.type(f"{user.first_name} {user.last_name}")
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit.click()

    def should_have_registered_user_with(self, user: Users):
        self.output_name.should(have.text(f"{user.first_name} {user.last_name}"))
        self.output_email.should(have.text(user.email))
        self.output_current_address.should(have.text(user.current_address))
        self.output_permanent_address.should(have.text(user.permanent_address))
