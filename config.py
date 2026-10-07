import os

# Public demo password shown on the Sauce Demo login page.
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
