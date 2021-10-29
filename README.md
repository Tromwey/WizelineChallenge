# WizelineChallenge
QA Automation challenge for Wizeline Bootcamp


--------------------------------Tools--------------------------------

IDE: VSCode 1.61.2

Programming language: Python 3.10

Required modules: Selenium 4.0.0, Pytest 6.2.5

Web Explorers: Edge 95.0.1020.30, Chrome 95.0.4638.54

--------------------------------Setup--------------------------------

Python installation:

https://www.python.org/downloads/

Python modules installation:

--Selenium

	pip install Selenium

--Pytest

	pip install Pytest

Web drivers for the web explorers are available in the folder WebDrivers


--------------------------------Guide--------------------------------

Tests:

--LoginPage

	A) Login with a valid user
	
	B) Login with an invalid user
	
--HomePage

	C) Logout from the home page
	
	D) Sort products by Price (low to high)
	
	E) Add multiple items to the shopping cart
	
	F) Add the specific product ‘Sauce Labs Onesie’ to the shopping cart
	
--CartPage

	G) Complete a purchase


Executing tests by Page

	pytest .\test_*NamePage*.py

Executing tests by Page with Report as outcome 

	pytest .\test_*NamePage*.py -v --html=../Report/*reportName*.html
