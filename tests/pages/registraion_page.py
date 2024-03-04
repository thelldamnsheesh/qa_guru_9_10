import os
from selene import browser, command, have, by

class RegistrationPage:
    def open_page(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#lastName').type(value)

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

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, file):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'../resources/{file}'))

    def fill_adress(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self,value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def select_city(self,value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def page_zoom(self, value):
        browser.driver.execute_script(f"document.body.style.zoom='{value}%'")

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_info(self, name, email, gender, phone, DateOfBirth, subject, hobbie, adress, city):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-body').should(have.text(name))
        browser.element('.modal-body').should(have.text(email))
        browser.element('.modal-body').should(have.text(gender))
        browser.element('.modal-body').should(have.text(phone))
        browser.element('.modal-body').should(have.text(DateOfBirth))
        browser.element('.modal-body').should(have.text(subject))
        browser.element('.modal-body').should(have.text(hobbie))
        browser.element('.modal-body').should(have.text(adress))
        browser.element('.modal-body').should(have.text(city))
