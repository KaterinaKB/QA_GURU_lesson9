import os

from selene import browser, have, command


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(2)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def choose_female_gender(self):
        browser.element('[value="Female"] + label').click()
        return self

    def fill_phone_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.all(".react-datepicker__month-select option").element_by(
            have.exact_text(month)
        ).click()
        browser.element(".react-datepicker__year-select").click()
        browser.all(".react-datepicker__year-select option").element_by(
            have.exact_text(year)
        ).click()
        browser.all(".react-datepicker__day").element_by(have.exact_text(day)).click()
        return self

    def fill_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()
        return self

    def choose_reading_as_hobby(self):
        browser.all("[for^=hobbies]").element_by(have.exact_text("Reading")).click()
        return self

    def select_picture(self, value):
        project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        resources_path = os.path.join(project_root_path, "tests", "resources")
        browser.element("#uploadPicture").type(f"{resources_path}/{value}")
        return self

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def choose_state(self, value):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.all("#state div").element_by(have.exact_text(value)).click()
        return self

    def choose_city(self, value):
        browser.element("#city").click()
        browser.all("#city div").element_by(have.exact_text(value)).click()
        return self

    def submit(self):
        browser.element("#submit").press_enter()

    def should_have_registered_user_with(
        self,
        full_name,
        email,
        gender,
        phone,
        birthday,
        subject,
        hobby,
        picture,
        address,
        state_and_city,
    ):
        browser.all(".table").all("td").should(
            have.exact_texts(
                ("Student Name", full_name),
                ("Student Email", email),
                ("Gender", gender),
                ("Mobile", phone),
                ("Date of Birth", birthday),
                ("Subjects", subject),
                ("Hobbies", hobby),
                ("Picture", picture),
                ("Address", address),
                ("State and City", state_and_city),
            )
        )
