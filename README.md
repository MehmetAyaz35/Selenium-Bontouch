# Selenium Web Automation Script

## Overview
This Python script demonstrates the use of Selenium for automating web navigation and interactions. It specifically automates a sequence of actions on the Bontouch website, including navigating to the careers page, handling cookies, clicking links, and filling forms.

## Features
- Navigates to the Bontouch homepage.
- Handles cookie notifications.
- Accesses the careers page via the website's menu.
- Clicks on specific career links and form elements.
- Enters an email address into a form field.
- Manages visibility and clickability of web elements using explicit waits.

## Prerequisites
To run this script, you'll need:
- Python installed on your machine.
- Selenium WebDriver.
- ChromeDriver compatible with the version of your Chrome browser.

## Installation
1. **Install Python**: Download and install Python from [python.org](https://www.python.org).
2. **Install Selenium**: Run the following command to install the Selenium package:
   ```bash
   pip install selenium
   ```
3. **ChromeDriver**: Download ChromeDriver from ChromeDriver - WebDriver for Chrome and ensure it is in your system's PATH.
## Setup
Ensure all prerequisites are installed.
Update the script with the correct paths for ChromeDriver if not in PATH.
Verify internet connectivity as this script requires access to the web.
## Running the Script
Execute the script from the command line:
```bash
   python bontouch.py
   ```
## Troubleshooting
Driver Compatibility: Ensure your ChromeDriver matches your Chrome browser's version.
Element Not Found: The website’s layout may have changed. Update the selectors accordingly.
## Contributions
Contributions to improve the script or extend its functionality are welcome. Please fork the repository and submit a pull request with your enhancements.



