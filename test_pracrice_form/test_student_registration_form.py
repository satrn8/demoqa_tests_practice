from selene import have, command
from selene.support.shared import browser


class Student:
    first_name = "Alyona"
    last_name = "Tch"
    email = "verypyc@gmail.com"
    gender = "Female"
    mobile = "9998887788"
    date_of_birth = {"day": "14", "month": "06", "year": "2022"}
    subjects = "math"
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
    browser.element("#dateOfBirthInput").type(Student.date_of_birth)






