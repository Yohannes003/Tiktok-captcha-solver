
---

# TikTok Login and CAPTCHA Solver

This project demonstrates how to use an undetected Chrome WebDriver with Selenium to automate TikTok login and CAPTCHA solving using the `sadcaptcha` API. It handles loading and saving cookies, ensuring you don't have to re-login every time, and solves CAPTCHA challenges if encountered during the login process.

## Requirements

- Python 3.x
- `undetected-chromedriver` library
- `selenium` library
- `selenium-stealth` library
- `pickle` (Standard Python library)
- `time` (Standard Python library)
- `tiktok_captcha_solver` library (for CAPTCHA solving)

You can install the required dependencies using the following command:

```bash
pip install undetected-chromedriver selenium selenium-stealth
```

For the CAPTCHA solver, you will need to use `sadcaptcha`:

1. Visit [sadcaptcha.com](https://www.sadcaptcha.com/) to generate an API key.  
2. Replace `API_KEY` in the script with the generated API key.

## How It Works

### Initialization and Configuration
1. The script uses `undetected-chromedriver` to start a Chrome browser session that is undetectable by TikTok.
2. The browser is configured using `selenium-stealth` to make it look like a regular browser (e.g., mimicking user behavior and system configurations).
3. The script attempts to load saved cookies from `tiktok_cookies.pkl` if they exist. If not, the user is prompted to login via CAPTCHA.

### Solving CAPTCHA
If a CAPTCHA is detected (or login is required), the script will use the `sadcaptcha` API to solve it automatically.

### Cookie Management
Cookies are saved to a file (`tiktok_cookies.pkl`) after a successful login and used for future sessions, preventing the need to log in repeatedly.

## How to Get Your Cookies

To capture and save the cookies for your TikTok account, you can run the `cookies.py` script. This will prompt you to log in manually to TikTok, and once logged in, it will capture and save the cookies to a file.

1. Create a new Python file named `cookies.py`.
2. Copy and paste the following code into `cookies.py`:

```python
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def save_cookies(driver, cookie_file='tiktok_cookies.pkl'):
    cookies = driver.get_cookies()
    with open(cookie_file, 'wb') as file:
        pickle.dump(cookies, file)
    print(f"Saved cookies to {cookie_file}.")

def get_tiktok_cookies():
    driver = webdriver.Chrome()  # Or use your undetected driver
    driver.get("https://www.tiktok.com/")
    time.sleep(5)  # Wait for the page to load and prompt for login

    # Manually log in to your TikTok account in the browser that opens
    input("Press Enter after logging in manually...")
    
    # Save cookies after logging in
    save_cookies(driver)
    driver.quit()

if __name__ == "__main__":
    get_tiktok_cookies()
```

3. Run the `cookies.py` script:

```bash
python cookies.py
```

4. This will open a browser window where you need to manually log in to your TikTok account.
5. After logging in, press Enter in the terminal to save the cookies to a file called `tiktok_cookies.pkl`.

Once you have the `tiktok_cookies.pkl` file, you can use it with the main script (`tiktok_scraper.py`) to avoid logging in every time and automatically bypass CAPTCHA.

## Functions

- **`initialize_driver()`**: Initializes the undetected Chrome WebDriver with stealth settings.
- **`load_cookies(driver, cookie_file='tiktok_cookies.pkl')`**: Loads cookies from the specified file and adds them to the browser.
- **`save_cookies(driver, cookie_file='tiktok_cookies.pkl')`**: Saves the current browser cookies to the specified file.
- **`solve_captcha(driver, api_key)`**: Uses the `sadcaptcha` API to solve CAPTCHA if present.
- **`open_tiktok_with_cookies(driver, api_key, cookie_file='tiktok_cookies.pkl')`**: Opens TikTok, attempts to load cookies, and solves CAPTCHA if necessary.
- **`visit_tiktok(api_key, cookie_file='tiktok_cookies.pkl')`**: The main function that visits TikTok and handles login and CAPTCHA solving.

## How to Run

1. Make sure you've installed all the required libraries.
2. Replace the `API_KEY` in the script with your own `sadcaptcha` API key (visit [sadcaptcha.com](https://www.sadcaptcha.com/) to generate one).
3. Run the `cookies.py` script to capture your cookies and save them as `tiktok_cookies.pkl`.
4. Run the `tiktok_scraper.py` script:

```bash
python tiktok_scraper.py
```

The script will attempt to load cookies from the `tiktok_cookies.pkl` file. If it doesn't find the file or if login is required, it will solve the CAPTCHA using the `sadcaptcha` API.

## Notes

- Make sure that you don’t violate TikTok's Terms of Service when using this script.
- The CAPTCHA-solving process requires a valid API key from `sadcaptcha`, which may involve some costs depending on usage.
- This script is intended for educational purposes. Use responsibly!

