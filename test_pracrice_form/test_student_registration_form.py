from selene import have, command
from selene.support.shared import browser
from demoqa_tests_practice.utils import resource


class Student:
    first_name = "Alyona"
    last_name = "Tch"
    email = "verypyc@gmail.com"
    gender = "Female"
    mobile = "9998887788"
    date_of_birth = {"day": "27", "month": "01", "year": "1992"}
    subjects = "Maths"
    hobbies = "Sports"
    picture = "test.jpeg"
    address = "Street"
    state = "Uttar Pradesh"
    city = "Merrut"


def test_registration_form():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type(Student.first_name)
    browser.element("#lastName").type(Student.last_name)
    browser.element("#userEmail").type(Student.email)
    browser.element('[for="gender-radio-2"]').click()
    browser.element("#userNumber").type(Student.mobile)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1992"]').click()
    browser.element('.react-datepicker__month-select [value="1"]').click()
    browser.element('.react-datepicker__day--027').click()
    browser.element("#subjectsInput").type(Student.subjects).press_tab()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(resource('pepe.png'))
