import sys
import os
from github import Github
import secretData


def create_local_repo(repo_name=str, repo_path=str, gitIgnoreList=list) -> None:
    """Create a local repository in a given projects folder

    Args:
        repo_name (str, optional): Project or repository name. Defaults to str.
        projects_path (str, optional): Projects folder location. Defaults to str.
        gitIgnoreList (list, optional): git ignore list for new project. Defaults to list.
    """
    # create a folder of new repo
    os.mkdir(repo_path)
    os.chdir(repo_path)

    # files needed in new repos
    for file in gitIgnoreList:
        os.system(f'echo {file} >> .gitignore')
    os.system(f'echo {repo_name} >> README.md')
    os.system(f'touch requirements.txt')

    # Start local repo
    os.system('git init')
    os.system('git add .')
    os.system('git commit -m "first commit"')

    print('\nLocal repository sucessfully created in ' + repo_path)


def create_github_repo(token=str, repo_name=str) -> str:
    """Create a new repo in github using the name given in terminal.

    Args:
        token (string): usr and password for github generated for this specific task. Defaults to str.
        repo_name (string): The name for new repository. Defaults to str.
        webpage (string, optional): github webpage. Defaults to 'https://github.com/'.
    """
    g = Github(token)
    user = g.get_user()
    username = user.login
    user.create_repo(repo_name)
    repo_url = f'https://github.com/{username}/{repo_name}.git'
    print('\nRemote repository sucessfully created in ' + repo_url)
    return repo_url


def link_repos(repo_path=str, repo_url=str) -> None:
    """use the terminal to link a remote branch to a new local branch.

    Args:
        repo_name (string, optional): The projects name. Defaults to str.
        projects_path (string, optional): the project location using absolute path. Defaults to str.
        webpage (string, optional): github webpage. Defaults to 'https://github.com/'.
    """
    os.system('cd ' + repo_path)
    os.system('git remote add origin ' + repo_url)
    os.system('git push -u origin master')

    print('\nProject Linked sucessfully!')


def create_pyenv(repo_path=str) -> None:
    """Create a Python3 virtual enviroment inside a new local project

    Args:
        projects_path (str, optional): Projects folder location in absolute path. Defaults to str.
        repo_name (str, optional): name of the project or repository. Defaults to str.
    """
    os.system('cd ' + repo_path)
    os.system('python3 -m venv venv')
    print('\nvitual enviroment created sucessfully!')


def main():
    # Arguments for functions in secrets
    token = secretData.gitToken
    git_ignore_list = secretData.gitIgnoreList
    
    #get path
    current_path = os.getcwd().replace('\"', '/')
    current_path = current_path.split('/')
    projects_path = ''
    for folder in current_path[1:-2]:
        projects_path += '/' + folder

    # System arguments
    args = sys.argv
    if len(args) < 2:
        print("[ERROR]: Type project's name after create statement. Write --help for more details")
        return None

    # set repositoty name
    repo_name = args[1]
    repo_path = f'{projects_path}/{repo_name}'

    # Main functions
    try:
        if '--help' in args:
            print("""

              You shoud write: create <project_name> <options>

              Options: -nolocal : Only make a remote repo
                       -noremote : Only make a local repo
                       -pyenv : Create a python vitual enviroment

                       """)
            return None

        if '-nolocal' not in args:
            create_local_repo(repo_name, repo_path, git_ignore_list)

        if '-noremote' not in args:
            repo_url = create_github_repo(token, repo_name)

        if '-nolocal' not in args and '-noremote' not in args:
            link_repos(repo_path, repo_url)

        if '-pyenv' in args and '-nolocal' not in args:
            create_pyenv(repo_path)

        if '-nolocal' not in args:
            os.system('code .')

        if '-nolocal' in args and '-noremote' in args:
            print('[ERROR]: Create a repo in local or remote.')

    except Exception as e:
        print(f'[ERROR]: {e}')
        return None


if __name__ == "__main__":
    main()
