from .base_page import BasePage
from .inventory_page import parse_price


class CheckoutPage(BasePage):
    path = "/checkout-step-one.html"

    @property
    def error(self):
        return self.by_test_id("error")

    @property
    def complete_header(self):
        return self.page.locator(".complete-header")

    def fill_information(self, first: str, last: str, postal_code: str):
        self.by_test_id("firstName").fill(first)
        self.by_test_id("lastName").fill(last)
        self.by_test_id("postalCode").fill(postal_code)
        self.by_test_id("continue").click()

    def item_prices(self) -> list[float]:
        return [parse_price(t) for t in self.page.locator(".cart_item .inventory_item_price").all_inner_texts()]

    def subtotal(self) -> float:
        return parse_price(self.page.locator(".summary_subtotal_label").inner_text())

    def tax(self) -> float:
        return parse_price(self.page.locator(".summary_tax_label").inner_text())

    def total(self) -> float:
        return parse_price(self.page.locator(".summary_total_label").inner_text())

    def finish(self):
        self.by_test_id("finish").click()
