import sys
import os
from selenium import webdriver


def create_github_repo(username=str, password=str, repo_name=str, webpage='https://github.com/') -> None:
    """Create a new repo in github using the name given in terminal.

    Args:
        username (string): Username for github. Defaults to str.
        password (string): Password for github. Defaults to str.
        repo_name (string): The name for new repository. Defaults to str.
        webpage (string, optional): Github page. Defaults to 'https://github.com/'.
    """
    browser = webdriver.Firefox()

    # go to login webpage
    browser.get(f'{webpage}login')
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
    browser.get(f'{webpage}new')
    # repo name
    nav_button = browser.find_element_by_xpath('//*[@id="repository_name"]')
    nav_button.send_keys(repo_name)
    # start new repo. Use css selector because the button was hidden
    nav_button = browser.find_element_by_css_selector('button.btn.btn-primary.first-in-line')
    nav_button.submit()

    browser.quit()


def link_github_repo(repo_name=str, projects_path=str, webpage='https://github.com/', username='sibarras') -> None:
    """use the terminal to link a remote branch to a new local branch. Create a virtual enviroment and open visual studio code.

    Args:
        repo_name (string, optional): The projects name. Defaults to str.
        projects_path (string, optional): the project location using absolute path. Defaults to str.
        webpage (string, optional): github webpage. Defaults to 'https://github.com/'.
        username (string, optional): github username. Defaults to 'sibarras'.
    """
    os.mkdir(projects_path + repo_name)
    os.chdir(projects_path + repo_name)
    os.system('touch README.md')
    os.system('python -m venv venv')
    os.system('git init')
    os.system('git add .')
    os.system('git remote add origin ' + f'{webpage}{username}/{repo_name}.git')
    os.system('git push -u origin master')
    os.system('git status')
    os.system('code .')


def main():
    username = 'sibarras'
    password = 'Paranga1@git'

    projects_path = '/home/sam/Desktop/Projects/'
    repo_name = str(sys.argv[1])
    try:
        create_github_repo(username, password, repo_name)
        link_github_repo(repo_name, projects_path)
    except Exception as e:
        print(f'[ERROR]: {e}')


if __name__ == "__main__":
    main()
