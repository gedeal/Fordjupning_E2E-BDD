import re
from playwright.sync_api import expect

class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("#search-input")

    def navigate(self):
        self.page.goto("https://forverkliga.se/JavaScript/my-contacts/#/")

    def search_for(self, query):
        expect(self.page).to_have_title(re.compile(query))
        # expect(self.page).get_by_role(re.compile("Välkommen!"))

        # self.page.get_by_role("heading", name="Välkommen!")





