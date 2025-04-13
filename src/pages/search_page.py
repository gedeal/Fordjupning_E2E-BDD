import re
from playwright.sync_api import expect
from time import sleep


class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("#search-input")

    def navigate(self):
        self.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/")
        sleep(0)


    def search_for(self, query):
        expect(self.page).to_have_title(re.compile(query))

    # page.get_by_role("heading", name="Mina vänner").click()
    # page.get_by_role("heading", name="Välkommen!").click()
    # page.get_by_text("Här hittar du dina vänner.").click()

    def get_by(self, type, txt):
        self.page.get_by_role(type, name=txt).click()
        sleep(0)


