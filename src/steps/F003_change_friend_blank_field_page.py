import re
from behave import given, when, then
from time import sleep
from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect


@given(u'User chooses to change friend name')
def step_choose_friend(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Vänlista")
    expect(context.page.get_by_text('William Riker')).to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).to_be_visible()

    # context.page.locator(':nth-match(:text("Ändra"), 5)').click()
    (context.page.get_by_role("main")
     .locator("div")
     .filter(has_text="James T. Kirk")
     .locator("a")
     .click()
     )

@when(u'User erases the friend name')
def step_change_info(context):

    expect(context.page.get_by_text("Fyll i båda fälten för att ä")).not_to_be_visible()
    context.page.get_by_role("textbox").nth(0).click()
    context.page.get_by_role("textbox").nth(0).fill("")     # ERROR
    context.page.get_by_role("textbox").nth(1).click()
    context.page.get_by_role("textbox").nth(1).fill("EMAIL")
    sleep(0)

@then(u'system shows error message - name')
def step_show_error_message(context):
    expect(context.page.get_by_text("Fyll i båda fälten för att ä")).to_be_visible()
    sleep(0)

## -------------------------------------------------------------

@given(u'User chooses to change friend email')
def step_choose_friend(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Vänlista")
    expect(context.page.get_by_text('William Riker')).to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).to_be_visible()

    # context.page.locator(':nth-match(:text("Ändra"), 5)').click()
    (context.page.get_by_role("main")
     .locator("div")
     .filter(has_text="James T. Kirk")
     .locator("a")
     .click()
     )


@when(u'User erases the friend email')
def step_change_info(context):

    expect(context.page.get_by_text("Fyll i båda fälten för att ä")).not_to_be_visible()
    context.page.get_by_role("textbox").nth(0).click()
    context.page.get_by_role("textbox").nth(0).fill("NAME")
    context.page.get_by_role("textbox").nth(1).click()
    context.page.get_by_role("textbox").nth(1).fill("")     # ERROR
    sleep(0)


@then(u'system shows error message - email')
def step_show_error_message(context):
    expect(context.page.get_by_text("Fyll i båda fälten för att ä")).to_be_visible()
    sleep(2)