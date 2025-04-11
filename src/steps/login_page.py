import playwright
from behave import given, when, then

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect


@given(u'User chooses the link')
def step_choose_link(context):

    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.navigate()
    search_page.search_for("Mina vänner")
    # search_page.search_for("Välkommen!")

    search_page.get_by("link", "Start")
    search_page.get_by("link", "Vänlista")
    search_page.get_by("link", "Ny vän")
    # search_page.search_for("?")
    context.search_page = search_page


@when(u'User puts the link address')
def step_impl(context):
    context.page.get_by_role("button").get_by_text("")



@then(u'page is show')
def step_see_page(context):
    context.page.get_by_role("button").get_by_text("")
