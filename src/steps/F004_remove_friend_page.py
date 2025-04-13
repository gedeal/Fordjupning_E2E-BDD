import re

import playwright
from behave import given, when, then
from time import sleep

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect


@given(u'User has a friend in the list')
def step_choose_friend(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Vänlista")
    expect(context.page.get_by_text('William Riker')).to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).to_be_visible()
    expect(context.page.get_by_text('Jean-Luc Picard')).to_be_visible()

    sleep(0)


@when(u'User removes the friend')
def step_erase_name(context):
    (context.page.get_by_role("main")
     .locator("div")
     .filter(has_text="William Riker")
     .locator("button")
     .click()
     )
    sleep(0)


@then(u'friend name is not in the list')
def step_verify(context):
    expect(context.page.get_by_text('William Riker')).not_to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).not_to_be_visible()
    expect(context.page.get_by_text('Jean-Luc Picard')).to_be_visible()
    sleep(0)