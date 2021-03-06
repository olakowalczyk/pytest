from pages.form import FormPage
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

pytest_plugins = [
    'tests.config.browser'
]


def test_initial_values(browser):  # checks initial values
    form_page = FormPage(browser)
    form_page.load()
    assert form_page.firstname_input_value() == 'Mickey'
    assert form_page.lastname_input_value() == 'Mouse'


def test_clear(browser):  # checks clearing inputs
    form_page = FormPage(browser)
    form_page.load()
    form_page.clear_form()
    assert form_page.firstname_input_value() == ''
    assert form_page.lastname_input_value() == ''


def test_inputs(browser):  # checks new input values
    firstname = 'Donald'
    lastname = 'Duck'

    form_page = FormPage(browser)
    form_page.load()
    form_page.enter_firstname(firstname)
    form_page.enter_lastname(lastname)
    assert form_page.firstname_input_value() == firstname
    assert form_page.lastname_input_value() == lastname


def test_submit(browser):  # checks sumbit i.e. reload page
    firstname = 'Peter'
    lastname = 'Pan'

    form_page = FormPage(browser)
    form_page.load()
    form_page.enter_firstname(firstname)
    form_page.enter_lastname(lastname)
    form_page.submit()
    assert form_page.firstname_input_value() == 'Mickey'
    assert form_page.lastname_input_value() == 'Mouse'
