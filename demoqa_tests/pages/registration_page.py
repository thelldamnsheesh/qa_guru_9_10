import os
from selene import browser, command, have, by


class Registration_form:
    def open_page(self):
        browser.open('/automation-practice-form')

    def registration_user(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        if user.gender == 'Male':
            browser.all('[for^=gender-radio-1]').element_by(have.exact_text(user.gender)).click()
        if user.gender == 'Female':
            browser.all('[for^=gender-radio-2]').element_by(have.exact_text(user.gender)).click()
        if user.gender == 'Other':
            browser.all('[for^=gender-radio-3]').element_by(have.exact_text(user.gender)).click()
        browser.element('#userNumber').type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(
            by.text(user.month_of_birth)
        ).click()
        browser.element('.react-datepicker__year-select').click().element(
            by.text(user.year_of_birth)
        ).click()
        browser.element(f'.react-datepicker__day--0{user.day_of_birth}').click()
        browser.element('#subjectsInput').type(user.subject).press_tab()
        browser.all('[for^=hobbies-checkbox-1]').element_by(have.exact_text(user.hobbie)).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'../resources/{user.picture}'))
        browser.element('#currentAddress').type(user.adress)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()

    def zoom_page(self, value):
        browser.driver.execute_script(f"document.body.style.zoom='{value}%'")

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def should_registered_user_info(self, user):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element('.modal-body').should(have.text(f'{user.first_name} {user.last_name}'))
        browser.element('.modal-body').should(have.text(user.email))
        browser.element('.modal-body').should(have.text(user.gender))
        browser.element('.modal-body').should(have.text(user.phone))
        browser.element('.modal-body').should(have.text(f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}'))
        browser.element('.modal-body').should(have.text(user.subject))
        browser.element('.modal-body').should(have.text(user.hobbie))
        browser.element('.modal-body').should(have.text(user.adress))
        browser.element('.modal-body').should(have.text(f'{user.state} {user.city}'))