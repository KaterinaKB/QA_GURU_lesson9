from model.pages.registration_page import RegistrationPage


def test_registration_with_valid_data():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (
        registration_page.fill_first_name("Kate")
        .fill_last_name("Voronova")
        .fill_email("test@ya.ru")
        .choose_female_gender()
        .fill_phone_number("7123456789")
        .fill_date_of_birth("2001", "September", "15")
        .fill_subject("Computer Science")
        .choose_reading_as_hobby()
        .select_picture("Grogu.jpg")
        .fill_current_address("Bolshaya Sadovaya Street 302-bis")
        .choose_state("NCR")
        .choose_city("Delhi")
    )
    registration_page.submit()

    # THEN
    registration_page.should_have_registered_user_with(
        "Kate Voronova",
        "test@ya.ru",
        "Female",
        "7123456789",
        "15 September,2001",
        "Computer Science",
        "Reading",
        "Grogu.jpg",
        "Bolshaya Sadovaya Street 302-bis",
        "NCR Delhi",
    )
