import re
from behave import given, when, then
from time import sleep
from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect

@given(u'User chooses to change friends info')
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

@when(u'User changes the friends name and epost')
def step_change_info(context):

    context.page.get_by_role("textbox").nth(0).click()
    context.page.get_by_role("textbox").nth(0).fill("NAME")
    context.page.get_by_role("textbox").nth(1).click()
    context.page.get_by_role("textbox").nth(1).fill("EMAIL")
    sleep(0)

@then(u'user saves changes to the list')
def step_save_changes(context):
    context.page.get_by_role("button", name="Spara").click()
    sleep(0)


@then(u'user see friends changes in the list')
def step_verify_changes(context):
    expect(context.page.get_by_text('NAME')).to_be_visible()
    expect(context.page.get_by_text('EMAIL')).to_be_visible()
    sleep(0)




