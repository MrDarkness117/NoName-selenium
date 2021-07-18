class BasePage(object):
    """
    Pass in the URL for go() value through page objects (VK (auth_passed.py), CheckAuth (auth_control.py))
    Передача URL в метод go() через объекты страниц (VK, CheckAuth)
    """

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)