from model.application import app
from data.users import student


def test_simple_registration_form_with_valid_data():
    app.open()
    app.left_panel.open_simple_registration_form()

    app.simple_registration_form.register(student)

    app.simple_registration_form.should_have_registered_user_with(student)
