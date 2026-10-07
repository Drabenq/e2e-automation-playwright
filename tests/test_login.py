import re

import pytest
from playwright.sync_api import expect

from config import PASSWORD


def test_valid_login_opens_inventory(login_page, page):
    login_page.login("standard_user", PASSWORD)

    expect(page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(page.locator(".inventory_item")).to_have_count(6)


def test_locked_out_user_sees_error(login_page):
    login_page.login("locked_out_user", PASSWORD)

    expect(login_page.error).to_contain_text("this user has been locked out")


@pytest.mark.parametrize(
    "username, password, message",
    [
        ("", PASSWORD, "Username is required"),
        ("standard_user", "", "Password is required"),
        ("standard_user", "wrong", "Username and password do not match"),
        ("unknown_user", PASSWORD, "Username and password do not match"),
    ],
    ids=["empty-username", "empty-password", "wrong-password", "unknown-user"],
)
def test_invalid_login_shows_error(login_page, page, username, password, message):
    login_page.login(username, password)

    expect(login_page.error).to_contain_text(message)
    expect(page).not_to_have_url(re.compile(r"inventory"))


def test_inventory_requires_login(page):
    page.goto("/inventory.html")

    expect(page.locator('[data-test="error"]')).to_contain_text("only access '/inventory.html' when you are logged in")
