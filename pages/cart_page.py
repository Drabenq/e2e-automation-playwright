from .base_page import BasePage


class CartPage(BasePage):
    path = "/cart.html"

    def item_names(self) -> list[str]:
        return self.page.locator(".cart_item .inventory_item_name").all_inner_texts()

    def checkout(self):
        self.by_test_id("checkout").click()
