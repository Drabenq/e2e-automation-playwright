import re

from .base_page import BasePage


def parse_price(text: str) -> float:
    return float(re.sub(r"[^\d.]", "", text))


class InventoryPage(BasePage):
    path = "/inventory.html"

    @property
    def items(self):
        return self.page.locator(".inventory_item")

    @property
    def cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    def item(self, name: str):
        return self.items.filter(has_text=name)

    def add_to_cart(self, name: str):
        self.item(name).get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, name: str):
        self.item(name).get_by_role("button", name="Remove").click()

    def sort_by(self, option: str):
        """option: az, za, lohi, hilo"""
        self.by_test_id("product-sort-container").select_option(option)

    def names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def prices(self) -> list[float]:
        return [parse_price(t) for t in self.page.locator(".inventory_item_price").all_inner_texts()]

    def go_to_cart(self):
        self.page.locator(".shopping_cart_link").click()
