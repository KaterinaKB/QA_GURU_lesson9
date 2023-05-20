from demoqa.model.pages.registration_page import RegistrationPage
from demoqa.data.users import student
import allure

@allure.label('owner', 'Voronova K.')
@allure.description('Тест на успешную регистрацию в полной форме регистрации')
@allure.title('Регистрация с валидными данными')
def test_registration_with_valid_data():
    registration_page = RegistrationPage(student)
    registration_page.open()

    registration_page.register(student)

    registration_page.should_have_registered_user_with(student)
