import pytest
from playwright.sync_api import expect


def _start_checkout(inventory, cart, items):
    for name in items:
        inventory.add_to_cart(name)
    inventory.go_to_cart()
    cart.checkout()


def test_complete_purchase(inventory, cart, checkout, page):
    _start_checkout(inventory, cart, ["Sauce Labs Backpack"])

    checkout.fill_information("Ana", "Lopez", "1406")
    checkout.finish()

    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    expect(inventory.cart_badge).to_have_count(0)


def test_order_total_is_subtotal_plus_tax(inventory, cart, checkout):
    _start_checkout(inventory, cart, ["Sauce Labs Backpack", "Sauce Labs Onesie", "Sauce Labs Bolt T-Shirt"])

    checkout.fill_information("Ana", "Lopez", "1406")

    assert checkout.subtotal() == pytest.approx(sum(checkout.item_prices()))
    assert checkout.total() == pytest.approx(checkout.subtotal() + checkout.tax())


@pytest.mark.parametrize(
    "first, last, postal, message",
    [
        ("", "Lopez", "1406", "First Name is required"),
        ("Ana", "", "1406", "Last Name is required"),
        ("Ana", "Lopez", "", "Postal Code is required"),
    ],
    ids=["no-first-name", "no-last-name", "no-postal-code"],
)
def test_checkout_form_validation(inventory, cart, checkout, first, last, postal, message):
    _start_checkout(inventory, cart, ["Sauce Labs Backpack"])

    checkout.fill_information(first, last, postal)

    expect(checkout.error).to_contain_text(message)
