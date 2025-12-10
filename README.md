# demoblaze-qa

A clean UI automation project built with **Python, Selenium, Pytest**, and **Page Object Model (POM)** to validate key user flows on the DemoBlaze site.

## Features
- Stable, repeatable UI test flows  
- Clean page objects and reliable locators  
- Reusable waits, fixtures, and utilities  
- Functional, regression, and basic integration tests

## Setup



Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Install allure (Optional for visual results)

```bash
pytest --alluredir=allure-results
allure serve allure-results
```