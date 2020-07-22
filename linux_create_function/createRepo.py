import sys
import os
from selenium import webdriver
from github import Github


def create_github_repo(username=str, password=str, repo_name=str, webpage='https://github.com/') -> None:
    g = Github(username, password)
    user = g.get_user()
    user.login
    user.create_repo(repo_name)


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
    print('\nProyecto creado correctamente')
    print('Repositorio remoto en ' + f'{webpage}{username}/{repo_name}.git')
    print('Repositorio local en ' + f'{projects_path}{repo_name}')
    os.system('code .')


def main():
    username = 'sibarras'
    password = 'Paranga1@git'
    projects_path = '/home/sam/Desktop/Projects/'

    if len(sys.argv) < 2:
        print("[ERROR]: Colocar nombre del proyecto.")
        return None
    repo_name = str(sys.argv[1])

    try:
        create_github_repo(username, password, repo_name)
        link_github_repo(repo_name, projects_path)
    except Exception as e:
        print(f'[ERROR]: {e}')


if __name__ == "__main__":
    main()
