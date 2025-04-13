
from behave import given, when, then

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

@given(u'User chooses the page link')
def choose_link(context):

    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.navigate()
    search_page.search_for("Mina vänner")
    # search_page.search_for("Välkommen!")
    sleep(0)

@when(u'User browse the button options')
def check_buttons(context):

    search_page = SearchPage(context.page)
    search_page.get_by("link", "Ny vän")
    expect(context.page.get_by_text('Fyll i båda fälten för att lägga till din vän')).to_be_visible()
    sleep(0)
    search_page.get_by("link", "Vänlista")
    expect(context.page.get_by_text('Jean-Luc Picard')).to_be_visible()
    sleep(0)
    search_page.get_by("link", "Start")


@then(u'first page is show')
def see_first_page(context):

    expect(context.page.get_by_text('Här hittar du dina vänner')).to_be_visible()
    sleep(0)