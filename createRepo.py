import sys
from selenium import webdriver

def create_github_repo(username = str, password = str, repo_name = str) -> None:
    """Create a new repo in github using the name given in terminal.

    Args:
        username (string): Username for github. Defaults to str.
        password (string): Password for github. Defaults to str.
        repo_name (string): The name for new repository. Defaults to str.
    """
    webpage = 'https://github.com/'
    browser = webdriver.Chrome()

    # go to login webpage
    browser.get(webpage + 'login')
    # login username
    nav_button = browser.find_element_by_xpath('//*[@id="login_field"]')
    nav_button.send_keys(username)
    # login password
    nav_button = browser.find_element_by_xpath('//*[@id="password"]')
    nav_button.send_keys(password)
    # press enter to get into account
    nav_button = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
    nav_button.click()

    # create new repo
    browser.get(webpage + 'new')
    # repo name
    nav_button = browser.find_element_by_xpath('//*[@id="repository_name"]')
    nav_button.send_keys(repo_name)
    # start new repo. Use css selector because the button was hidden
    nav_button = browser.find_element_by_css_selector('button.btn.btn-primary.first-in-line')
    nav_button.submit()
    
    browser.quit()


def main():
    username = 'sibarras'
    password = 'Paranga1@git'
    repo_name = str(sys.argv[1])
    
    create_github_repo(username, password, repo_name)

if __name__ == "__main__":
    main()