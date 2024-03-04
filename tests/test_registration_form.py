from tests.pages.registraion_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open_page()

    registration_page.fill_first_name('Пользователь')
    registration_page.fill_last_name('Тестовый')
    registration_page.fill_email('Test@gmail.com')
    registration_page.select_gender('Male')
    registration_page.fill_phone_number('8005553535')
    registration_page.fill_date_of_birth('13', 'June', '1995')
    registration_page.select_subject('Maths')
    registration_page.select_hobby('Sports')
    registration_page.upload_picture('mem.jpg')
    registration_page.fill_address('Russia, Moscow')
    registration_page.select_state('Uttar Pradesh')
    registration_page.select_city('Agra')
    registration_page.submit_form()

    registration_page.should_have_registered(
        'Пользователь',
        'Тестовый',
        'Test@gmail.com',
        'Male',
        '8005553535',
        '13',
        'June',
        '1995',
        'Maths',
        'Sports',
        'mem.jpg',
        'Russia, Moscow',
        'Uttar Pradesh',
        'Agra')

    registration_page.close_modal_window()
