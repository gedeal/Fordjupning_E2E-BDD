import re

import playwright
from behave import given, when, then
from time import sleep

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect


@given(u'User chooses to add a friend')
def step_add_friend(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Ny vän")


@when(u'User adds a friend and epost')
def step_add_name_epost(context):
    context.page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox").click()
    context.page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox").fill("John No name")
    context.page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox").click()
    context.page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox").fill("NoName@inter.net")


@then(u'user saves friend to the list')
def step_save_name(context):
    sleep(0)
    context.page.get_by_role("button", name="Spara").click()

@then(u'user see friend name in the list')
def step_verify_name_in_list(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Vänlista")

    expect(context.page.get_by_text('John No name')).to_be_visible()
    expect(context.page.get_by_text('NoName@inter.net')).to_be_visible()
    sleep(0)


