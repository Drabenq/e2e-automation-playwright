from playwright.sync_api import expect

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


def test_cart_badge_counts_added_items(inventory):
    expect(inventory.cart_badge).to_have_count(0)

    inventory.add_to_cart(BACKPACK)
    expect(inventory.cart_badge).to_have_text("1")

    inventory.add_to_cart(BIKE_LIGHT)
    expect(inventory.cart_badge).to_have_text("2")


def test_remove_item_updates_badge(inventory):
    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)

    inventory.remove_from_cart(BACKPACK)

    expect(inventory.cart_badge).to_have_text("1")


def test_cart_lists_selected_items(inventory, cart):
    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)

    inventory.go_to_cart()

    assert sorted(cart.item_names()) == sorted([BACKPACK, BIKE_LIGHT])


def test_cart_persists_after_reload(inventory, page):
    inventory.add_to_cart(BACKPACK)

    page.reload()

    expect(inventory.cart_badge).to_have_text("1")
