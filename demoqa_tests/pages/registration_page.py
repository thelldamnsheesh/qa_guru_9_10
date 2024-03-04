from selene import browser, command, have, by
from demoqa_tests import resource


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
        browser.all('[for^=hobbies-checkbox-1]').element_by(have.exact_text(user.hobby)).click()
        browser.element("#uploadPicture").set_value(resource.path(user.picture))
        browser.element('#currentAddress').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def read_modal_header(self):
        return browser.element('.modal-header')

    def read_table_data(self):
        return browser.all('.table td:nth-child(2)')

    def should_have_registered(self, user):
        self.read_modal_header().should(have.text("Thanks for submitting the form"))
        self.read_table_data().should(
            have.texts(f'{user.first_name} {user.last_name}', user.email, user.gender, user.phone,
                       f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}', user.subject,
                       user.hobby, user.picture, user.address, f'{user.state} {user.city}')
        )

    def close_modal_window(self):
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()
