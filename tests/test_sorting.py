import pytest


@pytest.mark.parametrize("option, reverse", [("lohi", False), ("hilo", True)])
def test_sort_by_price(inventory, option, reverse):
    inventory.sort_by(option)

    prices = inventory.prices()
    assert prices == sorted(prices, reverse=reverse)


@pytest.mark.parametrize("option, reverse", [("az", False), ("za", True)])
def test_sort_by_name(inventory, option, reverse):
    inventory.sort_by(option)

    names = inventory.names()
    assert names == sorted(names, reverse=reverse)
