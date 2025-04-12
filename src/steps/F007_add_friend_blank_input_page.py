import re

import playwright
from behave import given, when, then
from time import sleep

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect

@given(u'User chooses to add a friend name')
def step_add_friend(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Ny vän")


@when(u'User adds a name')
def step_add_name(context):
    context.page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox").click()
    context.page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox").fill("John No name")


@when(u'User do not add an email')
def step_not_add_email(context):
    context.page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox").click()
    context.page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox").fill("")


@then(u'System shows error message (name)')
def step_save_name(context):
    expect(context.page.get_by_role('button', name="Spara")).to_be_disabled()
    expect(context.page.get_by_text('Fyll i båda fälten för att lägga till din vän')).to_be_visible()
    sleep(0)
# ---------------------------------------------------

@given(u'User chooses to add a friend email')
def step_add_friend_email(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Ny vän")


@when(u'User do not add a name')
def step_not_add_name(context):
    context.page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox").click()
    context.page.get_by_role("main").locator("div").filter(has_text="Namn").get_by_role("textbox").fill("")


@when(u'User adds a email')
def step_add_email(context):
    context.page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox").click()
    context.page.get_by_role("main").locator("div").filter(has_text="E-post").get_by_role("textbox").fill("NoName@inter.net")

@then(u'System shows error message (email)')
def step_save_email(context):
    expect(context.page.get_by_role('button', name="Spara")).to_be_disabled()
    expect(context.page.get_by_text('Fyll i båda fälten för att lägga till din vän')).to_be_visible()
    sleep(0)
