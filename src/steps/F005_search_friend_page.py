import re

import playwright
from behave import given, when, then
from time import sleep

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect


@given(u'User want to see a friend name in the list')
def step_choose_friend_name(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Vänlista")
    expect(context.page.get_by_text('William Riker')).to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).to_be_visible()
    expect(context.page.get_by_text('Jean-Luc Picard')).to_be_visible()

    sleep(0)

@when(u'User search for a friend by name')
def step_search_friend_name(context):
    context.page.get_by_role("textbox", name="Sök namn").fill("Jean-Luc Picard")
    sleep(0)


@then(u'user finds a friend')
def step_found_friend_name(context):
    expect(context.page.get_by_text('Jean-Luc Picard')).to_be_visible()

    expect(context.page.get_by_text('James T. Kirk')).not_to_be_visible()
    expect(context.page.get_by_text('Spock')).not_to_be_visible()
    expect(context.page.get_by_text('William Riker')).not_to_be_visible()

    sleep(1)


#  --------------------------------------------

@given(u'User has a friend email in the list')
def step_choose_friend_email(context):
    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    search_page.get_by("link", "Vänlista")
    expect(context.page.get_by_text('William Riker')).to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).to_be_visible()
    expect(context.page.get_by_text('Jean-Luc Picard')).to_be_visible()

    sleep(0)
@when(u'User search for a friend by email')
def step_search_email(context):
    context.page.get_by_role("textbox", name="Sök namn").fill("captain.picard@starfleet.com")
    sleep(0)

@then(u'user finds a friend email')
def step_found_friend_email(context):
    expect(context.page.get_by_text('captain.picard@starfleet.com')).to_be_visible()

    expect(context.page.get_by_text('James T. Kirk')).not_to_be_visible()
    expect(context.page.get_by_text('Spock')).not_to_be_visible()
    expect(context.page.get_by_text('commander.riker@starfleet.com')).not_to_be_visible()
