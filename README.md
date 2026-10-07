# E2E Automation with Playwright

![E2E tests](https://github.com/Drabenq/e2e-automation-playwright/actions/workflows/e2e.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)

End-to-end tests for [Sauce Demo](https://www.saucedemo.com), a demo e-commerce site, written with **Playwright for Python** and **pytest** using the **Page Object Model**.

## Coverage

| Flow | Scenarios |
|------|-----------|
| Login | Valid user, locked user, empty fields, wrong password, direct access without login |
| Cart | Badge count, remove items, cart contents, cart kept after reload |
| Sorting | Price low-high and high-low, name A-Z and Z-A |
| Checkout | Complete purchase, total = subtotal + tax, required form fields |

## Design

```
pages/          # Page Objects: selectors and actions live here, never in tests
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
tests/          # scenarios written in terms of user actions
```

- Selectors use the site's `data-test` attributes and visible roles, not fragile CSS paths.
- Web-first assertions (`expect(...)`) wait automatically, so there are no `sleep` calls.
- Each test runs in a fresh browser context, so tests do not depend on each other.
- Screenshots and Playwright traces are saved only when a test fails.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
pytest                       # headless
pytest --headed --slowmo 300 # watch the browser
```

Open a failure trace with `playwright show-trace test-results/<test>/trace.zip`.

## CI

GitHub Actions installs Chromium, runs the suite and uploads the HTML report. When a test fails it also uploads screenshots and traces.
