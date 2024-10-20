from browser import Browser
import time
import argparse
def login_to_website(url, username, password, proxy=None):
    browser = Browser.create(url, proxy)

    try:
        browser.get_page(url)
        username_input = browser.get_by_id("login-username")
        password_input = browser.get_by_id("login-password")

        if username_input and password_input:
            username_input.send_keys(username)
            password_input.send_keys(password)

            login_button = browser.get_by_xpath("//span[text()='Log In']")
            if login_button:
                browser.force_click(login_button)
                print("Успешный вход в систему!")
            else:
                print("Не удалось найти кнопку 'Log In'.")
        else:
            print("Не удалось найти поля для логина или пароля.")

    finally:
        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Пример программы.")
    parser.add_argument('--login', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()
    
    url = "https://accounts.spotify.com/en/login"
    username = args.login
    password = args.password
    proxy = None
    print(username, password)
    # login_to_website(url, username, password, proxy)