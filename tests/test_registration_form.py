from demoqa_tests.pages.registration_page import Registration_form
from demoqa_tests.data.users import user


def test_registration_form():
    registration_page = Registration_form()
    registration_page.open_page()

    registration_page.registration_user(user)
    registration_page.submit_form()
    registration_page.should_have_registered(user)
    registration_page.close_modal_window()

