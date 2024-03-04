from selene import browser, command, have, by
from resources import resource


class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        if value == 'Male':
            browser.all('[for^=gender-radio-1]').element_by(have.exact_text(value)).click()
        if value == 'Female':
            browser.all('[for^=gender-radio-2]').element_by(have.exact_text(value)).click()
        if value == 'Other':
            browser.all('[for^=gender-radio-3]').element_by(have.exact_text(value)).click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(month)
        ).click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(year)
        ).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def select_subject(self, value):
        browser.element('#subjectsInput').type(value).press_tab()

    def select_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, file):
        browser.element("#uploadPicture").set_value(resource.path(file))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self, first_name, last_name, email, gender, phone, day, month, year, subject,
                               hobby, picture, address, state, city):

        browser.all('.table td:nth-child(2)').should(
            have.texts(f'{first_name} {last_name}', email, gender, phone, f'{day} {month},{year}', subject,
                       hobby, picture, address, f'{state} {city}')
        )

    def close_modal_window(self):
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()
