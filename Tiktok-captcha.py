import pickle
import os
import time
from tiktok_captcha_solver import SeleniumSolver
from selenium_stealth import stealth
import undetected_chromedriver as uc

def initialize_driver():
    driver = uc.Chrome(headless=False)  # Use headless=True for production if needed
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    return driver

def load_cookies(driver, cookie_file='tiktok_cookies.pkl'):
    if os.path.exists(cookie_file):
        with open(cookie_file, 'rb') as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        print(f"Loaded cookies from {cookie_file}.")
    else:
        print(f"Cookie file {cookie_file} not found. Proceeding without cookies.")

def save_cookies(driver, cookie_file='tiktok_cookies.pkl'):
    cookies = driver.get_cookies()
    with open(cookie_file, 'wb') as file:
        pickle.dump(cookies, file)
    print(f"Saved cookies to {cookie_file}.")

def solve_captcha(driver, api_key):
    sadcaptcha = SeleniumSolver(
        driver,
        api_key,
        mouse_step_size=1, 
        mouse_step_delay_ms=10  
    )
    try:
        solved = sadcaptcha.solve_captcha_if_present()
        if solved:
            print("CAPTCHA solved successfully!")
        else:
            print("No CAPTCHA detected or failed to solve CAPTCHA.")
    except Exception as e:
        print(f"Error solving CAPTCHA: {e}")


def open_tiktok_with_cookies(driver, api_key, cookie_file='tiktok_cookies.pkl'):
    url = "https://www.tiktok.com/"
    driver.get(url)
    time.sleep(3) 
  
    load_cookies(driver, cookie_file)
    driver.refresh()
    time.sleep(3)  
    if "login" in driver.page_source.lower() or "captcha" in driver.page_source.lower():
        print("Login required or CAPTCHA detected. Attempting to solve CAPTCHA...")
        solve_captcha(driver, api_key)
    else:
        print("Logged in using cookies or no CAPTCHA detected.")

    save_cookies(driver, cookie_file)

def visit_tiktok(api_key, cookie_file='tiktok_cookies.pkl'):
    driver = initialize_driver()
    try:
        # Open TikTok and handle login/CAPTCHA
        open_tiktok_with_cookies(driver, api_key, cookie_file)

        print("Proceeding with TikTok interaction...")
        # Example: Navigate to a specific TikTok page or perform a search
        driver.get("https://www.tiktok.com/@username")
        time.sleep(5) 
    finally:
        driver.quit()

API_KEY = "your api key"

if __name__ == "__main__":
    visit_tiktok(API_KEY)
