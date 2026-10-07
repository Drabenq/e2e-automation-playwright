import pytest

from config import PASSWORD
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage



@pytest.fixture()
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture()
def inventory(page):
    """Starts each test already logged in as the standard user."""
    LoginPage(page).open().login("standard_user", PASSWORD)
    return InventoryPage(page)


@pytest.fixture()
def cart(page):
    return CartPage(page)


@pytest.fixture()
def checkout(page):
    return CheckoutPage(page)
